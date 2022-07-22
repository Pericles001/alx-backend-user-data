#!/usr/bin/env python3
"""
Personal data
"""


import os
import re
from typing import List


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    for f in fields:
        message = re.sub(
            rf"{f}=(.*?)\{separator}",
            f'{f}={redaction}{separator}',
            message
        )
    return message
