import json
import connect_model
import data_set_creation
import process_text


def main():
    """
    Drives the pogram.
    """
    # choose between mistral or gemma model for instruction processing
    mistral = False

    # mistral variables
    model_mistral = "mistral"
    file_path_mistral = "../data/aida_data_mistral2.json"
    save_path_mistral = "../data/aida_data_mistral2.json"

    # gemma variables
    model_gemma = "gemma2"
    file_path_gemma = "../data/aida_data_gemma2.json"
    save_path_gemma = "../data/aida_data_gemma2.json"

    # prepare content to generate dataset on
    paragraphs = process_text.text_to_list()

    # using mistral model to generate dataset
    if mistral:
        for paragraph in paragraphs:

            # determine how many datasets to create for each paragraph
            count = len(paragraph) // 100
            if count == 0:
                count = 1

            # instruction for the model to generate dataset
            prompt_mistral = f'###instruction: based on the content section, summarize the text and return only a python list (nothing extra) which contains {count} different dictionaries of key ("instruction", "response") value pairs covering key points of the content text. Example: {{"instruction": "Create a natural language instruction that specifically references the Artificial Intelligence and Data Act (AIDA)", "response": "sentence explanation for the given prompt, per the instructions and context provided"}} ### content: "{paragraph}"'

            # generate dataset using mistral
            response = connect_model.request_model(model_mistral, prompt_mistral)

            # confirm response format is correct
            data_set_creation.confirm_data_format(model_mistral, response)

            ## use AI to provide input to each dictionary
            # response = data_set_creation.create_input(model_mistral, response, paragraphs[0])

            response = json.loads(response.strip())  # skipping input key value pair

            # save datasets to json
            data_set_creation.save_data(response, file_path_mistral, save_path_mistral)

    # using gemma model to generate dataset (same logic and code as above)
    else:
        for paragraph in paragraphs:

            count = len(paragraph) // 100
            if count == 0:
                count = 1

            prompt_mistral = f'###instruction: based on the content section, summarize the text and return only a python list (nothing extra) which contains {count} different dictionaries of key ("instruction", "response") value pairs covering key points of the content text. Example: {{"instruction": "Create a natural language instruction that specifically references the Artificial Intelligence and Data Act (AIDA)", "response": "sentence explanation for the given prompt, per the instructions and context provided"}} ### content: "{paragraph}"'

            response = connect_model.request_model(model_gemma, prompt_mistral)
            data_set_creation.confirm_data_format(model_gemma, response)
            response = json.loads(response.strip())
            data_set_creation.save_data(response, file_path_gemma, save_path_gemma)


if __name__ == '__main__':
    main()
