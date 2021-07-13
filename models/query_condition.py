from typing import List


class ColumnCondition:
    def __init__(self, column_name: str, operation: str = "=", column_value: str = None):
        self.column_name = column_name
        self.operation = operation
        self.column_value = column_value

    def __str__(self):
        return f'/{self.column_name}/{self.operation}/{self.column_value}'


class QueryCondition:
    def __init__(self, table_name: str, column_conditions: List[ColumnCondition] = None):
        self.table_name = table_name
        self.column_conditions = column_conditions

    def __str__(self):
        if self.column_conditions:
            column_str = ""
            for c in self.column_conditions:
                column_str += str(c)
            return f'/{self.table_name}{column_str}'
        return f'/{self.table_name}'

