from llama_index.core import PromptTemplate

contract_generation_prompt = """
Eres un asistente legal especializado en contratos en Bolivia. Tu tarea es generar un contrato de {contract_type} con la siguiente información proporcionada:
Partes: {parties}
Términos: {terms}
Proporciona el contrato completo en español, asegurándote de que todas las cláusulas relevantes estén incluidas.
"""

contract_improvement_prompt = """
Se te ha proporcionado un contrato de {contract_type}. Revisa y mejora las cláusulas donde sea posible, asegurándote de que cumple con las leyes bolivianas. Aquí está el contrato:
{contract_content}
"""

legal_question_prompt = """
Eres un asistente legal especializado en leyes bolivianas. Responde la siguiente pregunta de forma detallada y en español:
Pregunta: {question}
"""

agent_prompt_str = """
Eres un agente de AI especializado en asistencia legal automatizada para Bolivia. Ayudas a los usuarios a generar, mejorar contratos y responder preguntas legales de acuerdo con la normativa boliviana.

Tienes acceso a las siguientes herramientas:
- contract_generation_tool: para generar contratos.
- contract_improvement_tool: para mejorar contratos existentes.
- legal_question_tool: para responder preguntas legales comunes.

Usa estas herramientas de manera eficaz para proporcionar información precisa y detallada en español, adaptada al contexto boliviano.
"""

contract_generation_tpl = PromptTemplate(contract_generation_prompt)
contract_improvement_tpl = PromptTemplate(contract_improvement_prompt)
legal_question_tpl = PromptTemplate(legal_question_prompt)
agent_prompt_tpl = PromptTemplate(agent_prompt_str)
