"""
Connect to local LLM model.
"""

import requests


def request_model(model, prompt):
    """
    Send a prompt to a model for generating a response based on the given instruction.

    This function makes an HTTP POST request to a local API that interacts with a language model.
    The prompt is sent along with the model's name, and the response is retrieved and returned.

    :param model: The name or identifier of the model to be used for generating the response.
    :param prompt: The text prompt that will be sent to the model for generating a response.
    :return: The generated response from the model if the request is successful,
             otherwise print an error message with the status code and error content.
    """
    # local API of the LLM model
    url = "http://localhost:11434/api/generate"

    payload = {
        "model": model,
        "prompt": prompt,
        "stream": False
    }

    response = requests.post(url, json=payload)

    if response.status_code == 200:
        return response.json()["response"]
    else:
        print(f"Error: {response.status_code}, {response.content}")
