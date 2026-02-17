import re

def clean_text(text):
    """
    Cleans text by removing special characters, converting to lowercase, 
    and removing extra whitespace.
    """
    if not text:
        return ""
    
    # Convert to lowercase
    text = text.lower()
    
    # Remove special characters and numbers (keep letters and basic punctuation)
    # Actually for skills like "c++" or "node.js", we need to be careful.
    # Let's keep alphanumeric and some specific chars like +, #, . for skills.
    # For general TF-IDF, simple cleanup is usually okay, but we want to capture skills.
    
    # Replace newlines and tabs with space
    text = text.replace('\n', ' ').replace('\t', ' ')
    
    # Remove multiple spaces
    text = re.sub(r'\s+', ' ', text)
    
    # We will strictly clean mostly for TF-IDF but keep a version for skill extraction if needed.
    # However, for simplicity in this project, we'll just normalize spaces and casing.
    # Real-world detailed cleaning might strip "c++" to "c", so we iterate carefully in skill matching.
    
    return text.strip()
