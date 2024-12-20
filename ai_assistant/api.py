from fastapi import FastAPI, File, UploadFile
from typing import Union
from ai_assistant.models import ContractRequest, ContractResponse, LegalQuestion, LegalAnswer
from ai_assistant.tools import generate_contract, improve_contract, answer_legal_question, rate_contract

app = FastAPI(title="Sistema de Asistencia Legal Automatizada")

@app.post("/generate_contract", response_model=ContractResponse)
def generate_contract_endpoint(request: ContractRequest):
    return generate_contract(request.contract_type, request.parties, request.terms)

@app.post("/improve_contract", response_model=ContractResponse)
async def improve_contract_endpoint(contract_type: str, contract_content: Union[str, None] = None,
                                    file: UploadFile = File(None)):
    content = await file.read() if file else contract_content
    return improve_contract(contract_type, content)

@app.post("/legal_question", response_model=LegalAnswer)
def legal_question_endpoint(question: LegalQuestion):
    return answer_legal_question(question.question)

@app.post("/rate_contract", response_model=LegalAnswer)
async def rate_contract_endpoint(file: UploadFile = File(None), contract_content: Union[str, None] = None):
    content = await file.read() if file else contract_content
    if content is None:
        return {"status": "Error", "answer": "No se proporcionó ningún contenido para calificar."}
    return rate_contract(content)
