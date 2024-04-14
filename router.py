# our usual suspects
the_usual_suspects = [
    {
        "endpoint": "NousResearch/Nous-Hermes-2-Mistral-7B-DPO",
        "price": "0.2",
        "type": "Chat",
    },
    {"endpoint": "mistralai/Mixtral8x22B", "price": "1.2", "type": "Language"},
    {"endpoint": "google/gemma-2b", "price": "0.1", "type": "Language"},
]


class Router:
    def __init__(self, models):
        self.models = models

    def _get_optimal_model(self, query):
        if len(query) <= 4000:  #
            return "google/gemma-2b"
        elif len(query) >= 4000 and len(query) <= 10000:
            return "NousResearch/Nous-Hermes-2-Mistral-7B-DPO"
        else:
            return "mistralai/Mixtral8x22B"

    def _call_model(self, query, model):
        return query, model

    def answer_query(self, query):
        model_endpoint = self._get_optimal_model(query)
        answer = self._call_model(query, model_endpoint)
        return answer


if __name__ == "__main__":
    router = Router(the_usual_suspects)
    answer = router.answer_query("This is a test")
    print(answer)
