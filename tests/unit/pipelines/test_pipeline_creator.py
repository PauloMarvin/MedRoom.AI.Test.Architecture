from sklearn.preprocessing import FunctionTransformer

from src.pipelines.pipeline_creator import PipelineCreator
from src.processors.text_processor_utils import TextProcessorUtils


class TestPipelineCreator:
    sample_sentence = (
        'Olá! Esta é uma string de exemplo com algumas pontuações! Será que elas serão removidas? também '
        'há links como https://www.google.com.br e www.youtube.com.br e emoticons como 😀 😍 😠 😡'
    )

    patterns_data = {
        'positive_emoji': [
            '😀', '😃', '😄', '😁', '😆', '😅', '😂', '🤣', '😊', '😍', '🥰', '😎', '🤩', '🥳', '😇', '🙂', '🙃',
            '😋', '😜', '😉', '🥺', '😻', '🤗', '🤭', '🤫', '🤔', '🤗', '🥴', '🤤', '😏',
        ],
        'negative_emoji': [
            '😞', '😔', '😟', '😢', '😭', '😩', '😠', '😡', '🤬', '🤯', '😳', '😤', '😓', '😖', '😣', '😕', '🙁',
            '😒', '😑', '😶', '🥱', '😪', '😵', '🤢', '🤮', '🤧', '😷', '🥴', '🤒', '🤕',
        ],
    }

    pipeline_exemple = [
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

    def test_create_pipeline(self):
        pipeline = PipelineCreator(self.pipeline_exemple)

        expected_sentence = ('olá string pontuação ser ser removir haver link emoticon positive_emoji positive_emoji '
                             'negative_emoji negative_emoji')

        assert pipeline.apply_pipeline(self.sample_sentence) == expected_sentence
