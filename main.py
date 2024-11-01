from llm import correct_answer_sheet
from text_extraction import upload_image

if __name__ == "__main__":
    total = int(input("Enter total marks: "))

    answer_key = upload_image("answer_key.jpg")

    user_answer = [upload_image("answer_sheet.jpg")]

    print(correct_answer_sheet(answer_key, total, user_answer))