from __future__ import annotations

import cv2
import numpy as np
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse

from .models import FrameMetadata
from .preprocessor import normalize_frame
from .vision import YOLOInspector

app = FastAPI(title="AI PCB Quality API")

inspector = YOLOInspector()


@app.post("/infer")
async def infer_image(file: UploadFile = File(...), board_id: str | None = None):
    contents = await file.read()
    np_arr = np.frombuffer(contents, np.uint8)
    frame = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)
    if frame is None:
        return JSONResponse(status_code=400, content={"error": "Invalid image file"})

    normalized = normalize_frame(frame)
    metadata = FrameMetadata(board_id=board_id, source=file.filename)
    result = inspector.run_inference(normalized, metadata=metadata)
    return result.model_dump()


@app.get("/health")
def health_check():
    return {"status": "ok"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
