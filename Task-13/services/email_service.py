import smtplib
from email.message import EmailMessage
from config import EMAIL_CONFIG

def send_email(to_list, subject, body, attachment_path):
    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = EMAIL_CONFIG["sender"]
    msg["To"] = "mohamedabubakkar.s2022ai-ds@sece.ac.in"

    msg.set_content(body)

    with open(attachment_path, "rb") as f:
        msg.add_attachment(f.read(), maintype="application", subtype="pdf", filename=attachment_path.name)

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(EMAIL_CONFIG["sender"], EMAIL_CONFIG["password"])
        server.send_message(msg)