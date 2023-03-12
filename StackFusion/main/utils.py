from StackFusion.config import Config
import smtplib, ssl
from email.message import EmailMessage

def send_email(email):
    em = EmailMessage()
    em['From'] = Config.MAIL_USERNAME
    em['To'] = email
    em['Subject'] = "[Assignment] StackFusion Online Assignment for Full Stack Developer!"
    em.set_content("Congratulations!! You are now registered.")
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(Config.MAIL_SERVER, Config.MAIL_PORT, context=context) as smtp:
        smtp.login(Config.MAIL_USERNAME, Config.MAIL_PASSWORD)
        smtp.sendmail(Config.MAIL_USERNAME, email, em.as_string())
