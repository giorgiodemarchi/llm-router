import os
from together import Together

from llmlingua import PromptCompressor



# def chat_completion(prompt, model):
#     client = Together(api_key=os.environ['TOGETHER_API_KEY'])

#     response = client.chat.completions.create(
#         model=model,
#         messages=[{"role": "user", "content": prompt}],
#     )
#     return response.choices[0].message.content

# model="mistralai/Mixtral-8x7B-Instruct-v0.1"
# prompt = "Tell me fun things to do in New York"

# response = chat_completion(prompt, model)

prompt = "Question: Sam bought a dozen boxes, each with 30 highlighter pens inside, for $10 each box. He reanged five of boxes into packages of sixlters each and sold them $3 per. He sold the rest theters separately at the of three pens $2. How much did make in total, dollars?\nLets think step step\nSam bought 1 boxes x00 oflters.\nHe bought 12 * 300ters in total\nSam then took 5 boxes 6ters0ters.\nHe sold these boxes for 5 *5\nAfterelling these  boxes there were 3030 highlighters remaining.\nThese form 330 / 3 = 110 groups of three pens.\nHe sold each of these groups for $2 each, so made 110 * 2 = $220 from them.\nIn total, then, he earned $220 + $15 = $235.\nSince his original cost was $120, he earned $235 - $120 = $115 in profit.\nThe answer is 115"

llm_lingua = PromptCompressor()
compressed_prompt = llm_lingua.compress_prompt(prompt, instruction="", question="", target_token=200)

print(prompt)
print(compressed_prompt)