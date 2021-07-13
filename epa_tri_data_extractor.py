import logging
import requests
from typing import List

from models.query_condition import QueryConditionByTable

logger = logging.getLogger(__name__)


def construct_query_str(query_conditions: [QueryConditionByTable]) -> str:
    query_str = ''
    if query_conditions:
        for q in query_conditions:
            query_str += str(q)
    return query_str


def fetch_epa_tri_table(query_str: str, output_format: str = 'JSON') -> List:
    output_table = []
    return output_table

