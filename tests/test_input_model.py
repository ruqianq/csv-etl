import unittest

from models.tri_facility import TriFacility
from models.tri_reporting_form import TriReportingForm


class TriFacilityTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.abc_facility = TriFacility(tri_facility_id='23323HNSNP381CK', facility_name='abc',
                                       street_address='3801 COOK BLVD', city_name='New York City',
                                       county_name='New York City', state_abbr='NY', zip_code=21029, region=3,
                                       fac_closed_ind=0, parent_co_name='CONCRETE PIPE & PRECAST LLC',
                                       epa_registry_id='110001888903')

        cls.abc_reporting_form = TriReportingForm(doc_ctrl_num=1000, active_status=1, tri_facility_id='23323HNSNP381CK',
                                                  tri_chem_id='4nyyd', report_year=2021, max_amount_of_chem=40,
                                                  cas_chem_name='Xylene (mixed isomers)')

    def test_create_tri_facility_class(self):
        self.assertEqual(self.abc_facility.tri_facility_id, '23323HNSNP381CK')

    def test_create_tri_reporting_form(self):
        self.assertEqual(self.abc_reporting_form.tri_facility_id, '23323HNSNP381CK')


if __name__ == '__main__':
    unittest.main()
