from functools import cache
from pydantic_settings import BaseSettings, SettingsConfigDict

class AgentSettings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env")

    openai_model: str = "gpt4o-mini"
    hf_embeddings_model: str = "intfloat/multilingual-e5-base"
    openai_api_key: str = "key"
    contract_storage_path: str = "contracts"

@cache
def get_agent_settings() -> AgentSettings:
    return AgentSettings()
