from __future__ import annotations

from typing import List, Tuple

from sklearn.pipeline import Pipeline
from sklearn.preprocessing import FunctionTransformer


class PipelineCreator:
    def __init__(self, pipeline_steps: List[Tuple[str, FunctionTransformer]]):
        self.text_pre_processor_pipeline = Pipeline(pipeline_steps)

    def apply_pipeline(self, text: str) -> str:
        processed_text = self.text_pre_processor_pipeline.fit_transform([text])[
            0
        ]
        return processed_text
