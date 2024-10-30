from fastapi import FastAPI, Depends
from ai_assistant.models import ContractRequest, ContractResponse, LegalQuestion, LegalAnswer
from ai_assistant.tools import generate_contract, improve_contract, answer_legal_question

app = FastAPI(title="Sistema de Asistencia Legal Automatizada")

# Generación de contrato
@app.post("/generate_contract", response_model=ContractResponse)
def generate_contract_endpoint(request: ContractRequest):
    return generate_contract(request.contract_type, request.parties, request.terms)

# Mejora de contrato
@app.post("/improve_contract", response_model=ContractResponse)
def improve_contract_endpoint(contract_type: str, contract_content: str):
    return improve_contract(contract_type, contract_content)

# Respuestas automáticas a preguntas legales
@app.post("/legal_question", response_model=LegalAnswer)
def legal_question_endpoint(question: LegalQuestion):
    return answer_legal_question(question.question)
