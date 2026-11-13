# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from digitalhub_runtime_python.entities.function._base.spec import FunctionBaseSpec, FunctionBaseValidator

from digitalhub_runtime_hydra.entities.function.hydra.models import ConfigValidator, SourceValidator


class FunctionSpecHydra(FunctionBaseSpec):
    """
    FunctionSpecHydra specifications.
    """

    def __init__(
        self,
        source: dict | None = None,
        config: dict | None = None,
        image: str | None = None,
        base_image: str | None = None,
        python_version: str | None = None,
        requirements: list | None = None,
    ) -> None:
        super().__init__(
            source=source,
            image=image,
            base_image=base_image,
            python_version=python_version,
            requirements=requirements,
        )
        self.config = config


class FunctionValidatorHydra(FunctionBaseValidator[SourceValidator]):
    """
    FunctionValidatorHydra validator.
    """

    source: SourceValidator
    """Source code validator"""

    config: ConfigValidator
    """Config validator"""
