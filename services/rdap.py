from typing import Optional, Tuple
import httpx
from httpx import Response

from models.validation_error import ValidationError

api_key: Optional[str] = None

async def get_rdap_ip_info(ip: str) -> dict:
    url = f'https://www.rdap.net/ip/{ip}'

    async with httpx.AsyncClient() as client:
            resp: Response = await client.get(url)
    if resp.status_code == 200:
        data = resp.json()

        return data
    return {}