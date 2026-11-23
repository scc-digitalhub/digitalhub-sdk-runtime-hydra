# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from digitalhub.entities._base.entity.status import Status
from digitalhub.entities.task._base.builder import TaskBuilder
from digitalhub.entities.task._base.spec import TaskSpecFunction

from digitalhub_runtime_hydra.entities._base.runtime_entity.builder import RuntimeEntityBuilderHydra
from digitalhub_runtime_hydra.entities._commons.enums import EntityKinds
from digitalhub_runtime_hydra.entities.task.hydra_job.entity import TaskHydraJob


class TaskHydraJobBuilder(TaskBuilder, RuntimeEntityBuilderHydra):
    """
    TaskHydraJobBuilder jober.
    """

    ENTITY_CLASS = TaskHydraJob
    ENTITY_SPEC_CLASS = TaskSpecFunction
    ENTITY_STATUS_CLASS = Status
    ENTITY_KIND = EntityKinds.TASK_HYDRA_JOB.value
