import unittest

from models.tri_facility import TriFacility


class TriFacilityTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.abc_facility = TriFacility(tri_facility_id='23323HNSNP381CK', facility_name='abc',
                                       street_address='3801 COOK BLVD', city_name='New York City',
                                       county_name='New York City', state_abbr='NY', zip_code=21029, region=3,
                                       fac_closed_ind=0, parent_co_name='CONCRETE PIPE & PRECAST LLC',
                                       epa_registry_id='110001888903')

    def test_create_tri_facility_class(self):
        self.assertEqual(self.abc_facility.tri_facility_id, '23323HNSNP381CK')


if __name__ == '__main__':
    unittest.main()
