# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from digitalhub.plugins import FunctionBuilder, SourceBuilderMixin

from digitalhub_runtime_hydra.entities.function.hydra.utils import config_check


class FunctionHydraBaseBuilder(SourceBuilderMixin, FunctionBuilder):
    """
    Base of the hydra function builder: checks the Hydra configuration.

    ``_prepare_kwargs`` replaces the hook of ``SourceBuilderMixin``, so the
    mixin is part of this base instead of a ``BuilderDef`` mixin.
    """

    def _prepare_kwargs(self, kwargs: dict) -> dict:
        return config_check(**kwargs)
