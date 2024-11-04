from llama_index.core.tools import FunctionTool, ToolMetadata
from ai_assistant.prompts import contract_generation_tpl, contract_improvement_tpl, legal_question_tpl, \
    contract_rating_tpl
from ai_assistant.models import ContractResponse, LegalAnswer
from ai_assistant.utils import save_contract
from ai_assistant.config import get_agent_settings
from llama_index.llms.openai import OpenAI

SETTINGS = get_agent_settings()
llm = OpenAI(model=SETTINGS.openai_model, api_key=SETTINGS.openai_api_key)

def generate_contract(contract_type: str, parties: dict, terms: dict) -> ContractResponse:
    prompt = contract_generation_tpl.format(contract_type=contract_type, parties=parties, terms=terms)
    contract_content = llm.generate(prompt)
    save_contract(contract_content, contract_type)
    return ContractResponse(status="OK", content=contract_content)

def improve_contract(contract_type: str, contract_content: str) -> ContractResponse:
    prompt = contract_improvement_tpl.format(contract_type=contract_type, contract_content=contract_content)
    improved_content = llm.generate(prompt)
    save_contract(improved_content, contract_type, improved=True)
    return ContractResponse(status="OK", content=improved_content)

def answer_legal_question(question: str) -> LegalAnswer:
    prompt = legal_question_tpl.format(question=question)
    answer = llm.generate(prompt)
    return LegalAnswer(status="OK", answer=answer)

def rate_contract(contract_content: str) -> LegalAnswer:
    """
    Califica un contrato en una escala del 1 al 5 en términos de claridad, completitud y cumplimiento con las leyes bolivianas.
    """
    # Formatear el prompt con el contenido del contrato
    prompt = contract_rating_tpl.format(contract_content=contract_content)
    # Llamada al modelo LLM para obtener la calificación del contrato
    rating_response = llm.generate(prompt)
    return LegalAnswer(status="OK", answer=rating_response)

generate_contract_tool = FunctionTool.from_defaults(fn=generate_contract, return_direct=False)
improve_contract_tool = FunctionTool.from_defaults(fn=improve_contract, return_direct=False)
answer_legal_question_tool = FunctionTool.from_defaults(fn=answer_legal_question, return_direct=True)
rate_contract_tool = FunctionTool.from_defaults(fn=rate_contract, return_direct=True)
