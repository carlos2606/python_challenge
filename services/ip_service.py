import re
from time import sleep
from typing import List, Tuple

from infrastructure import ip_cache
from services import geo_ip, rdap


async def get_record(ip: str):
    return ip_cache.get_ip_info(ip)

async def parse(file: str) -> List[dict]:
    list_of_ips = re.findall(r'[0-9]+(?:\.[0-9]+){3}', file, re.MULTILINE)
    return list_of_ips

async def bulk_create(file: bytes):
    list_of_ips = await parse(file.decode())
    response = []
    new_ips = []
    for ip in list_of_ips:
        new_record = await create_new_record(ip)
        response.append(new_record)
        # sleep(4)
    return response

async def create_new_record(ip: str) -> dict:
    if ip_cache.get_ip_info(ip):
        return ip_cache.get_ip_info(ip)
    record = {}
    geo_info = await geo_ip.get_geo_ip_info(ip)
    rdap_info = await rdap.get_rdap_ip_info(ip)
    record[ip] = []
    record[ip].append(geo_info)
    record[ip].append(rdap_info)
    ip_cache.set_ip_info(record)
    return record
            
