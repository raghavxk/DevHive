from pydantic import BaseSettings


class Settings(BaseSettings):
    secret_key : str
    db_name: str
    db_user: str
    db_password : str
    db_host : str
    debug_mode : bool

    class Config:
        env_file = ".env"

settings = Settings()


