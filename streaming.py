import os
from together import Together


def call_model_stream(query, model):
    client = Together(api_key=os.environ.get("TOGETHER_API_KEY"))
    stream = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": query}],
        stream=True,
    )

    for chunk in stream:
        yield chunk.choices[0].delta.content

model="mistralai/Mixtral-8x7B-Instruct-v0.1"
prompt = "tell me about new york"

response = call_model_stream(prompt, model)
for chunk in response:
    print(chunk, end='')

full_response = ""  # Initialize an empty string to collect the response
for chunk in response:
    full_response+= chunk

print(full_response)