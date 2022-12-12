from email.message import EmailMessage
import ssl
import smtplib
import my_config as mc

def send_my_email():
    """Sends an email"""

    email_sender = mc.SENDER
    email_password = mc.SENDER_PW
    email_receiver = mc.RECEIVER

    subject = "Water your plants!"
    body = """
    The plants in your living room are in dire need of water.
    """

    em = EmailMessage()
    em["From"] = email_sender
    em["To"] = email_receiver
    em["subject"] = subject
    em.set_content(body)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, em.as_string())