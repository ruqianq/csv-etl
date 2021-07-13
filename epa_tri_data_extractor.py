import logging
import requests
from typing import List


def fetch_epa_tri_table(table_name: str, query_condition: List = None, start_row: int = 0,
                        end_row: int = 10000, output_format: str = 'JSON') -> List:
    output_table = []
    return output_table

