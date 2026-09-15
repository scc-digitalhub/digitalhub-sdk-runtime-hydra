# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from digitalhub.entities._commons.utils import map_actions
from digitalhub.entities._mixin.runtime_entity.builder import RuntimeEntityBuilder

from digitalhub_runtime_hydra.entities.enums import Actions, EntityKinds


class RuntimeEntityBuilderHydra(RuntimeEntityBuilder):
    EXECUTABLE_KIND = EntityKinds.FUNCTION_HYDRA.value
    TASKS_KINDS = map_actions(
        [
            (
                EntityKinds.TASK_HYDRA_BUILD.value,
                Actions.BUILD.value,
            ),
            (
                EntityKinds.TASK_HYDRA_JOB.value,
                Actions.JOB.value,
            ),
            (
                EntityKinds.TASK_HYDRA_SUBTASK.value,
                Actions.SUBTASK.value,
            ),
        ]
    )
    RUN_KINDS = map_actions(
        [
            (
                EntityKinds.RUN_HYDRA_BUILD.value,
                Actions.BUILD.value,
            ),
            (
                EntityKinds.RUN_HYDRA_JOB.value,
                Actions.JOB.value,
            ),
            (
                EntityKinds.RUN_HYDRA_SUBTASK.value,
                Actions.SUBTASK.value,
            ),
        ]
    )