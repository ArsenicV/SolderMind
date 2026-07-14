# SolderMind
This repository contains the initial scaffold for an AI-native PCB quality assurance solution.
It focuses on edge computer vision using OpenCV and Ultralytics YOLO, with a structured ingestion and inference pipeline.

#### Why YOLO?
Becuase of the project's requirements and fast-paced environment, YOLO is the best in case of speed and accuracy.
Used Transfer Learning to train this model


#### Goals

- Capture high-resolution PCB images from edge cameras
- Run YOLO-based defect/anomaly detection
- Normalize and preprocess frame data with OpenCV
- Provide a lightweight inference API for integration
- Enable future extensions for CAD/Gerber verification, orchestration, and retraining

#### Key Components
- `src/ai_pcb_quality/preprocessor.py` - image normalization and frame decoding
- `src/ai_pcb_quality/vision.py` - Ultralytics YOLO inference wrapper
- `src/ai_pcb_quality/ingestion.py` - Kafka/MQTT ingestion skeleton
- `src/ai_pcb_quality/orchestrator.py` - decisioning and result routing stub
- `src/ai_pcb_quality/api.py` - FastAPI application for inference


#### Stack
- Python 3.11+
- `ultralytics` YOLO for edge computer vision
- `opencv-python-headless` for image preprocessing
- `FastAPI` / `uvicorn` for service API
- `kafka-python` / `paho-mqtt` for streaming ingestion skeleton
- `pydantic` for typed inference results

---
```
[todo]: Planning to use Curriculum Learning and improve the accuracy of the model
[todo]: Model evaluation
```
