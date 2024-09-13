from openai import OpenAI


class OpenAIWrapper:
    def __init__(self):
        self.client = OpenAI(
                base_url="http://192.168.1.3:11434/v1",
                api_key="Fake key !!"
                )

    def generate_response(self, messages, max_tokens=30):
        response = self.client.chat.completions.create(
                model="phi",
                max_tokens=max_tokens,
                messages=messages
                )

        return response



if __name__ == "__main__":
    messages = [
                {
                    "role" : "system",
                    "content" :  "Your an assistant that created slogun for marketing based on user short desciption."
                },
                {
                    "role" : "user",
                    "content" : "A company that bakes cake that looks like a cartoon character"
                },

                {
                    "role" : "assistant",
                    "content" : "Indulge in Sweet Imagination with our Edible Art Cakes!"
                }

            ]

    wrapper = OpenAIWrapper()
    running = True

    while running:
        user_input = input(">>> ")

        if user_input == "exit":
            running = False
            continue


        messages.append({
                "role" : "user",
                "content" : user_input
            })

        response = wrapper.generate_response(messages=messages)
        response_text = response.choices[0]. message.content.split("\n")[0]
        print(response_text)

        messages.append({
                "role" : "assistant",
                "content" : response_text
            })




        
