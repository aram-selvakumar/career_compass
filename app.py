import os
from flask import Flask, render_template, request, redirect, url_for, flash
from werkzeug.utils import secure_filename
from resume_parser import extract_text
from matcher import calculate_match_score, calculate_skill_gap

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Needed for flash messages

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'pdf', 'docx'}

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    if 'resume' not in request.files:
        flash('No file part')
        return redirect(url_for('index'))
    
    file = request.files['resume']
    jd_text = request.form.get('job_description')

    if file.filename == '':
        flash('No selected file')
        return redirect(url_for('index'))

    if not jd_text or not jd_text.strip():
        flash('Please enter a job description')
        return redirect(url_for('index'))

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)

        # Extract text
        resume_text = extract_text(filepath)
        
        # Cleanup uploaded file after extraction (optional, but good for temp storage)
        # For now, we keep it or could delete it. Let's keep it simple.
        
        # Calculations
        tfidf_score = calculate_match_score(resume_text, jd_text)
        matched_skills, missing_skills, skill_match_score, jd_skills = calculate_skill_gap(resume_text, jd_text)
        
        # Generate suggestions
        suggestions = []
        if tfidf_score < 50:
            suggestions.append("Your resume content has low similarity with the job description. Try to mirror some keywords from the JD.")
        if missing_skills:
            suggestions.append(f"Consider adding these missing skills to your resume: {', '.join(missing_skills[:5])}...")
        if not matched_skills:
            suggestions.append("We couldn't find any matching technical skills. Ensure your resume lists skills clearly.")

        # Final weighted score (optional, but requested: convert similarity to percentage and show skill match)
        # We will show both.
        
        return render_template('result.html', 
                               match_score=tfidf_score,
                               skill_score=skill_match_score,
                               matched_skills=matched_skills,
                               missing_skills=missing_skills,
                               jd_skills=jd_skills,
                               suggestions=suggestions,
                               filename=filename)
    else:
        flash('Allowed file types are PDF and DOCX')
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
