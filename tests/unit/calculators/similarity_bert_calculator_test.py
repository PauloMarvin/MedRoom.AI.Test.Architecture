from __future__ import annotations

import torch
from transformers import BertModel, BertTokenizer

from src.calculators.similarity_bert_calculator import SimilarityBertCalculator


class TestSimilarityBertCalculator:
    sample_sentence_1 = 'Estou sentido bastante dor de cabeça hoje.'
    sample_sentence_2 = 'Estou me sentido mal hoje, bastante dor de cabeça'
    bert_version = 'neuralmind/bert-base-portuguese-cased'
    tokenizer = BertTokenizer.from_pretrained(bert_version)
    bert_model = BertModel.from_pretrained(bert_version).eval()
    similarity_bert_calculator = SimilarityBertCalculator(
        bert_model=bert_model,
        tokenizer=tokenizer,
    )

    def test_calculate_similarity(self):
        similarity = self.similarity_bert_calculator.calculate_similarity(
            self.sample_sentence_1,
            self.sample_sentence_2, )

        expected_similarity = 0.09547793865203857

        assert similarity == expected_similarity

    def test_calculate_similarity_by_cosine(self):
        similarity = self.similarity_bert_calculator.calculate_similarity_by_cosine(
            self.sample_sentence_1,
            self.sample_sentence_2, )

        expected_similarity = 0.09547793865203857

        assert similarity == expected_similarity

    def test_calculate_embeds(self):
        embeds = self.similarity_bert_calculator.calculate_embeds(
            [self.sample_sentence_1],
        )

        expected_embeds = torch.tensor([
            0.0052, -0.2035, 0.3811, -0.3400, 0.3185, 0.0156, 0.0652, 0.1325,
            -0.0889, 0.4988,
        ])

        assert torch.allclose(embeds[0][0][0][:10], expected_embeds, atol=1e-4)

    def test_calculate_mean_of_embeds(self):
        embeds = self.similarity_bert_calculator.calculate_embeds(
            [self.sample_sentence_1, self.sample_sentence_2],
        )
        mean_of_embeds = self.similarity_bert_calculator.calculate_mean_of_embeds(
            embeds,
        )

        assert mean_of_embeds == 0.09547793865203857
