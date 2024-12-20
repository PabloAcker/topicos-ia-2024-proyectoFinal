import os
import fitz
from datetime import datetime
from ai_assistant.config import get_agent_settings

SETTINGS = get_agent_settings()

def save_contract(content: str, contract_type: str, improved: bool = False):
    folder = SETTINGS.contract_storage_path
    os.makedirs(folder, exist_ok=True)
    filename = f"{contract_type}_{'improved' if improved else 'generated'}_{datetime.now().isoformat()}.txt"
    path = os.path.join(folder, filename)
    with open(path, "w") as file:
        file.write(content)
    print(f"Contrato guardado en {path}")

def extract_text_from_pdf(pdf_path: str) -> str:
    text = ""
    with fitz.open(pdf_path) as pdf:
        for page in pdf:
            text += page.get_text()
    return text
