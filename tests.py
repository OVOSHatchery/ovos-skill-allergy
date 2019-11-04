from allergyrequest import convert_allergy_index_to_level
import unittest

from zipcoderequest import get_zip_from_ip


class AllergyLevelTest(unittest.TestCase):
    def test_convert_allergy_index_to_level(self):
        self.assertEqual(convert_allergy_index_to_level(1), "low")

    def test_get_zip_from_ip(self):
        self.assertEqual(get_zip_from_ip('196.52.2.47'), '10123')


