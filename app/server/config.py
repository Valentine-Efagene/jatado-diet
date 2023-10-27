
from pydantic_settings import BaseSettings, SettingsConfigDict
import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()


class Settings(BaseSettings):
    app_name: str = "Jatado Diet"
    admin_email: str = "efagenevalentine@gmail.com"
    pagination_limit: int = 15
    environment: str = str(os.getenv("ENV"))
    mongodb_dev_uri: str = str(os.getenv("MONGODB_DEV_URI"))
    mongodb_prod_uri: str = str(os.getenv("MONGODB_PROD_URI"))
    mongodb_test_uri: str = str(os.getenv("MONGODB_TEST_URI"))
    mongodb_dev_db_name: str = str(os.getenv("MONGODB_DEV_DB_NAME"))
    mongodb_prod_db_name: str = str(os.getenv("MONGODB_PROD_DB_NAME"))
    mongodb_test_db_name: str = str(os.getenv("MONGODB_TEST_DB_NAME"))


settings = Settings()
