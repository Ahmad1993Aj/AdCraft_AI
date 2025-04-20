from . import config

class PromptGenerator:
    def __init__(self, client, prompt_config):
        self.prompt_config = prompt_config
        self.client = client
        self.chat = self.generate_initial_answer()

    def generate_initial_answer(self):
        system_prompt = "You are creating advertising texts for a concert hall."
        content_prompt = f"""
        Concert hall area: {self.prompt_config.concert_hall_area}
        Channel used for marketing: {self.prompt_config.channel}
        Target audience age: {self.prompt_config.age}
        Length of the text: {self.prompt_config.length} sentences
        Create a compelling advertising text.
        """

        chat_completion = self.client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": system_prompt
                },
                {
                    "role": "user",
                    "content": content_prompt
                }
            ],
            model="gpt-4o-mini",
            temperature=config.temperature,
            n=config.n,
        )
        return chat_completion

    def get_most_recent_answer(self):
        return self.chat.choices[0].message.content

    def change_prompt(self, parameter):
        pass