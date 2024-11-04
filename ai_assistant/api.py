from fastapi import FastAPI
from ai_assistant.models import ContractRequest, ContractResponse, LegalQuestion, LegalAnswer
from ai_assistant.tools import generate_contract, improve_contract, answer_legal_question, rate_contract

app = FastAPI(title="Sistema de Asistencia Legal Automatizada")

@app.post("/generate_contract", response_model=ContractResponse)
def generate_contract_endpoint(request: ContractRequest):
    return generate_contract(request.contract_type, request.parties, request.terms)

@app.post("/improve_contract", response_model=ContractResponse)
def improve_contract_endpoint(contract_type: str, contract_content: str):
    return improve_contract(contract_type, contract_content)

@app.post("/legal_question", response_model=LegalAnswer)
def legal_question_endpoint(question: LegalQuestion):
    return answer_legal_question(question.question)

@app.post("/rate_contract", response_model=LegalAnswer)
def rate_contract_endpoint(contract_content: str):
    return rate_contract(contract_content)
