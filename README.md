# AI Assignment Agent

This project is an AI-powered assignment explainer. It helps students understand programming assignments. The app uses Google Gemini (GenAI) for explanations.

## Features

- Simple web interface for students to paste assignment questions.
- AI explains the assignment, key concepts, and common mistakes.
- Shows extracted features from the question.
- Uses Flask for backend API and serving the frontend.
- Connects to Google Gemini API for AI responses.

## How it works

1. The user opens the web app in a browser.
2. The user pastes a programming assignment question.
3. The app extracts features from the question.
4. The app sends the question to the backend API.
5. The backend uses Google Gemini to generate an explanation.
6. The frontend displays the explanation and features.

## Project Structure

```
Diagram created using GitHub Copilot
+-------------------+
|   Frontend (JS)   |
+-------------------+
          |
          v
+-------------------+
|   Flask Backend   |
+-------------------+
          |
          v
+-------------------+
|  Google Gemini AI |
+-------------------+
```

- The frontend is built with HTML, CSS, and JavaScript.
- The backend is a Flask app in Python.
- The backend calls the Gemini API for explanations.

## Setup Instructions

1. Clone the repository.
2. Create a Python virtual environment.
3. Install dependencies with `pip install -r requirements.txt`.
4. Add your Google Gemini API key to a `.env` file:
   - `GOOGLE_API_KEY=your_api_key_here`
5. Start the Flask app with `python app.py`.
6. Open `http://localhost:5000` in your browser.

## Security

- The `.env` file is not tracked in the repository.
- Do not share your API key publicly.

## Usage

- Paste your assignment question in the text area.
- Click "Explain" to get an AI-generated breakdown.
- View features and the explanation below the form.

## Contributing

Feel free to open issues or submit pull requests.

---

This project is for educational purposes. It does not provide full assignment solutions.
