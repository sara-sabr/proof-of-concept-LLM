# print(len("The proposed Artificial Intelligence and Data Act (AIDA), introduced as part of the Digital Charter Implementation Act, 2022, would set the foundation for the responsible design, development and deployment of AI systems that impact the lives of Canadians. The Act would ensure that AI systems deployed in Canada are safe and non-discriminatory and would hold businesses accountable for how they develop and use these technologies."))
#
# print(430 // 120)
#
# import json
#
# with open("../data/merged_dataset.json", "r") as file:
#     data = json.load(file)
#
# print(len(data))
#
#
# with open("../data/text_to_summarize.txt", "r") as file:
#     data = file.read()
#
# print("number of letters: ", len(data))
# print("number of questions: ", len(data) // 120)
#
#
# with open("../data/aida_dataset_mistral.json", "r") as file:
#     data = json.load(file)
#     print("mistral data count: ", len(data))
#
# with open("../data/aida_dataset_gemma.json", "r") as file:
#     data = json.load(file)
#     print("gemma data count: ", len(data))


#pip install huggingface_hub

#export HF_TOKEN="<>"



from huggingface_hub import InferenceClient

import json



repo_id = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"



llm_client = InferenceClient(

    model=repo_id,

    timeout=120,

)



def call_llm(inference_client: InferenceClient, prompt: str):

    response = inference_client.post(

        json={

            "inputs": prompt,

            "parameters": {"max_new_tokens": 200},

            "task": "text-generation",

        },

    )

    return json.loads(response.decode())[0]["generated_text"]





response=call_llm(llm_client, "tell me a crazy joke")

print (response)