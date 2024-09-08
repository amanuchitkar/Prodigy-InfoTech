import re

def password_strength_checker(password):
    """
    Check the strength of a password based on multiple criteria and give feedback.
    
    Criteria:
    - Length: At least 8 characters
    - Contains both lowercase and uppercase letters
    - Contains numbers
    - Contains special characters
    
    :param password: The password string to evaluate
    :return: Feedback on password strength
    """
    
    # Criteria checks
    length_criteria = len(password) >= 8
    lowercase_criteria = re.search(r'[a-z]', password) is not None
    uppercase_criteria = re.search(r'[A-Z]', password) is not None
    number_criteria = re.search(r'[0-9]', password) is not None
    special_char_criteria = re.search(r'[\W_]', password) is not None  # Special characters
    
    # Scoring the password
    score = 0
    feedback = []
    
    if length_criteria:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")
    
    if lowercase_criteria:
        score += 1
    else:
        feedback.append("Password should contain lowercase letters.")
    
    if uppercase_criteria:
        score += 1
    else:
        feedback.append("Password should contain uppercase letters.")
    
    if number_criteria:
        score += 1
    else:
        feedback.append("Password should contain numbers.")
    
    if special_char_criteria:
        score += 1
    else:
        feedback.append("Password should contain special characters.")
    
    # Password strength evaluation
    if score == 5:
        return "Strong password! Your password meets all criteria.", score
    elif score >= 3:
        return "Medium strength password. Consider improving the following:\n" + "\n".join(feedback), score
    else:
        return "Weak password. Please address the following:\n" + "\n".join(feedback), score

if __name__ == "__main__":
    print("Password Complexity Checker")
    password = input("Enter your password to check its strength: ")
    feedback, score = password_strength_checker(password)
    print(feedback)
