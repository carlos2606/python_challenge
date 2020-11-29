from typing import Optional, Tuple
import httpx
from httpx import Response

from models.validation_error import ValidationError

api_key: Optional[str] = None

async def get_geo_ip_info(ip: str) -> dict:
    url = f'http://ip-api.com/json/{ip}'

    async with httpx.AsyncClient() as client:
        resp: Response = await client.get(url)
        if resp.status_code != 200:
            raise ValidationError(resp.text, status_code=resp.status_code)
    
    data = resp.json()

    return data
