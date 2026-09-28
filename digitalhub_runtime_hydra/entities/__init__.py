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

function_hydra_plugin = EntityPlugin(
    builder=FunctionHydraBuilder,
    shortcuts=(CrudPlugin(new_function_hydra),),
)

entity_plugins = (
    function_hydra_plugin,
    EntityPlugin(builder=TaskHydraBuildBuilder),
    EntityPlugin(builder=TaskHydraJobBuilder),
    EntityPlugin(builder=TaskHydraSubtaskBuilder),
    EntityPlugin(builder=RunHydraRunBuildBuilder),
    EntityPlugin(builder=RunHydraRunJobBuilder),
    EntityPlugin(builder=RunHydraRunSubtaskBuilder),
)  # SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0
