import numpy as np
import cv2


def normalize_frame(frame: np.ndarray, size: tuple[int, int] = (640, 640)) -> np.ndarray:
    """Normalize an image frame for YOLO inference."""
    if frame is None:
        raise ValueError("Frame must not be None")

    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    resized = cv2.resize(frame, size, interpolation=cv2.INTER_LINEAR)
    normalized = resized.astype("float32") / 255.0
    return normalized


def load_image(path: str) -> np.ndarray:
    """Load an image from disk into an OpenCV BGR ndarray."""
    image = cv2.imread(path, cv2.IMREAD_COLOR)
    if image is None:
        raise FileNotFoundError(f"Could not load image from {path}")
    return image
