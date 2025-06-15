# Link Analyzer ChatBot

An intelligent chatbot that automates the extraction of web content from URLs and answers user questions using advanced natural language processing (NLP) models.

---

## Overview

This project combines the power of web scraping and AI to build a chatbot that can:

* Automatically extract and summarize content from websites.
* Understand and answer user queries using the extracted content.
* Provide a conversational interface for natural interactions.

---

## Features

* **Web Content Extraction**: Scrapes content from any given URL using tools like BeautifulSoup or Newspaper3k.
* **AI-Powered Q\&A**: Utilizes LLMs (e.g., Hugging Face Transformers, BERT, or GPT models) to provide answers.
* **Interactive Chat Interface**: Simple UI for user interaction via web browser.
* **Contextual Understanding**: Maintains conversation flow to handle follow-up questions.
* **Multilingual Support** *(optional)*: Extendable to multiple languages.

---

## Tech Stack

| Layer        | Technology                             |
| ------------ | -------------------------------------- |
| Frontend     | HTML, CSS, JavaScript                  |
| Backend      | Python, Flask                          |
| NLP Models   | Hugging Face Transformers / BERT / GPT |
| Web Scraping | BeautifulSoup / Newspaper3k            |
| Deployment   | Localhost / Any cloud provider         |

---

## Project Structure

```
├── app/
│   ├── static/                # CSS, JS, images
│   ├── templates/             # HTML templates
│   ├── main.py                # Flask application
│   ├── content_extractor.py   # Web scraping logic
│   ├── qa_engine.py           # AI Q&A model code
├── .env                       # Environment variables (API keys)
├── requirements.txt
├── README.md
```

---

## Installation & Setup

1. **Clone the repository**

   ```bash
   git clone https://github.com/your-username/ai-chatbot-web-content-qa.git
   cd ai-chatbot-web-content-qa
   ```

2. **Create a virtual environment (optional but recommended)**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up your API Key**

   If your project uses an external LLM API (e.g., OpenAI or Hugging Face), create a `.env` file in the root directory:

   ```env
   API_KEY=your_api_key_here
   ```

   Then, in your Python code, load the key securely using:

   ```python
   import os
   from dotenv import load_dotenv

   load_dotenv()
   api_key = os.getenv("API_KEY")
   ```

   > 🔒 **Never hard-code your API keys!** Use `.env` and add it to `.gitignore`.

5. **Run the app**

   ```bash
   python main.py
   ```

6. **Open in browser**
   Visit `http://127.0.0.1:5000/`

---

## 🤔 Example Usage

1. Enter a website URL (e.g., a news article or blog post).
2. The chatbot extracts the content.
3. Ask questions like:

   * "What is this article about?"
   * "Who is the author?"
   * "When was it published?"
4. Get context-aware, AI-generated answers instantly.

---

## Future Enhancements

* Add support for PDF and DOCX file uploads.
* Improve summarization before QA.
* Add login/user tracking.
* Deploy on cloud (e.g., Heroku, Render, or AWS).

---

## Acknowledgements

* [Hugging Face Transformers](https://huggingface.co/)
* [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/)
* [Flask](https://flask.palletsprojects.com/)
* [Newspaper3k](https://github.com/codelucas/newspaper)

