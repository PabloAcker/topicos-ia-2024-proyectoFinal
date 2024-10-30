from random import randint
from llama_index.core.tools import FunctionTool, ToolMetadata
from ai_assistant.prompts import contract_generation_tpl, contract_improvement_tpl, legal_question_tpl
from ai_assistant.models import ContractRequest, ContractResponse, LegalQuestion, LegalAnswer
from ai_assistant.utils import save_contract

# Función para generar contratos
def generate_contract(contract_type: str, parties: dict, terms: dict) -> ContractResponse:
    prompt = contract_generation_tpl.format(contract_type=contract_type, parties=parties, terms=terms)
    # Aquí iría la llamada al modelo de IA para completar el contrato
    contract_content = "Contenido del contrato generado aquí..."  # Simulación de respuesta
    save_contract(contract_content, contract_type)
    return ContractResponse(status="OK", content=contract_content)

# Función para mejorar contratos
def improve_contract(contract_type: str, contract_content: str) -> ContractResponse:
    prompt = contract_improvement_tpl.format(contract_type=contract_type, contract_content=contract_content)
    # Aquí iría la llamada al modelo de IA para mejorar el contrato
    improved_content = "Contrato mejorado aquí..."  # Simulación de respuesta
    save_contract(improved_content, contract_type, improved=True)
    return ContractResponse(status="OK", content=improved_content)

# Función para responder preguntas legales
def answer_legal_question(question: str) -> LegalAnswer:
    prompt = legal_question_tpl.format(question=question)
    # Simulación de respuesta
    answer = "Respuesta detallada sobre la pregunta legal..."  # Simulación de respuesta
    return LegalAnswer(status="OK", answer=answer)

# Register tools as FunctionTools
generate_contract_tool = FunctionTool.from_defaults(fn=generate_contract, return_direct=False)
improve_contract_tool = FunctionTool.from_defaults(fn=improve_contract, return_direct=False)
answer_legal_question_tool = FunctionTool.from_defaults(fn=answer_legal_question, return_direct=True)
