from pydantic import BaseModel, Field
from datetime import datetime
from enum import Enum
class ContractType(str, Enum):
    compra_venta = "COMPRAVENTA"
    arrendamiento = "ARRENDAMIENTO"
    trabajo = "TRABAJO"
    servicios = "SERVICIOS"
    sociedad = "SOCIEDAD"
    prestamo = "PRESTAMO"
    comodato = "COMODATO"
    donacion = "DONACION"
    mandato = "MANDATO"
    confidencialidad = "CONFIDENCIALIDAD"

class ContractRequest(BaseModel):
    contract_type: ContractType
    parties: dict  # Información sobre las partes involucradas
    terms: dict    # Términos específicos del contrato

class ContractResponse(BaseModel):
    status: str
    content: str

class LegalQuestion(BaseModel):
    question: str

class LegalAnswer(BaseModel):
    status: str
    answer: str
    timestamp: datetime = Field(default_factory=datetime.now)
