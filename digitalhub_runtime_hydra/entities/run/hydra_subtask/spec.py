# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from digitalhub_runtime_hydra.entities.run.hydra_job.spec import RunSpecHydraRunJob


class RunSpecHydraRunSubtask(RunSpecHydraRunJob):
    """RunSpecHydraRunSubtask specifications."""

    job_ref: str | None = None
