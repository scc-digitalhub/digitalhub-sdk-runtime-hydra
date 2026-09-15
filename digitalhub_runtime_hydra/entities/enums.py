# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from enum import Enum


class EntityKinds(Enum):
    """
    Entity kinds.
    """

    FUNCTION_HYDRA = "hydra"
    TASK_HYDRA_BUILD = "hydra+build"
    TASK_HYDRA_JOB = "hydra+job"
    TASK_HYDRA_SUBTASK = "hydra+subtask"
    RUN_HYDRA_BUILD = "hydra+build:run"
    RUN_HYDRA_JOB = "hydra+job:run"
    RUN_HYDRA_SUBTASK = "hydra+subtask:run"

class Actions(Enum):
    """
    Task actions.
    """

    BUILD = "build"
    JOB = "job"
    SERVE = "serve"
    SUBTASK = "subtask"
