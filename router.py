import os
from together import Together

class Router:
  models: list

  def _get_optimal_model(query):
    pass

  def call_model(query, model):
    """
    Takes a model and an input prompt, calls Together.ai and outputs response
    """
    client = Together(api_key=os.environ['TOGETHER_API_KEY'])

    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": query}],
    )
    return response.choices[0].message.content

  
  def answer_query(query):
    model = _get_optimal_model(query)
    pass