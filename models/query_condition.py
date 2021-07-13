from typing import List


class ColumnCondition:
    def __init__(self, column_name: str, operation: str = "=", column_value: str = None):
        self.column_name = column_name
        self.operation = operation
        self.column_value = column_value



class QueryCondition:
    def __init__(self, table_name: str, column_condition: List[ColumnCondition] = None):
        self.table_name = table_name
        self.column_condition = column_condition

