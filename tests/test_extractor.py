import unittest
from util import construct_query_str
from models.query_condition import QueryConditionByTable, ColumnCondition


class TestExtractor(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.query_condition_no_column_condition = QueryConditionByTable(table_name='tri_facility')
        cls.column_condition = ColumnCondition(column_name='state', column_value='VA')
        cls.query_condition_with_condition = QueryConditionByTable(table_name='tri_facility',
                                                                   column_conditions=[cls.column_condition])

    def test_construct_query_str_no_rows(self):
        self.assertEqual(construct_query_str([self.query_condition_with_condition,
                                              self.query_condition_no_column_condition]),
                         '/tri_facility/state/=/VA/tri_facility/JSON')

    def test_construct_query_str_with_rows(self):
        self.assertEqual(construct_query_str([self.query_condition_with_condition,
                                              self.query_condition_no_column_condition], rows='20:100'),
                         '/tri_facility/state/=/VA/tri_facility/JSON/rows/20:100')


if __name__ == '__main__':
    unittest.main()
