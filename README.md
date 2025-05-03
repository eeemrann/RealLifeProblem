
## Human-Like Email Sender (Python)

A tiny Python project to send **50+ personalized emails** without landing in spam — by mimicking how a real human would send them.  
Minimal code, real-world value.

---

## Problem Statement

Traditional methods like **Mail Merge** or using bulk email services often:
- Trigger spam filters
- Send all emails at once (unnaturally fast)
- Lack of personalization
- Rely on external platforms or APIs

Deliverability and a natural human touch are critical when sending academic or personal updates to 50+ students.

---

## My Solution

This project uses a **simple Python script** to:
- Read recipient data from a CSV file
- Personalize each email (name, course, etc.)
- Send emails **one at a time**, with **random delays**
- Use a real SMTP server (like Gmail) with secure app passwords
- Avoid spam triggers by using natural language, plain-text emails, and human-like timing

---

## Features
- 🧍 Human-like delay (`15–60s`) between emails
- ✉️ Personalized subjects and bodies
- 📄 Reads from `students.csv`
- 🔐 Works with Gmail (via app password)
- 🛑 Easily interruptable via `Ctrl + C`
- ✅ Spam-safe — verified in real use

---

## Example CSV (`students.csv`)
```csv
name, email, course
Alice Johnson,alice@example.com, Mathematics
Bob Smith,bob@example.com, Physics
...
```

---

## How It Works

```bash
# Install required packages
pip install pandas
```

Run the script:

```bash
python send_emails.py
```

The script will:
- Read each row from `students.csv`
- Send a customized email to that student
- Wait 15–60 seconds before sending the next

---

## Gmail App Password Setup

To use Gmail:
1. Enable **2-Step Verification** in your Google account
2. Go to [App Passwords](https://myaccount.google.com/apppasswords)
3. Generate a password for "Mail" > "Other (Python Script)"
4. Use that 16-character password in the script instead of your real Gmail password

---

## To Stop the Script

Press `Ctrl + C` at any time. The script handles it gracefully.

---

## File Structure

```
.
├── send_emails.py    # Main script
├── students.csv      # Recipient data
└── README.md         # Project documentation
```

---

## Best Practices
- Never hardcode credentials in scripts (use `.env` files or input prompts)
- Always test with a few emails before running at scale
- Warm up your email account before sending hundreds of emails/day

---

## Future Improvements
- Add HTML email support
- Support multiple SMTP providers (SendGrid, Mailgun)
- Track open/click metrics
- GUI wrapper for non-coders

---

## UI Preview

https://github.com/user-attachments/assets/6ec32253-caec-4fd1-a2c9-f6b204b973af


