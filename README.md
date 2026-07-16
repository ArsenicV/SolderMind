# AI-Native Automated PCB Quality Assurance

This repository contains the initial scaffold for an AI-native PCB quality assurance solution.
It focuses on edge computer vision using OpenCV and Ultralytics YOLO, with a structured ingestion and inference pipeline.

## Goals

- Capture high-resolution PCB images from edge cameras
- Run YOLO-based defect/anomaly detection
- Normalize and preprocess frame data with OpenCV
- Provide a lightweight inference API for integration
- Enable future extensions for CAD/Gerber verification, orchestration, and retraining

## Key Components

- `src/ai_pcb_quality/preprocessor.py` - image normalization and frame decoding
- `src/ai_pcb_quality/vision.py` - Ultralytics YOLO inference wrapper
- `src/ai_pcb_quality/ingestion.py` - Kafka/MQTT ingestion skeleton
- `src/ai_pcb_quality/orchestrator.py` - decisioning and result routing stub
- `src/ai_pcb_quality/api.py` - FastAPI application for inference

## Tech Stack

- Python 3.11+
- `ultralytics` YOLO for edge computer vision
- `opencv-python-headless` for image preprocessing
- `FastAPI` / `uvicorn` for service API
- `kafka-python` / `paho-mqtt` for streaming ingestion skeleton
- `pydantic` for typed inference results

## Getting Started

1. Create a virtual environment:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the API:
   ```bash
   python -m src.ai_pcb_quality.api
   ```
4. POST an image to `/infer` to get YOLO inference results.

## Next steps

- Add CAD/Gerber verification and board tolerance matching
- Implement Kafka/MQTT ingestion and edge data capture
- Add persistent defect storage, audit logging, and operator alerts
- Build a retraining pipeline for active learning
