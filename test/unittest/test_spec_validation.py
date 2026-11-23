# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from types import SimpleNamespace
from unittest.mock import Mock

import digitalhub_runtime_python.entities.function._base.entity as python_entity_module
import pytest
from digitalhub.entities.function._base.entity import Function
from pydantic import ValidationError

from digitalhub_runtime_hydra.entities.function.hydra.builder import FunctionHydraBuilder
from digitalhub_runtime_hydra.entities.function.hydra.entity import FunctionHydra
from digitalhub_runtime_hydra.entities.function.hydra.models import HydraConfig, HydraSourceCode
from digitalhub_runtime_hydra.entities.function.hydra.spec import FunctionSpecHydra
from digitalhub_runtime_hydra.entities.run.hydra_job.builder import RunHydraRunJobBuilder
from digitalhub_runtime_hydra.entities.task.hydra_build.builder import TaskHydraBuildBuilder


def test_function_spec_validates_nested_source_and_config_models() -> None:
    spec = FunctionHydraBuilder().build_spec(
        source={"source": "main.py", "handler": "main"},
        config={"path": "config.yaml"},
    )

    assert isinstance(spec.source, HydraSourceCode)
    assert isinstance(spec.config, HydraConfig)


def test_hydra_export_restores_typed_config_after_export(monkeypatch, tmp_path) -> None:
    config = HydraConfig(path="config.yaml", base64="Y29uZmln")
    function = object.__new__(FunctionHydra)
    function.spec = FunctionSpecHydra(
        source={"source": "remote-source", "handler": "main"},
        config=config,
    )
    function._context = Mock(return_value=SimpleNamespace(root=tmp_path))
    monkeypatch.setattr(python_entity_module, "write_text", Mock())

    def export(entity):
        assert entity.spec.config.base64 is None
        return "exported"

    monkeypatch.setattr(Function, "export", export)

    assert function.export() == "exported"
    assert function.spec.config is config
    assert config.base64 == "Y29uZmln"


def test_hydra_builder_preserves_config_check_with_source_mixin() -> None:
    builder = FunctionHydraBuilder()

    function = builder.build(
        kind=builder.ENTITY_KIND,
        project="project",
        name="function",
        code="print('hello')",
        handler="main",
        init_function="initialize",
        complete_function="complete",
        config={"path": "config.yaml"},
    )

    assert function.spec.source.base64 == "cHJpbnQoJ2hlbGxvJyk="
    assert function.spec.source.init_function == "initialize"
    assert function.spec.source.complete_function == "complete"
    assert function.spec.config.path == "config.yaml"


def test_task_spec_validates_build_instructions() -> None:
    spec = TaskHydraBuildBuilder().build_spec(function="function", instructions=["install"])

    assert spec.instructions == ["install"]

    with pytest.raises(ValidationError):
        TaskHydraBuildBuilder().build_spec(function="function", instructions=[1])


def test_run_spec_keeps_run_fields_separate_from_task_fields() -> None:
    builder = RunHydraRunJobBuilder()
    spec = builder.build_spec(function="function", task="task", inputs={}, parameters={}, config={}, workers=2)

    assert spec.inputs == {}
    assert spec.parameters == {}
    assert spec.workers == 2

    with pytest.raises(TypeError, match="instructions"):
        builder.build_spec(function="function", task="task", instructions=["install"])

    with pytest.raises(TypeError, match="replicas"):
        builder.build_spec(function="function", task="task", replicas=1)
