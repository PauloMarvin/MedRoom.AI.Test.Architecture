from __future__ import annotations

from typing import List, Optional

import torch
import torch.nn.functional as torch_functional
from transformers import BertModel, PreTrainedTokenizerBase

from src.pipelines.pipeline_creator import PipelineCreator


class SimilarityBertCalculator:
    def __init__(
            self,
            bert_model: BertModel,
            tokenizer: PreTrainedTokenizerBase,
            text_pre_processor_pipeline: Optional[PipelineCreator] = None,
    ):
        self.device = torch.device(
            'cuda' if torch.cuda.is_available() else 'cpu',
        )
        self.bert_model = bert_model.to(self.device)
        self.tokenizer = tokenizer
        self.text_pre_processor_pipeline = text_pre_processor_pipeline
        if text_pre_processor_pipeline is not None:
            self.text_pre_processor_pipeline = text_pre_processor_pipeline

    def calculate_similarity(self, sentence1: str, sentence2: str) -> float:
        processed_base_text = self.__process_text(sentence1)
        processed_compare_text = self.__process_text(sentence2)
        similarity = self.calculate_similarity_by_cosine(
            processed_base_text,
            processed_compare_text,
        )
        return similarity

    def __process_text(self, sentence: str) -> str:
        if self.text_pre_processor_pipeline is None:
            return sentence
        else:
            return self.text_pre_processor_pipeline.apply_pipeline(sentence)

    def calculate_similarity_by_cosine(self, sentence1: str, sentence2: str) -> float:
        embeds = self.calculate_embeds([sentence1, sentence2])
        similarity = self.calculate_mean_of_embeds(embeds)

        return similarity

    def calculate_embeds(self, sentences: List[str]) -> List[torch.Tensor]:
        encodings = self.tokenizer(
            sentences,
            padding=True,
            return_tensors='pt',
        )

        encodings = encodings.to(self.device)

        with torch.no_grad():
            embeds = self.bert_model(**encodings)

        return embeds

    def calculate_mean_of_embeds(self, embeds: List[torch.Tensor]) -> float:
        embeds = embeds[0]
        embeds_means = torch.mean(embeds, dim=1)

        normalized = torch_functional.normalize(embeds_means, p=2, dim=1)
        mean_dist = normalized @ normalized.T
        mean_dist = torch.ones_like(mean_dist) - mean_dist

        similarity = mean_dist[0, 1].item()
        return similarity
