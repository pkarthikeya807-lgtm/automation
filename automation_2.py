import os
import re

INPUT_FILE = "raw_data.txt"
OUTPUT_FILE = "extracted_emails.txt"

def extract_emails():
    if not os.path.exists(INPUT_FILE):
        print(f"Error: {INPUT_FILE} does not exist.")
        return

    with open(INPUT_FILE, "r", encoding="utf-8") as file:
        content = file.read()

    email_regex = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
    all_emails = re.findall(email_regex, content)
    unique_emails = sorted(list(set(all_emails)))

    if unique_emails:
        with open(OUTPUT_FILE, "w", encoding="utf-8") as output:
            for email in unique_emails:
                output.write(email + "\n")
        print(f"Extracted {len(unique_emails)} emails to {OUTPUT_FILE}")
    else:
        print("No emails found.")

if __name__ == "__main__":
    extract_emails()