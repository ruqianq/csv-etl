import unittest
from models.output import ToxicAirPollutionByCompany


class TestOutputModel(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.abc_inc = ToxicAirPollutionByCompany(tri_facility_id='10001', company_names='ABC Inc.',
                                                 toxic_air_pollution=120000, street_address='123 Sam str',
                                                 city_name='New York City', county_name='NYC', state_abbr='NY',
                                                 zip_code='12345', cas_chem_names=['Air'])

    def test_create_toxic_air_pollution_by_company(self):
        self.assertEqual(self.abc_inc.toxic_air_pollution, 120000)


if __name__ == '__main__':
    unittest.main()
