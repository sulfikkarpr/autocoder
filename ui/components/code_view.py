import gradio as gr

def CodeView():
    """Creates a Gradio code block for displaying code."""
    return gr.Code(language="python", show_label=False)