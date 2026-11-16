# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

import pytest
from pydantic import ValidationError

from digitalhub_runtime_hydra.entities.function.hydra.builder import FunctionHydraBuilder
from digitalhub_runtime_hydra.entities.function.hydra.models import ConfigValidator, SourceValidator
from digitalhub_runtime_hydra.entities.run.hydra_job.builder import RunHydraRunJobBuilder
from digitalhub_runtime_hydra.entities.task.hydra_build.builder import TaskHydraBuildBuilder


def test_function_spec_validates_nested_source_and_config_models() -> None:
    spec = FunctionHydraBuilder().build_spec(
        source={"source": "main.py"},
        config={"path": "config.yaml"},
    )

    assert isinstance(spec.source, SourceValidator)
    assert isinstance(spec.config, ConfigValidator)


def test_task_spec_validates_build_instructions() -> None:
    spec = TaskHydraBuildBuilder().build_spec(function="function", instructions=["install"])

    assert spec.instructions == ["install"]

    with pytest.raises(ValidationError):
        TaskHydraBuildBuilder().build_spec(function="function", instructions=[1])


def test_run_spec_keeps_run_fields_separate_from_task_fields() -> None:
    builder = RunHydraRunJobBuilder()
    spec = builder.build_spec(task="task", inputs={}, parameters={}, config={}, workers=2)

    assert spec.inputs == {}
    assert spec.parameters == {}
    assert spec.workers == 2

    with pytest.raises(TypeError, match="instructions"):
        builder.build_spec(task="task", instructions=["install"])

    with pytest.raises(TypeError, match="replicas"):
        builder.build_spec(task="task", replicas=1)
