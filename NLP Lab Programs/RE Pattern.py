import re

text = """
Name: John Doe
Email: john.doe123@gmail.com
Mobile: +91-9876543210
Password: P@ssw0rd123
Date of Birth: 15/08/2004
Register Number: 23AIML1056
Department: Artificial Intelligence and Machine Learning
"""

email_pattern = r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.(com|org|edu|in)'
mobile_pattern = r'\+91-\d{10}'
password_pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@#$%&!*])[A-Za-z\d@#$%&!*]{8,}$'
dob_pattern = r'\d{2}/\d{2}/\d{4}'
reg_pattern = r'\d{2}[A-Z]{4}\d{4}'

print("Email:", re.search(email_pattern, text).group())
print("Mobile:", re.search(mobile_pattern, text).group())
print("DOB:", re.search(dob_pattern, text).group())
print("Register Number:", re.search(reg_pattern, text).group())

password = "P@ssw0rd123"

if re.match(password_pattern, password):
    print("Password: Valid")
else:
    print("Password: Invalid")
    
