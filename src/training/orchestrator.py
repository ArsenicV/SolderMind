from __future__ import annotations

from .models import InferenceResult


class AIOrchestrator:
    def __init__(self, confidence_threshold: float = 0.5) -> None:
        self.confidence_threshold = confidence_threshold

    def evaluate(self, result: InferenceResult) -> InferenceResult:
        """Apply routing and threshold logic to an inference result."""
        filtered_defects = [
            defect for defect in result.defects if defect.confidence >= self.confidence_threshold
        ]
        return InferenceResult(
            board_id=result.board_id,
            defects=filtered_defects,
            raw_labels=[d.label for d in filtered_defects],
            metadata=result.metadata,
        )

    def should_alert(self, result: InferenceResult) -> bool:
        return len(result.defects) > 0
