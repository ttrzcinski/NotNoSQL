from unittest import TestCase

from backend.not_no_sql.nns_converters import nns_converters


class Testnns_converters(TestCase):
    def test_is_valid_json_with_valid_json(self):
        # Assure
        tested_value = '{"code": "valid"}'

        # Act
        result = nns_converters.is_valid_json(tested_value)

        # Assert
        self.assertTrue(result)

    def test_is_valid_json_with_invalid_json(self):
        # Assure
        tested_value = '{"code": valid"}'

        # Act
        result = nns_converters.is_valid_json(tested_value)

        # Assert
        self.assertFalse(result)

    def test_is_valid_json_with_empty_json(self):
        # Assure
        tested_value = '{}'

        # Act
        result = nns_converters.is_valid_json(tested_value)

        # Assert
        self.assertFalse(result)

    def test_is_valid_json_with_empty(self):
        # Assure
        tested_value = '    '

        # Act
        result = nns_converters.is_valid_json(tested_value)

        # Assert
        self.assertFalse(result)

    def test_is_valid_json_with_none(self):
        # Assure
        tested_value = None

        # Act
        result = nns_converters.is_valid_json(tested_value)

        # Assert
        self.assertFalse(result)

    def test_conv_json_to_where_with_many_strings(self):
        # Assure
        tested_value = '{"col_1": "val_1", "col_2": "val_2"}'
        expected = 'col_1 LIKE \'val_1\' AND col_2 LIKE \'val_2\''

        # Act
        result = nns_converters.conv_json_to_where(tested_value)

        # Assert
        self.assertEqual(expected, result)

    def test_conv_json_to_where_with_many_ints(self):
        # Assure
        tested_value = '{"col_1": 1, "col_2": 2}'
        expected = 'col_1 = 1 AND col_2 = 2'

        # Act
        result = nns_converters.conv_json_to_where(tested_value)

        # Assert
        self.assertEqual(expected, result)

    def test_conv_json_to_where_with_many_mixed_types(self):
        # Assure
        tested_value = '{"col_1": 1, "col_2": "val_2"}'
        expected = 'col_1 = 1 AND col_2 LIKE \'val_2\''

        # Act
        result = nns_converters.conv_json_to_where(tested_value)

        # Assert
        self.assertEqual(expected, result)

    def test_conv_json_to_where_with_empty(self):
        # Assure
        tested_value = ''
        expected = '1 = 1'

        # Act
        result = nns_converters.conv_json_to_where(tested_value)

        # Assert
        self.assertEqual(expected, result)

    def test_conv_json_to_where_with_none(self):
        # Assure
        tested_value = None
        expected = None

        # Act
        result = nns_converters.conv_json_to_where(tested_value)

        # Assert
        self.assertEqual(expected, result)
