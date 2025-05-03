import smtplib
import pandas as pd
import time
import random
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Load student data
df = pd.read_csv("students.csv")

# SMTP configuration
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
USERNAME = 'ahmedemran412@gmail.com'          # <- Your email address
PASSWORD = '---- ---- ---- ----'             # <- Use an app password, not your actual password

# Connect to SMTP
server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
server.starttls()
server.login(USERNAME, PASSWORD)

# Send personalized emails
for _, row in df.iterrows():
    name = row['name']
    recipient = row['email']
    course = row['course']

    # Build the email
    msg = MIMEMultipart()
    msg['From'] = USERNAME
    msg['To'] = recipient
    msg['Subject'] = f"Important update about your {course} course"

    body = f"""
    Hi {name},

    This is just a quick reminder regarding your {course} course.

    Please let us know if you have any questions.

    Best,
    Mahdi Hasan
    Your Course Coordinator
    """

    msg.attach(MIMEText(body, 'plain'))

    try:
        server.send_message(msg)
        print(f"✅ Email sent to {recipient}")
    except Exception as e:
        print(f"❌ Failed to send to {recipient}: {e}")

    # Human-like delay between emails
    delay = random.uniform(15, 60)
    print(f"Waiting {round(delay, 2)} seconds before next email...")
    time.sleep(delay)

server.quit()
