# osheep

# Chatbot frontend

## Overview

This project involves creating a frontend website interface that interacts with a fine-tuned Mistral model hosted on Ollama. The interface sends POST requests to the model to generate specialized responses to instructions related to the Artificial Intelligence and Data Act (AIDA).

# Dataset Creation using Local Language Models

This project involves creating datasets using local language models. It provides a way to generate structured data based on input text, with a focus on summarizing content and generating instructions and responses.

## Overview

The project consists of several Python scripts that work together to generate datasets by interacting with local language models. The key scripts are:

1. **`connect_model.py`**: Handles the interaction with the local language model API.
2. **`data_set_creation.py`**: Contains functions to format, save, and manage datasets.
3. **`process_text.py`**: Split the text into smaller paragraphs.
4. **`main.py`**: The main driver script that coordinates the dataset creation process.

## Files and Functions

### `connect_model.py`

This module is responsible for connecting to a local language model and sending prompts to it.

- **`request_model(model, prompt)`**: 
  - Sends a prompt to a specified language model and retrieves the response.
  - Parameters:
    - `model`: The name of the model to use.
    - `prompt`: The text prompt to send to the model.
  - Returns: The generated response from the model or an error message.

### `data_set_creation.py`

This module contains various utility functions for dataset creation and management.

- **`format_data(model_response)`**:
  - Adds an 'input' key with an empty string as the value to each dataset entry.
  - Parameters: 
    - `model_response`: A JSON string representing a list of dataset dictionaries.
  - Returns: A list of dictionaries with an additional 'input' key.


- **`read_data(save_path)`**:
  - Reads JSON data from a file.
  - Parameters: 
    - `save_path`: The path to the JSON file.
  - Returns: The data from the file.


- **`save_data(dataset, file_path, save_path)`**:
  - Saves the dataset by extending the existing data in a JSON file.
  - Parameters: 
    - `dataset`: A list of dictionaries to be saved.
    - `file_path`: The path to save the updated dataset.
    - `save_path`: The path to the existing data file.


- **`confirm_data_format(dataset)`**:
  - Ensures that the dataset string is properly formatted as a JSON array.
  - Parameters: 
    - `dataset`: The dataset string that needs formatting.


- **`create_input(model, dataset, content)`**:
  - Generates 'input' key values for each dataset entry based on provided content.
  - Parameters: 
    - `model`: The model to use for generating inputs.
    - `dataset`: A JSON string representing a list of dataset dictionaries.
    - `content`: The content used for generating 'input' values.
  - Returns: The updated dataset with generated 'input' values.

### `process_text.py`

This module contains functions for processing and breaking down text into manageable components.

- **`break_down_text()`**:
  - Breaks down the text into a single string and stores its length in a list.
  - Parameters: None.
  - Returns: A list where the first element is the full text as a string and the second element is the length of the text.


- **`text_to_list()`**:
  - Splits the text into a list of paragraphs.
  - Parameters: None.
  - Returns: A list of paragraphs as strings with leading and trailing whitespace removed.

### `main.py`

The main driver script that coordinates the entire dataset creation process.

- **`main()`**:
  - The primary function that controls the flow of the program.
  - It allows the user to choose between different models (mistral or gemma2) and generates datasets by summarizing paragraphs of text.
  - It divides the text into paragraphs, generates instructions and responses using the selected model, and saves the datasets to a JSON file.

## Data

- aida_data_gemma.json
- aida_data_mistral.json
- aida_data_gpt.json
- merged_dataset.json
- text_to_summarize.txt

## Usage

1. **venv Setup**: Ensure virtual environment is setup.

2. **Model Setup**: Ensure the local language model API is running and accessible at the specified URL in `connect_model.py`.

3. **Run the Script**: Execute `main.py` to start the dataset creation process. You can choose between the mistral or gemma2 models by setting the `mistral` variable in the `main()` function.

4. **Output**: The generated datasets will be saved in JSON format in the specified file paths.

## Requirements

- Python 3.x
- `requests` library for making HTTP requests.

## Notes

- Ensure that the local language model API is configured correctly and accessible.
- The text to be summarized should be available in the specified file path (`../data/text_to_summarize.txt`).

## License

This project is licensed under the MIT License. See the LICENSE file for details.