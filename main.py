from llm import correct_answer_sheet
from text_extraction import upload_image
import os

if __name__ == "__main__":
    directory = os.listdir("./answer_sheets")

    user_answer = []

    print("Reading Files...")

    for file in directory:
        user_answer.append("https://ibb.co/7RJzZv6")

    answer_key = "https://ibb.co/sVw9B2F"

    total = int(input("Enter total marks: "))

    print("Generating Result...")

    print(correct_answer_sheet(answer_key, total, user_answer))