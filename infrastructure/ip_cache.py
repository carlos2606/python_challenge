import datetime
from typing import Optional, Tuple

__cache = {}


def get_ip_info(ip: str):
    data = __cache.get(ip)
    if not data:
        return None
    return data


def set_ip_info(ip_info: dict):
    __cache.update(ip_info)
