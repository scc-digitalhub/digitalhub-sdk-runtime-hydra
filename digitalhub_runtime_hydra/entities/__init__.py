# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from digitalhub.plugins import (
    Action,
    BuilderDef,
    CrudPlugin,
    ExecFamily,
    FunctionBuilder,
    RunBuilder,
    SourceBuilderMixin,
    Status,
    Task,
    TaskBuilder,
    TaskSpecFunction,
)
from digitalhub_runtime_python.entities.run._base.entity import RunBaseRun
from digitalhub_runtime_python.entities.run._base.status import RunStatusBaseRun

from digitalhub_runtime_hydra.entities._commons.enums import Actions, EntityKinds
from digitalhub_runtime_hydra.entities.function.hydra.builder import FunctionHydraBaseBuilder
from digitalhub_runtime_hydra.entities.function.hydra.crud import new_function_hydra
from digitalhub_runtime_hydra.entities.function.hydra.entity import FunctionHydra
from digitalhub_runtime_hydra.entities.function.hydra.spec import FunctionSpecHydra
from digitalhub_runtime_hydra.entities.run.hydra_build.spec import RunSpecHydraRunBuild
from digitalhub_runtime_hydra.entities.run.hydra_job.entity import RunHydraRunJob
from digitalhub_runtime_hydra.entities.run.hydra_job.spec import RunSpecHydraRunJob
from digitalhub_runtime_hydra.entities.run.hydra_subtask.spec import RunSpecHydraRunSubtask
from digitalhub_runtime_hydra.entities.task.hydra_build.spec import TaskSpecHydraBuild

# Imported on first use: the entities register even when the runtime cannot be
# imported, and the import error is reported when a run executes locally.
RUNTIME_HYDRA_BUILDER = "digitalhub_runtime_hydra.runtimes.builder:RuntimeHydraBuilder"
RUNTIME_HYDRA_JOB_BUILDER = "digitalhub_runtime_hydra.runtimes.builder:RuntimeHydraJobBuilder"
RUNTIME_HYDRA_SUBTASK_BUILDER = "digitalhub_runtime_hydra.runtimes.builder:RuntimeHydraSubtaskBuilder"

hydra = ExecFamily(
    executable=BuilderDef(
        EntityKinds.FUNCTION_HYDRA,
        FunctionHydra,
        FunctionSpecHydra,
        Status,
        base=FunctionHydraBaseBuilder,
        shortcuts=(CrudPlugin(new_function_hydra),),
    ),
    actions={
        Actions.BUILD: Action(
            task=BuilderDef(EntityKinds.TASK_HYDRA_BUILD, Task, TaskSpecHydraBuild, Status, base=TaskBuilder),
            run=BuilderDef(
                EntityKinds.RUN_HYDRA_BUILD, RunBaseRun, RunSpecHydraRunBuild, RunStatusBaseRun, base=RunBuilder
            ),
        ),
        Actions.JOB: Action(
            task=BuilderDef(EntityKinds.TASK_HYDRA_JOB, Task, TaskSpecFunction, Status, base=TaskBuilder),
            run=BuilderDef(
                EntityKinds.RUN_HYDRA_JOB, RunHydraRunJob, RunSpecHydraRunJob, RunStatusBaseRun, base=RunBuilder
            ),
            runtime_builder=RUNTIME_HYDRA_JOB_BUILDER,
        ),
        Actions.SUBTASK: Action(
            task=BuilderDef(EntityKinds.TASK_HYDRA_SUBTASK, Task, TaskSpecFunction, Status, base=TaskBuilder),
            run=BuilderDef(
                EntityKinds.RUN_HYDRA_SUBTASK,
                RunHydraRunJob,
                RunSpecHydraRunSubtask,
                RunStatusBaseRun,
                base=RunBuilder,
            ),
            runtime_builder=RUNTIME_HYDRA_SUBTASK_BUILDER,
        ),
    },
    runtime_builder=RUNTIME_HYDRA_BUILDER,
)

entity_plugins = (*hydra.plugins(),)
