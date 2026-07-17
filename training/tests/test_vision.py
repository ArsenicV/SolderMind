import numpy as np

from src.ai_pcb_quality.preprocessor import normalize_frame


def test_normalize_frame():
    frame = np.zeros((480, 640, 3), dtype=np.uint8)
    normalized = normalize_frame(frame)
    assert normalized.shape == (640, 640, 3)
    assert normalized.dtype == "float32"
    assert normalized.max() == 0.0
