from __future__ import annotations

import re
from typing import Any, Dict, List

import spacy
from spacy.matcher import Matcher


class TextProcessorUtils:
    nlp_object = spacy.load(
        'pt_core_news_sm',
        disable=['parser', 'ner', 'tagger'],
    )
    nlp_object.add_pipe('emoji', first=True)

    @classmethod
    def remove_sites_corpus(cls, corpus: List[str]) -> List[str]:
        formatted_corpus = []
        for text in corpus:
            formatted_corpus.append(cls.remove_sites(text))
        return formatted_corpus

    @classmethod
    def remove_punctuation_corpus(cls, corpus: List[str]) -> List[str]:
        formatted_corpus = []
        for text in corpus:
            formatted_corpus.append(cls.remove_punctuation(text))
        return formatted_corpus

    @classmethod
    def lower_text_corpus(cls, corpus: List[str]) -> List[str]:
        formatted_corpus = []
        for text in corpus:
            formatted_corpus.append(cls.lower_text(text))
        return formatted_corpus

    @classmethod
    def remove_stopwords_corpus(cls, corpus: List[str]) -> List[str]:
        formatted_corpus = []
        for text in corpus:
            formatted_corpus.append(cls.remove_stopwords(text))
        return formatted_corpus

    @classmethod
    def lemmatization_corpus(cls, corpus: List[str]) -> List[str]:
        formatted_corpus = []
        for text in corpus:
            formatted_corpus.append(cls.lemmatization(text))
        return formatted_corpus

    @classmethod
    def replace_matches_corpus(
        cls,
        corpus: List[str],
        patterns_dict: Dict[str, List[List[Dict[str, Any]]]],
    ) -> List[str]:
        formatted_corpus = []
        for text in corpus:
            formatted_corpus.append(cls.replace_matches(text, patterns_dict))
        return formatted_corpus

    @staticmethod
    def remove_sites(raw_text: str) -> str:
        formatted_text = raw_text
        for pattern in [r'(?:https?://)?(?:www\.)?[\w-]+\.[\w.-]+[^\s]*']:
            formatted_text = re.sub(pattern, '', formatted_text)
        return ' '.join(formatted_text.split())

    @classmethod
    def remove_punctuation(cls, raw_text: str) -> str:
        doc = cls.nlp_object(raw_text)
        formatted_text = ' '.join(
            [token.text for token in doc if not token.is_punct],
        )
        return formatted_text

    @staticmethod
    def lower_text(raw_text: str) -> str:
        return raw_text.lower()

    @classmethod
    def remove_stopwords(cls, raw_text: str) -> str:
        doc = cls.nlp_object(raw_text)
        formatted_text = [token.text for token in doc if not token.is_stop]
        return ' '.join(formatted_text)

    @classmethod
    def lemmatization(cls, raw_text: str) -> str:
        doc = cls.nlp_object(raw_text)
        formatted_text = [token.lemma_ for token in doc]
        return ' '.join(formatted_text)

    @classmethod
    def replace_matches(
        cls,
        raw_text: str,
        patterns_dict: Dict[str, List[List[Dict[str, Any]]]],
    ) -> str:
        patterns_dict = cls.__create_patterns_dict(patterns_dict)
        matcher = Matcher(cls.nlp_object.vocab)
        doc = cls.nlp_object(raw_text)
        for key, value in patterns_dict.items():
            matcher.add(key, value)
        parsed_doc = doc.text
        for match_id, start, end in matcher(doc):
            string_id = cls.nlp_object.vocab.strings[match_id]
            span = doc[start:end]
            parsed_doc = parsed_doc.replace(span.text, string_id)

        return parsed_doc

    @classmethod
    def __create_patterns_dict(
        cls,
        patterns_data: Dict[str, List[List[Dict[str, Any]]]],
    ) -> Dict[str, List[List[Dict[str, Any]]]]:
        patterns_dict = {}

        for pattern_name, emojis in patterns_data.items():
            pattern_list = [[{'ORTH': emoji}] for emoji in emojis]
            patterns_dict[pattern_name] = pattern_list

        return patterns_dict
