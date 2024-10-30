import os
from llama_index.core import (
    VectorStoreIndex,
    StorageContext,
    load_index_from_storage,
    SimpleDirectoryReader,
    PromptTemplate,
    Settings,
)
from llama_index.core.query_engine import RetrieverQueryEngine
from llama_index.llms.openai import OpenAI
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from ai_assistant.config import get_agent_settings
from ai_assistant.prompts import legal_question_tpl

SETTINGS = get_agent_settings()

# Configuración del modelo de lenguaje y modelo de embeddings
llm = OpenAI(model=SETTINGS.openai_model, api_key=SETTINGS.openai_api_key)
embed_model = HuggingFaceEmbedding(model_name=SETTINGS.hf_embeddings_model)
Settings.embed_model = embed_model
Settings.llm = llm

class LegalRAG:
    def __init__(
        self,
        store_path: str,
        data_dir: str | None = None,
        qa_prompt_tpl: PromptTemplate | None = None,
    ):
        self.store_path = store_path

        # Cargar o crear el índice
        if not os.path.exists(store_path) and data_dir is not None:
            self.index = self.ingest_data(store_path, data_dir)
        else:
            self.index = load_index_from_storage(
                StorageContext.from_defaults(persist_dir=store_path)
            )

        self.qa_prompt_tpl = qa_prompt_tpl or legal_question_tpl

    def ingest_data(self, store_path: str, data_dir: str) -> VectorStoreIndex:
        # Ingesta de documentos para crear el índice
        documents = SimpleDirectoryReader(data_dir).load_data()
        index = VectorStoreIndex.from_documents(documents, show_progress=True)
        index.storage_context.persist(persist_dir=store_path)
        return index

    def get_query_engine(self) -> RetrieverQueryEngine:
        # Obtener el motor de consulta con la plantilla de prompt de preguntas legales
        query_engine = self.index.as_query_engine()

        if self.qa_prompt_tpl is not None:
            query_engine.update_prompts(
                {"response_synthesizer:text_qa_template": self.qa_prompt_tpl}
            )

        return query_engine
