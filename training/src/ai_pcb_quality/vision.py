from __future__ import annotations

import numpy as np
from ultralytics import YOLO

from .models import DefectBoundingBox, InferenceResult, FrameMetadata


class YOLOInspector:
    def __init__(self, model_path: str | None = None) -> None:
        self.model_path = model_path or "yolov8n.pt"
        self.model = YOLO(self.model_path)

    def run_inference(self, frame: np.ndarray, metadata: FrameMetadata | None = None) -> InferenceResult:
        results = self.model(frame, imgsz=640)
        defects: list[DefectBoundingBox] = []

        for det in results:
            if det.boxes is None:
                continue
            for box in det.boxes:
                xyxy = box.xyxy.tolist()[0]
                confidence = float(box.conf[0])
                label = self.model.names[int(box.cls[0])]
                defects.append(
                    DefectBoundingBox(
                        x1=float(xyxy[0]),
                        y1=float(xyxy[1]),
                        x2=float(xyxy[2]),
                        y2=float(xyxy[3]),
                        confidence=confidence,
                        label=label,
                    )
                )

        labels = [defect.label for defect in defects]
        return InferenceResult(board_id=metadata.board_id if metadata else None, defects=defects, raw_labels=labels, metadata=metadata)
