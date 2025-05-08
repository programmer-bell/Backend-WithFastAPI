from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str
    SECRET_KEY: str = "your-secret"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 15

    '''
    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int
    STRIPE_SECRET_KEY: str
    PAYPAL_MODE: str
    PAYPAL_CLIENT_ID: str
    PAYPAL_CLIENT_SECRET: str  
    '''

    class Config:
        env_file = ".env"

settings = Settings()
