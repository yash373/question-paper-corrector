from llm import correct_answer_sheet
from text_extraction import upload_image
import os

if __name__ == "__main__":
    directory = os.listdir("./answer_sheets")

    user_answer = []

    for file in directory:
        user_answer.append(upload_image(f"./answer_sheets/{file}"))

    answer_key = upload_image("answer_key.jpg")

    total = int(input("Enter total marks: "))

    print(correct_answer_sheet(answer_key, total, user_answer))