import gradio as gr
from ai_assistant.agent import LegalAgent
from ai_assistant.prompts import agent_prompt_tpl
from ai_assistant.utils import extract_text_from_pdf

# Inicializa el agente de asistencia legal
agent = LegalAgent(agent_prompt_tpl).get_agent()

def agent_response_text(message, history=None):
    """Procesa solo el texto del mensaje en el chat general."""
    return agent.chat(message).response

def agent_response_file_for_improvement(file):
    """Procesa el archivo PDF subido para mejora."""
    if file is not None:
        pdf_content = extract_text_from_pdf(file.name)
        response = agent.chat(f"Mejora el siguiente contrato:\n{pdf_content}").response
        return response
    return "No se ha proporcionado ningún archivo."

def agent_response_file_for_rating(file):
    """Procesa el archivo PDF subido para calificación."""
    if file is not None:
        pdf_content = extract_text_from_pdf(file.name)
        response = agent.chat(f"Califica el siguiente contrato:\n{pdf_content}").response
        return response
    return "No se ha proporcionado ningún archivo."

# Configuración de la interfaz de Gradio
with gr.Blocks(css="""
    .container { max-width: 750px; margin: auto; padding: 20px; }
    .title { text-align: center; font-size: 1.5em; color: #333; margin-bottom: 20px; }
    .file-section { margin-top: 20px; padding: 15px; background-color: #f7f7f7; border-radius: 8px; }
    .file-section h3 { color: #444; }
""") as demo:
    gr.Markdown("<div class='title'>💼 Chatbot de Asistencia Legal Automatizada</div>")

    # Chat general de asistencia legal para mensajes de texto
    chatbot = gr.ChatInterface(fn=agent_response_text, type="messages")

    # Sección para mejora de contrato en PDF
    with gr.Column(elem_classes="file-section"):
        gr.Markdown("### Subir contrato en PDF para mejora")
        improve_file_input = gr.File(label="Subir contrato en PDF para mejora")
        improve_output = gr.Textbox(label="Respuesta de mejora del asistente")

        improve_file_input.change(agent_response_file_for_improvement, inputs=improve_file_input, outputs=improve_output)

    # Sección para calificación de contrato en PDF
    with gr.Column(elem_classes="file-section"):
        gr.Markdown("### Subir contrato en PDF para calificación")
        rate_file_input = gr.File(label="Subir contrato en PDF para calificación")
        rate_output = gr.Textbox(label="Calificación del contrato")

        rate_file_input.change(agent_response_file_for_rating, inputs=rate_file_input, outputs=rate_output)

demo.launch()
