from llama_index.core import PromptTemplate
from llama_index.core.agent import ReActAgent
from ai_assistant.tools import (
    generate_contract_tool,
    improve_contract_tool,
    answer_legal_question_tool,
)
from ai_assistant.prompts import agent_prompt_tpl

class LegalAgent:
    def __init__(self, system_prompt: PromptTemplate | None = None):
        self.agent = ReActAgent.from_tools(
            [
                generate_contract_tool,
                improve_contract_tool,
                answer_legal_question_tool,
            ],
            verbose=True,
        )
        if system_prompt is not None:
            self.agent.update_prompts({"agent_worker:system_prompt": system_prompt})
        else:
            self.agent.update_prompts({"agent_worker:system_prompt": agent_prompt_tpl})

    def get_agent(self) -> ReActAgent:
        return self.agent
