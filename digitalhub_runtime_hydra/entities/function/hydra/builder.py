# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from digitalhub.plugins import Status
from digitalhub_runtime_python.entities.function._base.builder import FunctionBaseBuilder

from digitalhub_runtime_hydra.entities._base.runtime_entity.builder import RuntimeEntityBuilderHydra
from digitalhub_runtime_hydra.entities._commons.enums import EntityKinds
from digitalhub_runtime_hydra.entities.function.hydra.entity import FunctionHydra
from digitalhub_runtime_hydra.entities.function.hydra.spec import FunctionSpecHydra
from digitalhub_runtime_hydra.entities.function.hydra.utils import config_check


class FunctionHydraBuilder(FunctionBaseBuilder, RuntimeEntityBuilderHydra):
    """
    FunctionHydra builder.
    """

    ENTITY_CLASS = FunctionHydra
    ENTITY_SPEC_CLASS = FunctionSpecHydra
    ENTITY_STATUS_CLASS = Status
    ENTITY_KIND = EntityKinds.FUNCTION_HYDRA.value

    def _prepare_kwargs(self, kwargs: dict) -> dict:
        return config_check(**kwargs)
