<div align="center"> 
  
  # SolderMind
  AI PCB Quality Assurance
</div>

---
## Overview
This repository implements an **AI Automated PCB Quality assurance solution** for industrial environments. Legacy Automated Optical Inspection (LAOI) systems in PCB manufacturing use rigid, rule based algorithms that fails to adapt to natural production variances. SolderMind replaces static thresholds with an autonomous multi agent pipeline that handels the defect lifecycle to detection to live recallibration.

The model was finetuned from COCO pretrained YOLOv8n weights using standard transfer learning. Training used default batch sampling provided by ultralytics.

- This repo implements the vision agent of the pipeline, which responsible for flag structural anomalies down to the micron layer, ignoring ambient lighting drift.

<br>

<br>

## Training pipeline

![pipeline](plots/vision_agent_pipeline.svg)


## Dataset

The model was trained on [roboflow PCB Defect detection dataset (V2)](https://universe.roboflow.com/uni-4sdfm/pcb-defects)

##### Class Distribution:
 | **Metric** | **Training** | **Testing** |
| --------------- | --------------- |------------|
| Row 1, Col 1    | Row 1, Col 2    | |
| Row 2, Col 1    | Row 2, Col 2    | |


## Model Selection

Considering the limited storage and RAM footprint, chose Yolo v8 Nano model for edge deployment.


## Evaluations







