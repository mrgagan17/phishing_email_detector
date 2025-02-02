def detect_phishing(email_text):  # Function to detect phishing emails based on common phishing keywords
    phishing_keywords = [
        "urgent", "click here", "verify your account",
        "password reset", "bank alert", "update your information", 
        "win a prize", "free gift", "suspended account"
    ]  # List of common phishing keywords used in scam emails

    # Convert email content to lowercase and check for phishing words
    for word in phishing_keywords:
        if word in email_text.lower():
            return "🧑‍💻💀 Warning: This email might be a phishing attempt!"
    
    return "✅ Safe Email."    # If no phishing keywords are found, the email is considered safe

if __name__ == "__main__":  # Main function to get user input and check for phishing
    email_content = input("Enter email content: ")
    print(detect_phishing(email_content))  # Call the detect_phishing function and print the result
