from typing import Optional, List

import fastapi
from fastapi import File, UploadFile, Body

from models.validation_error import ValidationError
from services import ip_service

router = fastapi.APIRouter()

@router.get('/api/GetRecord', status_code=200)
async def get_record(ip: str = Body(..., embed=True)):
    try:
        return await ip_service.get_record(ip)
    except ValidationError as ve:
        return fastapi.Response(content=ve.error_msg, status_code=ve.status_code)
    except Exception as x:
        return fastapi.Response(content=str(x), status_code=500)

    

@router.post('/api/CreateRecordsFromFile', status_code=201)
async def file_post(file: UploadFile = File(...)):
    file2store = await file.read()
    response = await ip_service.bulk_create(file2store)

    return {
        'ip_addresses': response,
        'count': len(response)
    }

@router.post('/api/CreateRecord', status_code=201)
async def post_record(ip: str = Body(..., embed=True)):
    response = await ip_service.create_new_record(ip)
    return {
        'Status': 'OK'
    }
