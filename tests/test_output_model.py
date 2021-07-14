import unittest
from models.toxic_air_pollution_by_company_dto import ToxicAirPollutionByCompany


class TestOutputModel(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.abc_inc = ToxicAirPollutionByCompany(id=10001, report_date='07122021', company_names='ABC Inc.',
                                                 toxic_air_pollution=120000, unit='ppm',
                                                 description='Lorem Ipsum is simply dummy text of the')

    def test_create_toxic_air_pollution_by_company(self):
        self.assertEqual(self.abc_inc.toxic_air_pollution, 120000)


if __name__ == '__main__':
    unittest.main()
