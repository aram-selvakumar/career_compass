from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from skills import SKILLS_DB
from preprocess import clean_text
import re

def calculate_match_score(resume_text, jd_text):
    """
    Calculates the match score using TF-IDF and Cosine Similarity.
    Returns score as a percentage (0-100).
    """
    if not resume_text or not jd_text:
        return 0.0

    resume_clean = clean_text(resume_text)
    jd_clean = clean_text(jd_text)

    documents = [resume_clean, jd_clean]
    
    vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = vectorizer.fit_transform(documents)
    
    # Cosine similarity between the two documents
    similarity = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])[0][0]
    
    return round(similarity * 100, 2)

def extract_skills_from_text(text):
    """
    Extracts skills from text based on the predefined SKILLS_DB.
    """
    clean_txt = clean_text(text)
    found_skills = set()
    
    # Simple keyword matching
    # Note: This finds "java" in "javascript" if not careful. 
    # Better approach uses word boundaries, but some skills have special chars (c++, node.js).
    # We will tokenize by space for simpler matching or use regex.
    
    # Create word set for faster lookup, but handling multi-word skills is tricky.
    # We will iterate through the DB and check existence in text.
    
    for skill in SKILLS_DB:
        # Regex to find whole word or phrase, case insenstive (text is already lower)
        # Escape special chars in skill name
        pattern = r'\b' + re.escape(skill) + r'\b'
        if re.search(pattern, clean_txt):
            found_skills.add(skill)
            
    return list(found_skills)

def calculate_skill_gap(resume_text, jd_text):
    """
    Identifies matched skills and missing skills.
    Returns (matched_skills, missing_skills, match_percentage).
    """
    resume_skills = set(extract_skills_from_text(resume_text))
    jd_skills = set(extract_skills_from_text(jd_text))
    
    if not jd_skills:
        return list(resume_skills), [], 0.0, list(resume_skills) # No skills in JD, so technically 100% or 0% match depending on logic. Let's return 0 gap.

    matched_skills = list(resume_skills.intersection(jd_skills))
    missing_skills = list(jd_skills - resume_skills)
    
    match_percentage = (len(matched_skills) / len(jd_skills)) * 100
    
    return matched_skills, missing_skills, round(match_percentage, 2), list(jd_skills)
