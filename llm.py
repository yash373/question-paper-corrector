from groq import Groq
from dotenv import load_dotenv

# Loads Dot Files
load_dotenv('.env.local')

def correction(answer_key:str, total_marks:int , user_answer:str) -> str:
    client = Groq()

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": "You are a genius teacher who is really good at correcting question papers. You must read the answer key and the student answer and give marks on the paper based on the given total marks and also give adequate feedback so that the student can improve."
            },
            {
                "role": "user",
                "content": f"Total Marks: {total_marks}\n\nAnswer Key: {answer_key}\n\nStudent Answer: {user_answer}\n\nMarks: ",
            }
        ],

        model="llama3-8b-8192",

        temperature=0.5,

        max_tokens=1024,

        top_p=1,

        stop=None,

        stream=False,
    )

    return (chat_completion.choices[0].message.content)