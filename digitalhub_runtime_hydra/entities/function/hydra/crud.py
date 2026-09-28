# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

import typing

from digitalhub.entities.function.crud import new_function

from digitalhub_runtime_hydra.entities.function.hydra.builder import FunctionHydraBuilder

if typing.TYPE_CHECKING:
    from digitalhub_runtime_hydra.entities.function.hydra.entity import FunctionHydra


def new_function_hydra(
    project: str,
    name: str,
    source: dict | None = None,
    code: str | None = None,
    code_src: str | None = None,
    base64: str | None = None,
    handler: str | None = None,
    init_function: str | None = None,
    complete_function: str | None = None,
    lang: str | None = None,
    config: dict | None = None,
    config_src: str | None = None,
    config_content: str | None = None,
    config_base64: str | None = None,
    config_path: str | None = None,
    image: str | None = None,
    base_image: str | None = None,
    python_version: str | None = None,
    requirements: list[str] | str | None = None,
    uuid: str | None = None,
    version: str | None = None,
    description: str | None = None,
    labels: list[str] | None = None,
    embedded: bool = False,
) -> FunctionHydra:
    """Create a Hydra function entity."""
    return new_function(
        project=project,
        name=name,
        kind=FunctionHydraBuilder.ENTITY_KIND,
        uuid=uuid,
        version=version,
        description=description,
        labels=labels,
        embedded=embedded,
        source=source,
        code=code,
        code_src=code_src,
        base64=base64,
        handler=handler,
        init_function=init_function,
        complete_function=complete_function,
        lang=lang,
        config=config,
        config_src=config_src,
        config_content=config_content,
        config_base64=config_base64,
        config_path=config_path,
        image=image,
        base_image=base_image,
        python_version=python_version,
        requirements=requirements,
    )
