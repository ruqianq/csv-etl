import unittest

from models.tri_facility import TriFacility
from models.tri_reporting_form import TriReportingForm
from models.query_condition import ColumnCondition, QueryConditionByTable


class TestTriFacility(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.abc_facility = TriFacility(tri_facility_id='23323HNSNP381CK', facility_name='abc',
                                       street_address='3801 COOK BLVD', city_name='New York City',
                                       county_name='New York City', state_abbr='NY', zip_code='21029', region=3,
                                       fac_closed_ind=0, parent_co_name='CONCRETE PIPE & PRECAST LLC',)

        cls.abc_reporting_form = TriReportingForm(doc_ctrl_num=1000, active_status=1, tri_facility_id='23323HNSNP381CK',
                                                  tri_chem_id='4nyyd', report_year=2021, max_amount_of_chem='40',
                                                  cas_chem_name='Xylene (mixed isomers)')
        cls.query_condition_no_column_condition = QueryConditionByTable(table_name='tri_facility')
        cls.column_condition = ColumnCondition(column_name='state', column_value='VA')
        cls.query_condition_with_condition = QueryConditionByTable(table_name='tri_facility',
                                                                   column_conditions=[cls.column_condition])

    def test_create_tri_facility_class(self):
        self.assertEqual(self.abc_facility.tri_facility_id, '23323HNSNP381CK')

    def test_create_tri_reporting_form(self):
        self.assertEqual(self.abc_reporting_form.tri_facility_id, '23323HNSNP381CK')

    def test_create_query_condition_no_column_condition(self):
        self.assertEqual(self.query_condition_no_column_condition.table_name, 'tri_facility')

    def test_create_query_condition_with_condition(self):
        self.assertEqual(self.query_condition_with_condition.column_conditions[0], self.column_condition)

    def test_create_column_conditon_str(self):
        self.assertEqual(str(self.column_condition), '/state/=/VA')

    def test_create_query_condition_str_no_column_condition(self):
        self.assertEqual(str(self.query_condition_no_column_condition), '/tri_facility')

    def test_create_query_condition_str_with_column_condition(self):
        self.assertEqual(str(self.query_condition_with_condition), '/tri_facility/state/=/VA')

    def test_create_two_tables_query_condition(self):
        self.assertEqual(str(self.query_condition_no_column_condition) + str(self.query_condition_with_condition),
                         '/tri_facility/tri_facility/state/=/VA')


if __name__ == '__main__':
    unittest.main()
