"""
Determine number of datasets
"""

import json
import connect_model


def format_data(model_response):
    """
    Add an 'input' key with an empty string as the value to each dataset entry.

    :param model_response: A JSON string containing a list of datasets (each as a dictionary).
    :return: A list of dictionaries, where each dictionary has an additional 'input' key with an empty
    string as its value.
    """
    generated_input = ""
    model_response = json.loads(model_response)
    for data in model_response:
        data.update({"input": generated_input})
    return model_response


def read_data(save_path):
    """
    Read JSON data from a file.

    :param save_path: The path to the JSON file to read.
    :return: The data from the file as a Python object.
    """
    with open(save_path, "r") as file:
        data = json.load(file)
    return data


def save_data(dataset, file_path, save_path):
    """
    Save the dataset by extending the existing data in a JSON file.

    :param dataset: A list of dictionaries to be added to the file.
    :param file_path: The path where the updated dataset will be saved.
    :param save_path: The path to the existing data file that needs to be extended.
    """
    # store full dictionary into json file
    data = read_data(save_path)
    data.extend(dataset)

    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)


def confirm_data_format(dataset):
    """
    Ensure that the dataset string is properly formatted as a JSON array.

    This function removes any extraneous characters before and after the JSON array
    to ensure that it can be parsed correctly.

    :param dataset: The dataset string that needs to be formatted as a JSON array.
    """
    while dataset[0] != "[":
        dataset = dataset[1:]
    while dataset[-1] != "]":
        dataset = dataset[:-1]


def create_input(model, dataset, content):
    """
    Generate the 'input' key values for each dataset entry based on the provided content.

    This function sends a prompt to a model to generate a string for the 'input' key
    that is relevant to the 'instruction' and 'response' in each dataset entry.

    :param model: The model to be used for generating the input.
    :param dataset: A JSON string representing a list of dataset dictionaries.
    :param content: The content to be used in generating the 'input' values.
    :return: The updated dataset with generated 'input' values for each entry.
    """
    dataset = json.loads(dataset)
    for data in dataset:
        model_prompt = f"#Based on the text in the ##Content and the instruction: {data['instruction']} and the response {data['response']}, generate the corresponding input. ##Content: {content}"
        model_prompt = f"""
### Instruction:
Generate a string value for the "input" key based on the provided text in the "Content" section. The generated input should align with the context of the "instruction" and the "response" values. Ensure that the input string is relevant and appropriate to the given instruction and response.

### Content:
{content}

### Instruction Provided:
{data['instruction']}

### Response Provided:
{data['response']}
"""
        generated_input = connect_model.request_model(model, model_prompt)
        data["input"] = generated_input.strip()
    return dataset
