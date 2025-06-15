from flask import Flask, request, render_template
from content_extractor import extract_content
from groq_api import query_groq
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form['url']
        question = request.form['question']

        try:
            content = extract_content(url)
            if not content:
                return render_template('index.html', error="Failed to extract content from the URL.")

            answer = query_groq(content, question)
            answer_lines = answer.splitlines()

            return render_template('index.html', url=url, question=question, answer_lines=answer_lines)

        except Exception as e:
            print(f"Error processing request: {e}")
            return render_template('index.html', error=f"An error occurred: {e}")

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)