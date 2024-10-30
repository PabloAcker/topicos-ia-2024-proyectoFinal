from llama_index.core import PromptTemplate
from llama_index.core.agent import ReActAgent
from ai_assistant.tools import (
    generate_contract_tool,  # Cambiado a match con tools.py
    improve_contract_tool,   # Cambiado a match con tools.py
    answer_legal_question_tool,  # Cambiado a match con tools.py
)
from ai_assistant.prompts import agent_prompt_tpl

class LegalAgent:
    def __init__(self, system_prompt: PromptTemplate | None = None):
        # Configuración del agente utilizando las herramientas de generación y mejora de contratos, y respuestas legales
        self.agent = ReActAgent.from_tools(
            [
                generate_contract_tool,
                improve_contract_tool,
                answer_legal_question_tool,
            ],
            verbose=True,
        )
        # Actualización del prompt del sistema si se proporciona uno
        if system_prompt is not None:
            self.agent.update_prompts({"agent_worker:system_prompt": system_prompt})
        else:
            self.agent.update_prompts({"agent_worker:system_prompt": agent_prompt_tpl})

    def get_agent(self) -> ReActAgent:
        # Devuelve el agente configurado para interactuar en el sistema de asistencia legal
        return self.agent
