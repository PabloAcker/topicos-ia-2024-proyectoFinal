from typing import Union
from llama_index.core.tools import FunctionTool, ToolMetadata
from ai_assistant.prompts import contract_generation_tpl, contract_improvement_tpl, legal_question_tpl, \
    contract_rating_tpl
from ai_assistant.models import ContractResponse, LegalAnswer
from ai_assistant.utils import save_contract, extract_text_from_pdf
from ai_assistant.config import get_agent_settings
from llama_index.llms.openai import OpenAI

SETTINGS = get_agent_settings()
llm = OpenAI(model=SETTINGS.openai_model, api_key=SETTINGS.openai_api_key)

def generate_contract(contract_type: str, parties: dict, terms: dict) -> ContractResponse:
    prompt = contract_generation_tpl.format(contract_type=contract_type, parties=parties, terms=terms)
    contract_content = llm.generate(prompt)
    save_contract(contract_content, contract_type)
    return ContractResponse(status="OK", content=contract_content)

def improve_contract(contract_type:  str, contract_content: Union[str, bytes]) -> ContractResponse:
    if isinstance(contract_content, bytes):
        temp_pdf_path = "temp_contract.pdf"
        with open(temp_pdf_path, "wb") as pdf_file:
            pdf_file.write(contract_content)
        contract_content = extract_text_from_pdf(temp_pdf_path)
    prompt = contract_improvement_tpl.format(contract_type=contract_type, contract_content=contract_content)
    improved_content = llm.generate(prompt)
    save_contract(improved_content, contract_type, improved=True)
    return ContractResponse(status="OK", content=improved_content)

def answer_legal_question(question: str) -> LegalAnswer:
    prompt = legal_question_tpl.format(question=question)
    answer = llm.generate(prompt)
    return LegalAnswer(status="OK", answer=answer)

def rate_contract(contract_content: str) -> LegalAnswer:
    if isinstance(contract_content, bytes):
        contract_content = extract_text_from_pdf(contract_content)
    prompt = contract_rating_tpl.format(contract_content=contract_content)
    rating_response = llm.generate(prompt)
    return LegalAnswer(status="OK", answer=rating_response)

generate_contract_tool = FunctionTool.from_defaults(fn=generate_contract, return_direct=False)
improve_contract_tool = FunctionTool.from_defaults(fn=improve_contract, return_direct=False)
answer_legal_question_tool = FunctionTool.from_defaults(fn=answer_legal_question, return_direct=True)
rate_contract_tool = FunctionTool.from_defaults(fn=rate_contract, return_direct=True)
