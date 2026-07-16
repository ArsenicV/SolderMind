from __future__ import annotations

from pydantic import BaseModel


class FrameMetadata(BaseModel):
    board_id: str | None = None
    capture_time: str | None = None
    source: str | None = None


class DefectBoundingBox(BaseModel):
    x1: float
    y1: float
    x2: float
    y2: float
    confidence: float
    label: str


class InferenceResult(BaseModel):
    board_id: str | None = None
    defects: list[DefectBoundingBox]
    raw_labels: list[str] = []
    metadata: FrameMetadata | None = None
