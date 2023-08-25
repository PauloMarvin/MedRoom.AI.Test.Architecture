import pytest

from src.processors.text_processor_utils import TextProcessorUtils


class TestTextProcessorUtils:
    sample_string = (
        'Olá! Esta é uma string de exemplo com algumas pontuações! Será que elas serão removidas? também '
        'há links como https://www.google.com.br e www.youtube.com.br e emoticons como 😀 😍 😠 😡')

    def test_remove_sites(self):
        sample_string = self.sample_string

        expected_string = (
            'Olá! Esta é uma string de exemplo com algumas pontuações! Será que elas serão removidas? também há links '
            'como e e emoticons como 😀 😍 😠 😡')

        assert TextProcessorUtils.remove_sites(sample_string) == expected_string

    def test_remove_punctuation(self):
        sample_string = self.sample_string

        expected_string = ('Olá Esta é uma string de exemplo com algumas pontuações Será que elas serão removidas '
                           'também há links como https://www.google.com.br e www.youtube.com.br e emoticons como 😀 '
                           '😍 😠 😡')

        assert TextProcessorUtils.remove_punctuation(sample_string) == expected_string

    def test_lower_text(self):
        sample_string = self.sample_string

        expected_string = (
            'olá! esta é uma string de exemplo com algumas pontuações! será que elas serão removidas? também há links '
            'como https://www.google.com.br e www.youtube.com.br e emoticons como 😀 😍 😠 😡')

        assert TextProcessorUtils.lower_text(sample_string) == expected_string

    def test_remove_stopwords(self):
        sample_string = self.sample_string

        expected_string = ('Olá ! string pontuações ! Será serão removidas ? há links https://www.google.com.br '
                           'www.youtube.com.br emoticons 😀 😍 😠 😡')
        assert TextProcessorUtils.remove_stopwords(sample_string) == expected_string

    def test_lemmatization(self):
        sample_string = self.sample_string

        expected_string = (
            'Olá ! este ser um string de exemplo com algum pontuação ! ser que ele ser removir ? também haver link '
            'como https://www.google.com.br e www.youtube.com.br e emoticons como 😀 😍 😠 😡')

        assert TextProcessorUtils.lemmatization(sample_string) == expected_string

    def test_replace_matches(self):
        patterns_data = {
            "positive_emoji": [
                '😀', '😃', '😄', '😁', '😆', '😅', '😂', '🤣', '😊', '😍',
                '🥰', '😎', '🤩', '🥳', '😇', '🙂', '🙃', '😋', '😜', '😉',
                '🥺', '😻', '🤗', '🤭', '🤫', '🤔', '🤗', '🥴', '🤤', '😏',
            ],
            "negative_emoji": [
                '😞', '😔', '😟', '😢', '😭', '😩', '😠', '😡', '🤬', '🤯',
                '😳', '😤', '😓', '😖', '😣', '😕', '🙁', '😒', '😑', '😶',
                '🥱', '😪', '😵', '🤢', '🤮', '🤧', '😷', '🥴', '🤒', '🤕',
            ]
        }

        sample_string = self.sample_string

        expected_string = ('Olá! Esta é uma string de exemplo com algumas pontuações! Será que elas serão removidas? '
                           'também há links como https://www.google.com.br e www.youtube.com.br e emoticons como '
                           'positive_emoji positive_emoji negative_emoji negative_emoji')

        assert TextProcessorUtils.replace_matches(sample_string, patterns_data) == expected_string


if __name__ == '__main__':
    pytest.main([__file__])
