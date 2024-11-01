from groq import Groq
from dotenv import load_dotenv

# Loads Dot Files
load_dotenv('.env.local')

class Message:
    def __init__(self, role, content, image_url):
        self.role = role
        self.content = content
        self.image_url = image_url
    
    def getMessage(self):
        return {
            "role": self.role,
            "content": [
                {
                    "type": "text",
                    "text": self.content
                },
                {
                    "type": "image_url",
                    "image_url": {
                        "url": self.image_url
                    }
                }
            ]
        }

def correct_answer_sheet(answer_key: str, total_marks: int, user_answers: list[str]) -> str:
    """Correct an answer sheet using the LLaMA model."""

    # Build the messages to send to the LLaMA model
    messages = [
        {
            "role": "system",
            "content": "You are a genius teacher who is really good at correcting question papers. You must read the answer key and the student answer and give marks on the paper based on the given total marks and also give adequate feedback so that the student can improve."
        }
    ]

    # Add the user answers to the messages
    for index, user_answer in enumerate(user_answers):
        messages.append(Message("user", f"Answer Sheet {index+1}/{len(user_answers)}", user_answer))

    # Add the answer key to the messages
    messages.append(Message("user", "Answer Key, Note: The total marks is " + str(total_marks) + "\n\nPlease Correcrt the following:\n", answer_key))

    # Create the client and get the chat completion
    client = Groq()
    chat_completion = client.chat.completions.create(
        messages=messages,
        model="llama-3.2-11b-vision-preview",
        temperature=0.5,
        max_tokens=1024,
        top_p=1,
        stop=None,
        stream=False,
    )

    # Return the result
    return chat_completion.choices[0].message.content
