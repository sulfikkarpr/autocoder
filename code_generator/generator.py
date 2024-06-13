import requests
from config import settings  # Assuming your config.py file exists

def generate_code(prompt, max_length=None, temperature=None):
    """
    Generates code using the Hugging Face Inference API.

    Args:
        prompt (str): The prompt describing the desired code.
        max_length (int, optional): Maximum length of the generated code. Defaults to None.
        temperature (float, optional): Controls the creativity of the generation. Defaults to None.
    """
    api_url = f"https://api-inference.huggingface.co/models/{settings.DEFAULT_CODE_MODEL}"
    headers = {"Authorization": f"Bearer {settings.HF_API_TOKEN}"}

    payload = {"inputs": prompt}
    if max_length is not None:
        payload["parameters"] = {"max_length": max_length}
    if temperature is not None:
        if "parameters" not in payload:
            payload["parameters"] = {}
        payload["parameters"]["temperature"] = temperature

    try:
        response = requests.post(api_url, headers=headers, json=payload)
        response.raise_for_status()  # Raise an exception for bad API responses

        generated_code = response.json()[0]["generated_text"]

        # Optionally format the code for readability (e.g., using 'black' or 'yapf')
        # ...

        return generated_code

    except requests.exceptions.RequestException as e:
        if response.status_code == 400:
            return f"Error: Bad Request. Ensure your prompt is formatted correctly.\nDetails: {response.text}"
        elif response.status_code == 403:
            return f"Error: Forbidden. Your API token might not have access to this model.\nDetails: {response.text}"
        elif response.status_code == 401:
            return f"Error: Unauthorized. Invalid API token.\nDetails: {response.text}"
        else:
            return f"Error: Could not generate code.\nDetails: {e}"


# Example usage:
if __name__ == "__main__":
    prompt = "Write a Python function to calculate the factorial of a number."
    generated_code = generate_code(prompt, max_length=50, temperature=0.5)

    if isinstance(generated_code, str) and generated_code.startswith("Error:"):
        print(generated_code)
    else:
        print(generated_code)