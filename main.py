from llm import correction
from text_extraction import readText

if __name__ == "__main__":
    total = int(input("Enter total marks: "))

    answer_key = readText("answer_key.jpg")

    user_answer = readText("answer_sheet.jpg")

    print(correction(answer_key, total, user_answer))