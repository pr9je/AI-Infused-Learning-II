import gradio as gr
from agent import agent

def chat(message, history):
    # Gradio fills in `message` (newest) and `history` (past turns) for you.
    return agent(message)


gr.ChatInterface(
    fn=chat,
    title="🛍️ Smart Shop Assistant",
    description="Ask me the price of shoes, hat, bag, shorts or pants — I'll look it up.",
).launch(share=True)   # share=True -> also prints a public link you can postpi