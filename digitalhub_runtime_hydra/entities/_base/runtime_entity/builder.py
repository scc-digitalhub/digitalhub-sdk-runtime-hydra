# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from digitalhub.plugins import RuntimeEntityBuilder, map_actions

from digitalhub_runtime_hydra.entities._commons.enums import Actions, EntityKinds


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
