import logging
import requests
from typing import List

logger = logging.getLogger(__name__)


def construct_query_condition() -> str:
    return ''


def fetch_epa_tri_table(query_condition: List = None, start_row: int = 0,
                        end_row: int = 10000, output_format: str = 'JSON') -> List:

    output_table = []
    return output_table

