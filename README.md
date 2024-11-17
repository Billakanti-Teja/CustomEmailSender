# Custom Email Sender

## Overview
The **Custom Email Sender** is a powerful tool for managing and sending personalized emails. It allows users to:
- Upload email recipient data through CSV files.
- Customize email content dynamically using placeholders.
- Schedule emails and manage delivery throttling.
- Track real-time analytics, including sent, pending, and failed emails.

The application is built with a **React.js frontend** and a **Flask backend**, using **Celery** for task scheduling and **Redis** as the message broker.

---

## Features
- **Upload CSV Files:** Easily upload a list of recipients and email details.
- **Dynamic Email Content:** Use placeholders (e.g., `{recipient_name}`) to create personalized emails.
- **Scheduling and Throttling:** Schedule emails for specific times and manage the sending rate to comply with limits.
- **Real-Time Analytics:** Monitor email statuses (Sent, Pending, Failed) through a dashboard.
- **Email Delivery Tracking:** Track email delivery using SMTP or ESP integration.

---

## Tech Stack
### Frontend
- React.js
- Axios
- Material-UI

### Backend
- Flask
- Flask-CORS
- Flask-SQLAlchemy
- Celery
- Redis

### Database
- SQLite (default, can be replaced with PostgreSQL or MySQL)

### Task Queue
- Celery with Redis

---

## Installation

### Prerequisites
- Python 3.8+
- Node.js 14+
- Redis server
- SQLite (default) or a configured database like PostgreSQL/MySQL

---

### 1. Backend Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/custom-email-sender.git
   cd custom-email-sender/backend

2. Install dependencies:
   ```bash
   pip install -r requirements.txt

3. Configure the database in config.py (default is SQLite):
   ```bash
   SQLALCHEMY_DATABASE_URI = "sqlite:///emails.db"

4. Start the Flask server:
   ```bash
   flask run

5. Start the Celery worker:
   ```bash
   celery -A app.tasks.celery worker --loglevel=info

### 2. Frontend Setup
1. Navigate to the frontend directory2:
   ```bash
   cd ../frontend

2. Install dependencies:
   ```bash
   npm install

3. Start the React development server:
   ```bash
   npm start

### 3. Usage:<br>
-Open the application in your browser (default: http://localhost:3000).<br>
-Upload a CSV file with email recipient details.<br>
-Customize your email content using placeholders.<br>
-Schedule emails or send them immediately.<br>
-Monitor email statuses in real-time on the dashboard.

   



