import gradio as gr
from code_generator import generator  # Import the module
from executor import executor
from utils.file_manager import save_to_file
from ui.components.code_view import CodeView
from ui.components.output_view import OutputView
from config import settings

def generate_and_display_code(prompt):
    """Generates code, displays it, executes it, and displays the output."""

    generated_code = generator.generate_code(prompt)
    # code_view = CodeView()
    # code_view.update(value=generated_code)

    # Execute the code (if execution is enabled)
    if settings.EXECUTE_CODE:  # Check if code execution is enabled in settings
        # output, error = executor.execute_code(generated_code)
        # output_view = OutputView()
        # output_view.update(value=f"Output:\n{output}\n\nError:\n{error}" if error else f"Output:\n{output}")
        output, error = executor.execute_code(generated_code)
        output_value = f"Output:\n{output}\n\nError:\n{error}" if error else f"Output:\n{output}"
    else:
        output_value = "Code execution is disabled in settings."
        # output_view = OutputView()
        # output_view.update(value="Code execution is disabled in settings.")

    save_to_file(generated_code)
    # return code_view, output_view
    return generated_code, output_value

# Define the Gradio interface
iface = gr.Interface(
    fn=generate_and_display_code,
    inputs="text",
    outputs=[CodeView(), OutputView()],  # Call functions to create instances
    title=settings.UI_TITLE,
    description="Generate and optionally run Python code from your prompts!"
)

# Launch the Gradio interface
if __name__ == "__main__":
    iface.launch(share=True)