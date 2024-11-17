from celery import Celery
from app.models import db, Email
import smtplib

celery = Celery(__name__)

@celery.task
def send_email_task(email_id):
    email = Email.query.get(email_id)
    try:
        # Replace with actual email-sending logic
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login("your_email@gmail.com", "app_password")
        server.sendmail("your_email@gmail.com", email.recipient, email.content)
        server.quit()
        email.status = "Sent"
    except Exception as e:
        email.status = f"Failed: {e}"
    db.session.commit()
