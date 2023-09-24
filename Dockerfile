FROM python:3.11.5-slim

ADD hangman.py .

CMD ["python", "./hangman.py"]
