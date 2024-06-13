import io
import sys
import contextlib

def execute_code(code):
    """Executes the provided Python code with basic sandboxing."""

    # Capture stdout for output
    output_buffer = io.StringIO()

    # Basic sandboxing using contextlib.redirect_stdout
    with contextlib.redirect_stdout(output_buffer):
        try:
            exec(code, {'__builtins__': {}})  # Restrict built-in functions for security
            error = None
        except Exception as e:
            error = str(e)

    # Get the output from the buffer
    output = output_buffer.getvalue()

    return output, error