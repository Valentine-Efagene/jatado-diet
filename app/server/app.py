from fastapi import FastAPI
from .country.country_controller import router as CountryRouter
from .state.state_controller import router as StateRouter
from .lga.lga_controller import router as LgaRouter

app = FastAPI()
app.include_router(CountryRouter, prefix='/countries', tags=['Country'])
app.include_router(StateRouter, prefix='/states', tags=['State'])
app.include_router(LgaRouter, prefix='/lgas', tags=['LGA'])


'''


@app.get('/', tags=['Root'])
async def read_root():
    return {
        "message": "Welcome to this fantastic app!"
    }
'''
