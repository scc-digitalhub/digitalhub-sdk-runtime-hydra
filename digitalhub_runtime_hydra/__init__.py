# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0
from digitalhub_runtime_hydra.entities.enums import EntityKinds
from digitalhub_runtime_hydra.entities.function.hydra.builder import FunctionHydraBuilder
from digitalhub_runtime_hydra.entities.run.hydra_build.builder import RunHydraRunBuildBuilder
from digitalhub_runtime_hydra.entities.run.hydra_job.builder import RunHydraRunJobBuilder
from digitalhub_runtime_hydra.entities.run.hydra_subtask.builder import RunHydraRunSubtaskBuilder
from digitalhub_runtime_hydra.entities.task.hydra_build.builder import TaskHydraBuildBuilder
from digitalhub_runtime_hydra.entities.task.hydra_job.builder import TaskHydraJobBuilder
from digitalhub_runtime_hydra.entities.task.hydra_subtask.builder import TaskHydraSubtaskBuilder

entity_builders = (
    (EntityKinds.FUNCTION_HYDRA.value, FunctionHydraBuilder),
    (EntityKinds.RUN_HYDRA_BUILD.value, RunHydraRunBuildBuilder),
    (EntityKinds.RUN_HYDRA_JOB.value, RunHydraRunJobBuilder),
    (EntityKinds.RUN_HYDRA_SUBTASK.value, RunHydraRunSubtaskBuilder),
    (EntityKinds.TASK_HYDRA_BUILD.value, TaskHydraBuildBuilder),
    (EntityKinds.TASK_HYDRA_JOB.value, TaskHydraJobBuilder),
    (EntityKinds.TASK_HYDRA_SUBTASK.value, TaskHydraSubtaskBuilder),
)

try:
    from digitalhub_runtime_hydra.runtimes.builder import (
        RuntimeHydraBuilder,
        RuntimeHydraJobBuilder,
        RuntimeHydraSubtaskBuilder,
    )

    runtime_builders = (
        (EntityKinds.FUNCTION_HYDRA.value, RuntimeHydraBuilder),
        (EntityKinds.RUN_HYDRA_BUILD.value, RuntimeHydraBuilder),
        (EntityKinds.RUN_HYDRA_JOB.value, RuntimeHydraJobBuilder),
        (EntityKinds.RUN_HYDRA_SUBTASK.value, RuntimeHydraSubtaskBuilder),
        (EntityKinds.TASK_HYDRA_BUILD.value, RuntimeHydraBuilder),
        (EntityKinds.TASK_HYDRA_JOB.value, RuntimeHydraJobBuilder),
        (EntityKinds.TASK_HYDRA_SUBTASK.value, RuntimeHydraSubtaskBuilder),
    )
except ImportError as e:
    from digitalhub.utils.logger.logger import get_logger

    logger = get_logger(__name__)
    logger.debug(f"Error importing runtime builders: {e}")
    runtime_builders = ()
