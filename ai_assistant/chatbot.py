import gradio as gr
from ai_assistant.agent import LegalAgent
from ai_assistant.prompts import agent_prompt_tpl
from ai_assistant.utils import extract_text_from_pdf

agent = LegalAgent(agent_prompt_tpl).get_agent()

def agent_response_text(message, history=None):
    """Procesa solo el texto del mensaje."""
    return agent.chat(message).response

def agent_response_file(file):
    """Procesa el archivo PDF subido."""
    if file is not None:
        pdf_content = extract_text_from_pdf(file.name)
        response = agent.chat(f"Mejora el siguiente contrato:\n{pdf_content}").response
        return response
    return "No se ha proporcionado ningún archivo."

with gr.Blocks(css="""
    .container { max-width: 750px; margin: auto; padding: 20px; }
    .title { text-align: center; font-size: 1.5em; color: #333; margin-bottom: 20px; }
    .file-section { margin-top: 20px; padding: 15px; background-color: #f7f7f7; border-radius: 8px; }
    .file-section h3 { color: #444; }
""") as demo:
    gr.Markdown("<div class='title'>💼 Chatbot de Asistencia Legal Automatizada</div>")

    chatbot = gr.ChatInterface(fn=agent_response_text, type="messages")

    with gr.Column(elem_classes="file-section"):
        gr.Markdown("### Subir contrato en PDF para mejora")
        file_input = gr.File(label="Subir contrato en PDF para mejora")
        file_output = gr.Textbox(label="Respuesta del asistente")

        file_input.change(agent_response_file, inputs=file_input, outputs=file_output)

demo.launch()
