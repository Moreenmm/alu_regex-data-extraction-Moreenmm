import re
import json

#Reading the sample_input.txt file
with open("sample_input.txt", "r") as file:
    data = file.read()

# -----------------------------
#THE  REGEX PATTERNS

email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'
phone_pattern = r'(\+\d{1,3}[- ]?)?\(?\d{2,4}\)?[- ]?\d{3}[- ]?\d{4}'
date_pattern = r'\b(\d{4}-\d{2}-\d{2}|\d{2}/\d{2}/\d{4})\b'
credit_card_pattern = r'\b\d{4}-\d{4}-\d{4}-\d{4}\b'

# -----------------------------
#EXTRACTION OF DATA

emails = re.findall(email_pattern, data)
phones = re.findall(phone_pattern, data)
dates = re.findall(date_pattern, data)
credit_cards = re.findall(credit_card_pattern, data)

# -----------------------------
#SECURITY HANDLING
#Masking the credit cards except for the last 4 digits


masked_cards = [
    "****-****-****-" + card[-4:]
    for card in credit_cards
]

# -----------------------------
#THE  STRUCTURED OUTPUT


output = {
    "emails": emails,
    "phone_numbers": phones,
    "dates": dates,
    "credit_cards_masked": masked_cards
}

#Saving the output in the sample_output.json file
with open("sample_output.json", "w") as file:
    json.dump(output, file, indent=4)

print("Kudos!! You data has been extracted successfully!")

