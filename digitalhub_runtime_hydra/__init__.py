# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0
from digitalhub_runtime_hydra.entities import entity_plugins
from digitalhub_runtime_hydra.entities._commons.enums import EntityKinds

entity_builders = tuple((plugin.kind, plugin.builder) for plugin in entity_plugins)

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
