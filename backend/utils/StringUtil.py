import re


class StringUtil:
    """ Extracted methods to process strings. """

    @staticmethod
    def is_none(phrase) -> bool:
        """ Checks, if given phrase is empty. """
        return phrase is None or len(phrase.strip()) == 0

    @staticmethod
    def has_content(phrase: str) -> bool:
        """ Checks, if given phrase has content. """
        return not StringUtil.is_none(phrase)

    @staticmethod
    def nvl(phrase: str, replace_word: str) -> str:
        """ Replaces given phrase, if is empty. """
        return replace_word if StringUtil.is_none(phrase) else phrase

    @staticmethod
    def replace_case_insensitive(phrase: str, word: str, replace_word=None) -> str:
        """ Replaces case insensitive words in given phrase. """
        if replace_word is None:
            replace_word = ''
        return re.compile(re.escape(word.lower()), re.IGNORECASE).sub(replace_word, phrase)

    @staticmethod
    def replace_with_uppercase(phrase: str, word: str) -> str:
        """ Replaces case insensitive words in given phrase. """
        return re.compile(re.escape(word.lower()), re.IGNORECASE).sub(word.upper(), phrase)

    @staticmethod
    def replace_with_lowercase(phrase: str, word: str) -> str:
        """ Replaces case insensitive words in given phrase. """
        return re.compile(re.escape(word.lower()), re.IGNORECASE).sub(word.lower(), phrase)
