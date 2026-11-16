# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from digitalhub_runtime_python.entities.function._base.models import PythonSourceCode
from pydantic import BaseModel, ConfigDict


class HydraSourceCode(PythonSourceCode):
    """Source code model for Hydra functions."""

    complete_function: str | None = None


SourceValidator = HydraSourceCode


class ConfigValidator(BaseModel):
    """
    Config params.
    """

    model_config = ConfigDict(use_enum_values=True)

    source: str | None = None
    "Pointer to source code."

    path: str | None = None
    "Config path."

    base64: str | None = None
    "Config (base64 encoded)."
