from pydanticSettings import BaseSettings,SettingsConfigDict
class Settings(BaseSettings):
    #app
    APP_NAME: str ="AI Travel Itinerary Builder",
    APP_VERSION: str = "1.0.0",
    DEBUG: bool = True
    #database
    DATABASE_URL: str
    #AI
    GEMINI_API_KEY: str
    #AI Settings
    GEMINI_MODEL: str = "gemini-2.5-flash"
    MAX_OUTPUT_TOKENS: int = 2048
    TEMPERATURE: float = 0.7
    #Environmental Settings
    model_config(SettingsConfigDict)
    {
        env_file: ".env",
        env_file_encoding: "utf-8",
        extra: "ignore"
    }
    settings=Settings()