# Career Compass 🧭

A web application that analyzes how well a resume matches a job description using TF-IDF and skill matching.

## Features
- **Resume Parsing**: Supports PDF and DOCX formats.
- **Match Score**: Calculates similarity using TF-IDF and Cosine Similarity.
- **Skill Gap Analysis**: Identifies matched and missing skills based on a predefined database.
- **Suggestions**: Provides actionable tips to improve the resume.
- **Modern UI**: Clean and responsive interface.

## Tech Stack
- **Backend**: Python, Flask
- **Frontend**: HTML, CSS
- **NLP**: scikit-learn (TF-IDF), pdfplumber, python-docx

## Installation

1.  **Clone the repository** (or navigate to the project folder):
    ```bash
    cd career_compass
    ```

2.  **Create a virtual environment** (optional but recommended):
    ```bash
    python -m venv venv
    # Windows
    venv\Scripts\activate
    # Mac/Linux
    source venv/bin/activate
    ```

3.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1.  **Run the application**:
    ```bash
    python app.py
    ```

2.  **Open in browser**:
    Go to [http://127.0.0.1:5000](http://127.0.0.1:5000)

3.  **Analyze**:
    - Upload a resume (PDF/DOCX).
    - Paste a Job Description.
    - Click "Analyze Match".

## Project Structure
```
career_compass/
├── app.py              # Main Flask app
├── matcher.py          # Matching logic
├── preprocess.py       # Text cleaning
├── resume_parser.py    # File extraction
├── skills.py           # Skill database
├── requirements.txt    # Dependencies
├── static/
│   └── style.css       # Styles
├── templates/
│   ├── index.html      # Home page
│   └── result.html     # Result page
└── uploads/            # Temp storage
```
