# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from digitalhub.plugins import RunBuilder
from digitalhub_runtime_python.entities.run._base.status import RunStatusBaseRun

from digitalhub_runtime_hydra.entities._base.runtime_entity.builder import RuntimeEntityBuilderHydra
from digitalhub_runtime_hydra.entities._commons.enums import EntityKinds
from digitalhub_runtime_hydra.entities.run.hydra_subtask.entity import RunHydraRunSubtask
from digitalhub_runtime_hydra.entities.run.hydra_subtask.spec import (
    RunSpecHydraRunSubtask,
)


class RunHydraRunSubtaskBuilder(RunBuilder, RuntimeEntityBuilderHydra):
    """
    RunHydraRunSubtaskBuilder runner.
    """

    ENTITY_CLASS = RunHydraRunSubtask
    ENTITY_SPEC_CLASS = RunSpecHydraRunSubtask
    ENTITY_STATUS_CLASS = RunStatusBaseRun
    ENTITY_KIND = EntityKinds.RUN_HYDRA_SUBTASK.value

    def build_spec(self, **kwargs) -> RunSpecHydraRunSubtask:
        """
        Build entity spec object.

        Parameters
        ----------
        **kwargs : dict
            Keyword arguments for the constructor.

        Returns
        -------
        RunSpecHydraRunSubtask
            Spec object.
        """
        res = super().build_spec(**kwargs)
        return res
