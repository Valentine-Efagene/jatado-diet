from fastapi import FastAPI
from .country.country_controller import router as CountryRouter
from .state.state_controller import router as StateRouter
from .user.user_controller import router as UserRouter
from .lga.lga_controller import router as LgaRouter
from .ethnicity.ethnicity_controller import router as EthnicityRouter
from .language.language_controller import router as LanguageRouter
from .macro_nutrient.macro_nutrient_controller import router as MacroNutrientRouter
from .micro_nutrient.micro_nutrient_controller import router as MicroNutrientRouter
from .auth.auth_controller import router as AuthRouter
from .config import settings
from .common.enums import Tag


def create_application() -> FastAPI:
    app = FastAPI()

    app.include_router(AuthRouter,
                       prefix='/token', tags=[Tag.AUTHENTICATION])
    app.include_router(UserRouter, prefix='/users', tags=[Tag.USER])
    app.include_router(CountryRouter, prefix='/countries', tags=[Tag.COUNTRY])
    app.include_router(StateRouter, prefix='/states', tags=[Tag.STATE])
    app.include_router(LgaRouter, prefix='/lgas', tags=[Tag.LGA])
    app.include_router(
        EthnicityRouter, prefix='/ethnicities', tags=[Tag.ETHNICITY])
    app.include_router(LanguageRouter, prefix='/languages',
                       tags=[Tag.LANGUAGE])
    app.include_router(MacroNutrientRouter,
                       prefix='/macro_nutrients', tags=[Tag.MACRO_NUTRIENT])
    app.include_router(MicroNutrientRouter,
                       prefix='/micro_nutrients', tags=[Tag.MICRO_NUTRIENT])

    @app.get('/', tags=[Tag.MISC])
    async def read_root():
        return {
            "message": "Welcome to this fantastic app!"
        }

    @app.get("/info", tags=[Tag.MISC])
    async def info():
        return {
            "app_name": settings.app_name,
            "admin_email": settings.admin_email,
            "mongodb_uri": settings.mongodb_dev_uri,
            "db_name": settings.mongodb_dev_db_name
        }

    return app


app = create_application()
