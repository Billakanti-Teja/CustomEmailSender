from flask import Flask, request, jsonify
from app.models import db, Email
from app.tasks import send_email_task

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload_csv():
    # Parse and save emails
    pass

@app.route('/schedule', methods=['POST'])
def schedule_email():
    data = request.json
    email = Email(**data)
    db.session.add(email)
    db.session.commit()
    send_email_task.apply_async(args=[email.id], countdown=data.get('schedule_in', 0))
    return jsonify({"message": "Email scheduled!"})

@app.route('/analytics', methods=['GET'])
def get_analytics():
    # Fetch and return analytics
    pass
