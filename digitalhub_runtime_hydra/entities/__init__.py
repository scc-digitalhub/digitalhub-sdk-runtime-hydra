# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from digitalhub.plugins import CrudPlugin, EntityPlugin

from digitalhub_runtime_hydra.entities.function.hydra.builder import FunctionHydraBuilder
from digitalhub_runtime_hydra.entities.function.hydra.crud import new_function_hydra
from digitalhub_runtime_hydra.entities.run.hydra_build.builder import RunHydraRunBuildBuilder
from digitalhub_runtime_hydra.entities.run.hydra_job.builder import RunHydraRunJobBuilder
from digitalhub_runtime_hydra.entities.run.hydra_subtask.builder import RunHydraRunSubtaskBuilder
from digitalhub_runtime_hydra.entities.task.hydra_build.builder import TaskHydraBuildBuilder
from digitalhub_runtime_hydra.entities.task.hydra_job.builder import TaskHydraJobBuilder
from digitalhub_runtime_hydra.entities.task.hydra_subtask.builder import TaskHydraSubtaskBuilder

# Imported on first use: the entities register even when the runtime cannot be
# imported, and the import error is reported when a run executes locally.
RUNTIME_HYDRA_BUILDER = "digitalhub_runtime_hydra.runtimes.builder:RuntimeHydraBuilder"
RUNTIME_HYDRA_JOB_BUILDER = "digitalhub_runtime_hydra.runtimes.builder:RuntimeHydraJobBuilder"
RUNTIME_HYDRA_SUBTASK_BUILDER = "digitalhub_runtime_hydra.runtimes.builder:RuntimeHydraSubtaskBuilder"

function_hydra_plugin = EntityPlugin(
    builder=FunctionHydraBuilder,
    shortcuts=(CrudPlugin(new_function_hydra),),
    runtime_builder=RUNTIME_HYDRA_BUILDER,
)

entity_plugins = (
    function_hydra_plugin,
    EntityPlugin(builder=TaskHydraBuildBuilder, runtime_builder=RUNTIME_HYDRA_BUILDER),
    EntityPlugin(builder=TaskHydraJobBuilder, runtime_builder=RUNTIME_HYDRA_JOB_BUILDER),
    EntityPlugin(builder=TaskHydraSubtaskBuilder, runtime_builder=RUNTIME_HYDRA_SUBTASK_BUILDER),
    EntityPlugin(builder=RunHydraRunBuildBuilder, runtime_builder=RUNTIME_HYDRA_BUILDER),
    EntityPlugin(builder=RunHydraRunJobBuilder, runtime_builder=RUNTIME_HYDRA_JOB_BUILDER),
    EntityPlugin(builder=RunHydraRunSubtaskBuilder, runtime_builder=RUNTIME_HYDRA_SUBTASK_BUILDER),
)  # SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0
