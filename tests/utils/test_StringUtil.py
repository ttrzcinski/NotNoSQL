from unittest import TestCase

from backend.utils.StringUtil import StringUtil


class TestStringUtil(TestCase):

    def test_is_none_with_none(self):
        # Assure
        tested_value = None

        # Act
        result = StringUtil.is_none(tested_value)

        # Assert
        self.assertTrue(result)

    def test_is_none_with_empty(self):
        # Assure
        tested_value = ''

        # Act
        result = StringUtil.is_none(tested_value)

        # Assert
        self.assertTrue(result)

    def test_is_none_with_whitespaces(self):
        # Assure
        tested_value = '     '

        # Act
        result = StringUtil.is_none(tested_value)

        # Assert
        self.assertTrue(result)

    def test_is_none_with_something(self):
        # Assure
        tested_value = 'something'

        # Act
        result = StringUtil.is_none(tested_value)

        # Assert
        self.assertFalse(result)

    def test_has_content_with_none(self):
        # Assure
        tested_value = None

        # Act
        result = StringUtil.has_content(tested_value)

        # Assert
        self.assertFalse(result)

    def test_has_content_with_empty(self):
        # Assure
        tested_value = ''

        # Act
        result = StringUtil.has_content(tested_value)

        # Assert
        self.assertFalse(result)

    def test_has_content_with_whitespaces(self):
        # Assure
        tested_value = '     '

        # Act
        result = StringUtil.has_content(tested_value)

        # Assert
        self.assertFalse(result)

    def test_has_content_with_something(self):
        # Assure
        tested_value = 'something'

        # Act
        result = StringUtil.has_content(tested_value)

        # Assert
        self.assertTrue(result)

    def test_nvl_with_none(self):
        # Assure
        tested_value = None
        tested_replacer = 'another'

        # Act
        result = StringUtil.nvl(tested_value, tested_replacer)

        # Assert
        self.assertEqual(tested_replacer, result)

    def test_nvl_with_empty(self):
        # Assure
        tested_value = ''
        tested_replacer = 'another'

        # Act
        result = StringUtil.nvl(tested_value, tested_replacer)

        # Assert
        self.assertEqual(tested_replacer, result)

    def test_nvl_with_whitespaces(self):
        # Assure
        tested_value = '     '
        tested_replacer = 'another'

        # Act
        result = StringUtil.nvl(tested_value, tested_replacer)

        # Assert
        self.assertEqual(tested_replacer, result)

    def test_nvl_with_something(self):
        # Assure
        tested_value = 'something'
        tested_replacer = 'another'

        # Act
        result = StringUtil.nvl(tested_value, tested_replacer)

        # Assert
        self.assertNotEqual(tested_replacer, result)

    def test_replace_case_insensitive_with_lowercase(self):
        # Assure
        tested_value = 'This code is funny.'
        tested_to_replace = 'code'
        tested_replacer = 'JOKE'

        # Act
        result = StringUtil.replace_case_insensitive(tested_value, tested_to_replace, tested_replacer)

        # Assert
        self.assertTrue(tested_replacer in result)

    def test_replace_case_insensitive_with_mixed(self):
        # Assure
        tested_value = 'This coDe is funny.'
        tested_to_replace = 'coDe'
        tested_replacer = 'JOKE'

        # Act
        result = StringUtil.replace_case_insensitive(tested_value, tested_to_replace, tested_replacer)

        # Assert
        self.assertTrue(tested_replacer in result)

    def test_replace_case_insensitive_with_uppercase(self):
        # Assure
        tested_value = 'This CODE is funny.'
        tested_to_replace = 'CODE'
        tested_replacer = 'JOKE'

        # Act
        result = StringUtil.replace_case_insensitive(tested_value, tested_to_replace, tested_replacer)

        # Assert
        self.assertTrue(tested_replacer in result)

    def test_replace_case_insensitive_with_other(self):
        # Assure
        tested_value = 'This cOdE is funny.'
        tested_to_replace = 'CoDe'
        tested_replacer = 'JOKE'

        # Act
        result = StringUtil.replace_case_insensitive(tested_value, tested_to_replace, tested_replacer)

        # Assert
        self.assertTrue(tested_replacer in result)

    def test_replace_case_insensitive_with_none(self):
        # Assure
        tested_value = 'This cOdE is funny.'
        tested_to_replace = 'CoDe'
        tested_replacer = None
        expected = 'This  is funny.'

        # Act
        result = StringUtil.replace_case_insensitive(tested_value, tested_to_replace, tested_replacer)

        # Assert
        self.assertEqual(expected, result)

    def test_replace_case_insensitive_with_no_replacer(self):
        # Assure
        tested_value = 'This cOdE is funny.'
        tested_to_replace = 'CoDe'
        expected = 'This  is funny.'

        # Act
        result = StringUtil.replace_case_insensitive(tested_value, tested_to_replace)

        # Assert
        self.assertEqual(expected, result)

    def test_replace_with_uppercase_with_lowercase(self):
        # Assure
        tested_value = 'This code is funny.'
        tested_to_replace = 'code'
        expected = 'This CODE is funny.'

        # Act
        result = StringUtil.replace_with_uppercase(tested_value, tested_to_replace)

        # Assert
        self.assertEqual(expected, result)

    def test_replace_with_uppercase_with_mixed(self):
        # Assure
        tested_value = 'This coDe is funny.'
        tested_to_replace = 'coDe'
        expected = 'This CODE is funny.'

        # Act
        result = StringUtil.replace_with_uppercase(tested_value, tested_to_replace)

        # Assert
        self.assertEqual(expected, result)

    def test_replace_with_uppercase_with_upper(self):
        # Assure
        tested_value = 'This CODE is funny.'
        tested_to_replace = 'CODE'
        expected = 'This CODE is funny.'

        # Act
        result = StringUtil.replace_with_uppercase(tested_value, tested_to_replace)

        # Assert
        self.assertEqual(expected, result)

    def test_replace_with_uppercase_with_other(self):
        # Assure
        tested_value = 'This cOdE is funny.'
        tested_to_replace = 'CoDe'
        expected = 'This CODE is funny.'

        # Act
        result = StringUtil.replace_with_uppercase(tested_value, tested_to_replace)

        # Assert
        self.assertEqual(expected, result)

    def test_replace_with_lowercase_with_lowercase(self):
        # Assure
        tested_value = 'This code is funny.'
        tested_to_replace = 'code'
        expected = 'This code is funny.'

        # Act
        result = StringUtil.replace_with_lowercase(tested_value, tested_to_replace)

        # Assert
        self.assertEqual(expected, result)

    def test_replace_with_lowercase_with_mixed(self):
        # Assure
        tested_value = 'This cOde is funny.'
        tested_to_replace = 'code'
        expected = 'This code is funny.'

        # Act
        result = StringUtil.replace_with_lowercase(tested_value, tested_to_replace)

        # Assert
        self.assertEqual(expected, result)

    def test_replace_with_lowercase_with_uppercase(self):
        # Assure
        tested_value = 'This CODE is funny.'
        tested_to_replace = 'code'
        expected = 'This code is funny.'

        # Act
        result = StringUtil.replace_with_lowercase(tested_value, tested_to_replace)

        # Assert
        self.assertEqual(expected, result)

    def test_replace_with_lowercase_with_other(self):
        # Assure
        tested_value = 'This cOdE is funny.'
        tested_to_replace = 'CoDe'
        expected = 'This code is funny.'

        # Act
        result = StringUtil.replace_with_lowercase(tested_value, tested_to_replace)

        # Assert
        self.assertEqual(expected, result)