# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from digitalhub.factory.plugins import CrudPlugin, EntityPlugin

from digitalhub_runtime_hydra.entities.function.hydra.builder import FunctionHydraBuilder
from digitalhub_runtime_hydra.entities.function.hydra.crud import new_function_hydra
from digitalhub_runtime_hydra.entities.run.hydra_build.builder import RunHydraRunBuildBuilder
from digitalhub_runtime_hydra.entities.run.hydra_job.builder import RunHydraRunJobBuilder
from digitalhub_runtime_hydra.entities.run.hydra_subtask.builder import RunHydraRunSubtaskBuilder
from digitalhub_runtime_hydra.entities.task.hydra_build.builder import TaskHydraBuildBuilder
from digitalhub_runtime_hydra.entities.task.hydra_job.builder import TaskHydraJobBuilder
from digitalhub_runtime_hydra.entities.task.hydra_subtask.builder import TaskHydraSubtaskBuilder

try:
    from digitalhub_runtime_hydra.runtimes.builder import (
        RuntimeHydraBuilder,
        RuntimeHydraJobBuilder,
        RuntimeHydraSubtaskBuilder,
    )
except ImportError as e:
    from digitalhub.utils.logger.logger import get_logger

    get_logger(__name__).debug(f"Error importing runtime builders: {e}")
    RuntimeHydraBuilder = None
    RuntimeHydraJobBuilder = None
    RuntimeHydraSubtaskBuilder = None

function_hydra_plugin = EntityPlugin(
    builder=FunctionHydraBuilder,
    shortcuts=(CrudPlugin(new_function_hydra),),
    runtime_builder=RuntimeHydraBuilder,
)

entity_plugins = (
    function_hydra_plugin,
    EntityPlugin(builder=TaskHydraBuildBuilder, runtime_builder=RuntimeHydraBuilder),
    EntityPlugin(builder=TaskHydraJobBuilder, runtime_builder=RuntimeHydraJobBuilder),
    EntityPlugin(builder=TaskHydraSubtaskBuilder, runtime_builder=RuntimeHydraSubtaskBuilder),
    EntityPlugin(builder=RunHydraRunBuildBuilder, runtime_builder=RuntimeHydraBuilder),
    EntityPlugin(builder=RunHydraRunJobBuilder, runtime_builder=RuntimeHydraJobBuilder),
    EntityPlugin(builder=RunHydraRunSubtaskBuilder, runtime_builder=RuntimeHydraSubtaskBuilder),
)  # SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0
