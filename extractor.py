import re

# 📂 Step 1: Read file
with open("input.txt", "r", encoding="utf-8") as file:
    text = file.read()

# 🔍 Step 2: Extract emails using regex
emails = re.findall(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+', text)

# 🧹 Step 3: Remove duplicates (important upgrade)
unique_emails = sorted(set(emails))

# 📁 Step 4: Save results nicely
with open("emails.txt", "w", encoding="utf-8") as file:
    file.write("EXTRACTED EMAILS\n")
    file.write("=" * 30 + "\n")
    
    for email in unique_emails:
        file.write(email + "\n")

# 📊 Step 5: Print summary
print("✅ Email Extraction Completed!")
print(f"📧 Total Emails Found: {len(emails)}")
print(f"🧹 Unique Emails Saved: {len(unique_emails)}")

print("\n📌 Emails List:")
for email in unique_emails:
    print(" -", email)