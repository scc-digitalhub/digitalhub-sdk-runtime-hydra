# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from digitalhub.runtimes.builder import RuntimeBuilder

from digitalhub_runtime_hydra.runtimes.hydra_runtime import (
    RuntimeHydra,
    RuntimeHydraJob,
    RuntimeHydraSubtask,
)

class RuntimeHydraBuilder(RuntimeBuilder):
    """RuntimeHydraBuilder class."""

    RUNTIME_CLASS = RuntimeHydra


class RuntimeHydraJobBuilder(RuntimeBuilder):
    """RuntimeHydraJobBuilder class."""

    RUNTIME_CLASS = RuntimeHydraJob


class RuntimeHydraSubtaskBuilder(RuntimeBuilder):
    """RuntimeHydraSubtaskBuilder class."""

    RUNTIME_CLASS = RuntimeHydraSubtask
