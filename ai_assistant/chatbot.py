import gradio as gr
from ai_assistant.agent import LegalAgent
from ai_assistant.prompts import agent_prompt_tpl

agent = LegalAgent(agent_prompt_tpl).get_agent()

def agent_response(message):
    return agent.chat(message).response

if __name__ == "__main__":
    demo = gr.ChatInterface(agent_response, type="messages")
    demo.launch()

