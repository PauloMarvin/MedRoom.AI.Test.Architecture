from __future__ import annotations

from sklearn.preprocessing import FunctionTransformer
from transformers import BertModel
from transformers import BertTokenizer

from src.calculators.similarity_bert_calculator import SimilarityBertCalculator
from src.pipelines.pipeline_creator import PipelineCreator
from src.processors.text_processor_utils import TextProcessorUtils


def main():
    patterns_data = {
        'positive_emoji': [
            '😀', '😃', '😄', '😁', '😆', '😅', '😂', '🤣', '😊', '😍', '🥰', '😎', '🤩', '🥳', '😇', '🙂', '🙃', '😋', '😜', '😉', '🥺',
            '😻', '🤗', '🤭', '🤫', '🤔', '🤗', '🥴', '🤤', '😏',
        ],
        'negative_emoji': [
            '😞', '😔', '😟', '😢', '😭', '😩', '😠', '😡', '🤬', '🤯', '😳', '😤', '😓', '😖', '😣', '😕', '🙁', '😒',
            '😑', '😶', '🥱', '😪', '😵', '🤢', '🤮', '🤧', '😷', '🥴', '🤒', '🤕',
        ],
    }

    text_pre_processor_pipeline = [
        ('lower_text', FunctionTransformer(TextProcessorUtils.lower_text_corpus)),
        (
            'remove_punctuation',
            FunctionTransformer(
                TextProcessorUtils.remove_punctuation_corpus,
            ),
        ),
        (
            'remove_with_regex',
            FunctionTransformer(
                TextProcessorUtils.remove_sites_corpus,
            ),
        ),
        (
            'remove_stopwords',
            FunctionTransformer(
                TextProcessorUtils.remove_stopwords_corpus,
            ),
        ),
        (
            'lemmatization',
            FunctionTransformer(
                TextProcessorUtils.lemmatization_corpus,
            ),
        ),
        (
            'replace_matches',
            FunctionTransformer(
                TextProcessorUtils.replace_matches_corpus,
                kw_args={
                    'patterns_dict': patterns_data,
                },
            ),
        ),
    ]
    text_processor_pipeline = PipelineCreator(text_pre_processor_pipeline)

    bert_version = 'neuralmind/bert-base-portuguese-cased'
    tokenizer = BertTokenizer.from_pretrained(bert_version)
    model = BertModel.from_pretrained(bert_version)
    model = model.eval()

    bert_similarity_calculator = SimilarityBertCalculator(
        bert_model=model,
        text_pre_processor_pipeline=text_processor_pipeline,
        tokenizer=tokenizer,
    )

    print('Bem vindo ao calculador de similaridade de frases!')
    print('O calculador utiliza um modelo BERT para calcular a similaridade entre duas frases.')
    print('O score de similaridade é dado em porcentagem, sendo 0% totalmente diferente e 100% totalmente igual.')
    sentence_1 = str(input('Digite a primeira frase: '))
    sentence_2 = str(input('Digite a segunda frase: '))

    similarity = bert_similarity_calculator.calculate_similarity(
        sentence_1,
        sentence_2,
    )
    similarity_percentage = (1 - round(similarity, 2)) * 100
    print(f'O score de similaridade é de {similarity_percentage}%')

    print(f'O score de similaridade é de {similarity_percentage}')


if __name__ == '__main__':
    main()
