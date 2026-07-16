from __future__ import annotations

"""Placeholder for the Solermind PCB inference pipeline.

This file is intended to hold the end-to-end inference workflow:
- load the trained model,
- preprocess the image,
- run inference,
- post-process detections,
- return structured results.
"""


class InferencePipeline:
    def __init__(self) -> None:
        pass

    def run(self, image):
        raise NotImplementedError("Inference pipeline implementation to be added.")
