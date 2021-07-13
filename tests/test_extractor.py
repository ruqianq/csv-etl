import unittest
from epa_tri_data_extractor import fetch_epa_tri_table


class ExtractorTestCase(unittest.TestCase):

    def test_fetch_epa_tri_table(self):
        self.assertEqual(fetch_epa_tri_table('tri_reporting_form'), [])


if __name__ == '__main__':
    unittest.main()
