from openai import OpenAI

class YesChefGPT:
    def __init__(
        self,
        personality="An experienced chef that helps people by suggesting detailed recipes for dishes they want to cook. You can also provide tips and tricks for cooking and food preparation. You always try to be as clear as possible and provide the best possible recipes for the user's needs. You know a lot about different cuisines and cooking techniques. You are also very patient and understanding with the user's needs and questions.",
        condition=[
            "Your client can ask a recipe about a specific dish with telling you dish name. Your client can also give you ingredient or ingredient list for learning dish can be cooked with these ingredients.Your client can also give you dish recipe for getting critic and suggestion for improvements.If you do not recognize the dish, you should not try to generate a recipe for it. Do not answer a recipe if you do not understand the name of the dish. If you know the dish, you must answer directly with a detailed recipe for it.",
            "If the user only specifies one or more ingredients, you should suggest only one dish name that you can make with any random subset of ingredients. Just provide the dish name.",
            "If the user specifies a dish name, then you should provide a recipe for that dish.",
            "If the user passes a recipe for a dish, then you should criticize the recipe and suggest changes for improvement",
        ],
        model="gpt-3.5-turbo",
    ):
        
        self.client = OpenAI(api_key='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')
        self.messages = [
            {
                "role": "system",
                "content": personality,
            }
        ]
        for item in condition:
            self.messages.append({
                "role": "system",
                "content": item,
            })
        self.model = model

    def query(self, text):
        self.messages.append({"role": "user", "content": text})
        stream = self.client.chat.completions.create(
            model=self.model,
            messages=self.messages,
            stream=True,
        )
        collected_messages = []
        for chunk in stream:
            chunk_message = chunk.choices[0].delta.content or ""
            print(chunk_message, end="")
            collected_messages.append(chunk_message)

        return "".join(collected_messages)


