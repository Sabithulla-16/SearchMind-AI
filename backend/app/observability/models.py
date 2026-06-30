from pydantic import BaseModel, Field

from typing import Dict


class StageMetric(BaseModel):

    name: str

    duration_ms: float = 0.0


class PipelineMetrics(BaseModel):

    stages: Dict[str, StageMetric] = Field(
        default_factory=dict
    )

    counters: Dict[str, int] = Field(
        default_factory=dict
    )