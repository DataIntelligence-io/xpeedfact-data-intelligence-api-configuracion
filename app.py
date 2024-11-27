from fastapi import FastAPI
from fastapi.responses import JSONResponse 
from Services.main_service import main as main_service
import json
from fastapi.security.api_key import APIKeyHeader
from fastapi import Security, HTTPException, status
from properties import API_KEY,API_KEY_NAME


app = FastAPI()

api_key_header = APIKeyHeader(name=API_KEY_NAME, auto_error=False)
async def get_api_key(api_key_header: str = Security(api_key_header)):
    if api_key_header == API_KEY:
        return api_key_header
    else:
        raise HTTPException(
            status_code=status.HTTP_401, detail="Could not validate credentials"
        )


@app.get("/test")
async def root(api_key: str = Security(get_api_key)):
    return {"data": "ok"}


@app.get("/")
async def root( key_configuracion : str , api_key: str = Security(get_api_key)):
    data = main_service(key_configuracion)
    print( "data: ", data)
    return JSONResponse(content=json.loads(data), media_type="application/json")