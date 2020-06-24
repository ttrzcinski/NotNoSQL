from unittest import TestCase

from backend.KeyValueReader import KeyValueReader


class TestKeyValueReader(TestCase):

    tested_kvr = None

    def setUp(self):
        self.tested_kvr = KeyValueReader('test_en.txt', '../tests')

    def test_exists_key(self):
        # Assure
        tested_key = 'TEST_1'

        # Act
        result = self.tested_kvr.exists_key(tested_key)

        # Assert
        self.assertTrue(result, 'Key' + tested_key + ' must be present in tested set.')

    def test_doesnt_exist_key(self):
        # Assure
        tested_key = 'TEST_1_not_existing'

        # Act
        result = self.tested_kvr.exists_key(tested_key)

        # Assert
        self.assertFalse(result, 'Key' + tested_key + ' cannot be present in tested set.')

    def test_value_of(self):
        # Assure
        tested_key = 'TEST_1'
        # TODO Remove that \N in the future
        tested_value = 'Something'

        # Act
        result = self.tested_kvr.value_of(tested_key)

        # Assert
        self.assertEqual(result, tested_value, 'Key ' + tested_key + ' must have value ' + tested_value + '.')

    def test_hasnt_value_of(self):
        # Assure
        tested_key = 'TEST_1_doesnt_have_that'

        # Act
        result = self.tested_kvr.value_of(tested_key)

        # Assert
        self.assertIsNone(result, 'Key ' + tested_key + ' doesnt\'t.')
