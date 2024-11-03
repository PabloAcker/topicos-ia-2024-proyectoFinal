from llama_index.core.tools import FunctionTool, ToolMetadata
from ai_assistant.prompts import contract_generation_tpl, contract_improvement_tpl, legal_question_tpl
from ai_assistant.models import ContractResponse, LegalAnswer
from ai_assistant.utils import save_contract

def generate_contract(contract_type: str, parties: dict, terms: dict) -> ContractResponse:
    prompt = contract_generation_tpl.format(contract_type=contract_type, parties=parties, terms=terms)
    contract_content = "Contenido del contrato generado aquí..."
    save_contract(contract_content, contract_type)
    return ContractResponse(status="OK", content=contract_content)

def improve_contract(contract_type: str, contract_content: str) -> ContractResponse:
    prompt = contract_improvement_tpl.format(contract_type=contract_type, contract_content=contract_content)
    improved_content = "Contrato mejorado aquí..."
    save_contract(improved_content, contract_type, improved=True)
    return ContractResponse(status="OK", content=improved_content)

def answer_legal_question(question: str) -> LegalAnswer:
    prompt = legal_question_tpl.format(question=question)
    answer = "Respuesta detallada sobre la pregunta legal..."
    return LegalAnswer(status="OK", answer=answer)

generate_contract_tool = FunctionTool.from_defaults(fn=generate_contract, return_direct=False)
improve_contract_tool = FunctionTool.from_defaults(fn=improve_contract, return_direct=False)
answer_legal_question_tool = FunctionTool.from_defaults(fn=answer_legal_question, return_direct=True)
