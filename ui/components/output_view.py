import gradio as gr

def OutputView():
    """Creates a Gradio text box for displaying output."""
    return gr.Textbox(label="Output", lines=5)