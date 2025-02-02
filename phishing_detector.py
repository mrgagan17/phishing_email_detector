def detect_phishing(email_text):
    phishing_keywords = [
        "urgent", "click here", "verify your account",
        "password reset", "bank alert", "update your information",
        "win a prize", "free gift", "suspended account"
    ]
    
    for word in phishing_keywords:
        if word in email_text.lower():
            return "🧑‍💻💀 Warning: This email might be a phishing attempt!"
    
    return "✅ Safe Email."

if __name__ == "__main__":
    email_content = input("Enter email content: ")
    print(detect_phishing(email_content))
