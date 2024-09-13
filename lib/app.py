from lib.wiki_wrapper import WikiWrapper
from lib.openai_wrapper import OpenAIWrapper

class App:
    def __init__(self):
        self.wiki = WikiWrapper()
        self.openai = OpenAIWrapper()

    def run(self, name, debug=False):

        summary = self.wiki.get_summary(name=name)

        if summary is None:
            print(f"Summary of {name} is not found")
            return

        if debug:
            print(summary)


        initial_messages = [
                    {
                        "role" : "system",
                        "content" :  f"Your an assistant that answers to user question based on {name}.Here is a summary of {name} = {summary}.Dont ans if the info not in the summary"
                    }
                ]


        running = True


        while running:
            user_input = input(">>> ")

            if user_input == "exit":
                running = False
                continue

            messages = []
            messages += initial_messages

            messages.append({
                    "role" : "user",
                    "content" : user_input
                })

            response = self.openai.generate_response(messages=messages)
            response_text = response.choices[0]. message.content.split("\n")[0]
            print(response_text)






