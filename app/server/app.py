from fastapi import FastAPI
from .country.country_controller import router as CountryRouter
from .state.state_controller import router as StateRouter
from .lga.lga_controller import router as LgaRouter
from .ethnicity.ethnicity_controller import router as EthnicityRouter
from .config import settings

app = FastAPI()

app.include_router(CountryRouter, prefix='/countries', tags=['Country'])
app.include_router(StateRouter, prefix='/states', tags=['State'])
app.include_router(LgaRouter, prefix='/lgas', tags=['LGA'])
app.include_router(EthnicityRouter, prefix='/ethnicity', tags=['Ethnicity'])


@app.get('/', tags=['Root'])
async def read_root():
    return {
        "message": "Welcome to this fantastic app!"
    }


@app.get("/info")
async def info():
    return {
        "app_name": settings.app_name,
        "admin_email": settings.admin_email,
        "mongodb_uri": settings.mongodb_dev_uri,
        "db_name": settings.mongodb_dev_db_name
    }
