import re

def check_password_strength(password):
    """Check the strength of a password and return a score."""
    score = 0
    
    # Check if password is at least 8 characters long
    if len(password) >= 8:
        score += 1
    
    # Check if password contains at least one lowercase letter
    if re.search(r"[a-z]", password):
        score += 1
    
    # Check if password contains at least one uppercase letter
    if re.search(r"[A-Z]", password):
        score += 1
    
    # Check if password contains at least one digit
    if re.search(r"\d", password):
        score += 1
    
    # Check if password contains at least one special character
    if re.search(r"[!@#$%^&*()\-_=+{}[\]|\\:;\"',.<>/?]", password):
        score += 1
    
    return score