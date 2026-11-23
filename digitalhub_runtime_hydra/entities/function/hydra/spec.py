# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from digitalhub_runtime_python.entities.function._base.spec import FunctionBaseSpec

from digitalhub_runtime_hydra.entities.function.hydra.models import HydraConfig, HydraSourceCode


class FunctionSpecHydra(FunctionBaseSpec):
    """
    FunctionSpecHydra specifications.
    """

    source: HydraSourceCode
    config: HydraConfig
