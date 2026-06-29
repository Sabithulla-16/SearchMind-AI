from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    PROJECT_NAME: str
    VERSION: str

    HOST: str
    PORT: int

    DEBUG: bool

    GROQ_API_KEY: str
    GROQ_MODEL: str

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )


settings = Settings()