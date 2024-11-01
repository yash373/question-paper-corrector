# Answer Sheet Corrector

This is a simple script that uses the LLaMA model to correct answer sheets. It takes in a directory of images and an answer key, and outputs a corrected answer sheet with marks and feedback.

## Usage

1. Install the required packages with `pip install -r requirements.txt`.
2. Create a directory called `answer_sheets` and add the images of the answer sheets to it.
3. Create a file called `answer_key.jpg` and add the answer key to it.
4. Run the script with `python main.py`.
5. Enter the total marks for the answer sheet when prompted.

## Note

This script assumes that the answer key is in the format of a single image with the correct answers written on it. The script will then use the LLaMA model to correct the answer sheets based on the answer key.

## Disclaimer

This script is for educational purposes only and should not be used for any commercial or malicious purposes. The LLaMA model is not perfect and may make mistakes, so please use it responsibly.
