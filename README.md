# Emotion Detector Application

This project is a Flask-based web application developed as part of the **IBM Generative AI Engineering Professional Certificate**. It utilizes the **Watson NLP Emotion Prediction service** to analyze text and return scores for five specific emotions.

## Features
- **Emotion Analysis**: Detects anger, disgust, fear, joy, and sadness[cite: 3].
- **Dominant Emotion Detection**: Automatically identifies the strongest emotion from the input text[cite: 4].
- **Robust Error Handling**: Specifically handles empty or invalid inputs (Status Code 400) by returning a clear user message: *"Invalid text! Please try again!"*.
- **RESTful API**: Implements a clean `/emotionDetector` endpoint for web-based queries[cite: 5].

## Technical Stack
- **Python 3**
- **Flask** (Web Framework)
- **Requests** (HTTP Library)
- **Watson NLP Runtime API**

## Installation & Usage
1. Clone the repository:
   \`git clone https://github.com/AEASodium/oaqjp-final-project-emb-ai.git\`
2. Install dependencies:
   \`pip install -r requirements.txt\`
3. Run the application:
   \`python3 server.py\`
4. Open your browser to \`http://localhost:5000\`
