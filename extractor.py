import logging
import requests
from typing import List

from models.query_condition import QueryConditionByTable

logger = logging.getLogger(__name__)


def construct_query_str(query_conditions: [QueryConditionByTable], output_format: str = 'JSON',
                        rows: str = None) -> str:
    query_str = ''
    if query_conditions:
        for q in query_conditions:
            query_str += str(q)
    query_str = query_str
    logger.info(f'Query data based on {query_str}/{output_format}')
    if rows:
        return query_str + f'/{output_format}' + f'/rows/{rows}'
    return query_str + f'/{output_format}'


def fetch_epa_tri_table(query_str: str, start_row: int = 0, end_row: int = 10000) -> List:

    output_table = []
    return output_table
