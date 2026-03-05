# 🛡️ AI Assessment Monitoring Logs Module

This module is part of the **AI Interview and Assessment Monitoring System**.  
It implements **structured logging** for monitoring candidate activity during online assessments.

---

# 📌 Features

The system logs the following events:

- ✅ Question Start Time
- ✅ Question Submit Time
- ✅ Timer Expiry
- ✅ Suspicious Activity (Tab Switch Detection)
- ✅ Face Detection Events (Logging Layer)
- ✅ IP Address & User Agent Tracking
- ✅ Admin Monitoring Dashboard
- ✅ Summary Report API

---

# 🏗️ System Architecture


Frontend (React Assessment Page)
↓
FastAPI Backend (Logging API)
↓
PostgreSQL Database
↓
Admin Monitoring Dashboard


---

# 🧰 Technologies Used

## Backend
- FastAPI
- SQLAlchemy
- PostgreSQL
- Pydantic
- Uvicorn

## Frontend
- React.js
- Fetch API

---

# ⚙️ Backend Setup Instructions

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/shubham-3575/Assessment-Monitoring.git
cd ai_assessment_backend
2️⃣ Create Virtual Environment
python -m venv venv

Activate the environment:

Windows (PowerShell)
.\venv\Scripts\Activate.ps1
Windows (CMD)
venv\Scripts\activate
3️⃣ Install Dependencies
pip install -r requirements.txt
4️⃣ Setup PostgreSQL

Install PostgreSQL from:

https://www.postgresql.org/download/

Create a database:

CREATE DATABASE ai_assessment;
5️⃣ Configure Environment Variables

Create a .env file in the backend root folder:

DATABASE_URL=postgresql://username:password@localhost:5432/ai_assessment

Replace:

username → your PostgreSQL username

password → your PostgreSQL password

6️⃣ Run Backend Server
python -m uvicorn app.main:app --reload

Backend will start at:

http://127.0.0.1:8000

Swagger API documentation:

http://127.0.0.1:8000/docs
🎨 Frontend Setup Instructions
1️⃣ Go to Frontend Folder
cd ai_assessment_frontend
2️⃣ Install Dependencies
npm install
3️⃣ Start React Application
npm start

Frontend runs at:

http://localhost:3000
🧪 How To Test The System
Option 1 — Automatic Logging

Open the assessment page.

Refresh the page → QUESTION_START is logged.

Switch browser tab → SUSPICIOUS_ACTIVITY is logged.

Wait for timer → TIMER_EXPIRED is logged.

Click submit → QUESTION_SUBMIT is logged.

Option 2 — Using Swagger API

Go to:

http://127.0.0.1:8000/docs

Use the endpoint:

POST /log-event

to manually add monitoring logs.

Option 3 — Admin Dashboard

Open the frontend application.

Enter an Assessment ID (example: A202).

Click Fetch Logs.

Click Fetch Summary.

The dashboard will display:

Event timeline

Suspicious activity count

Face detection events

Question submission statistics

📊 API Endpoints
POST /log-event

Stores a monitoring event.

GET /logs/{assessment_id}

Fetch logs for a specific assessment.

GET /logs/{assessment_id}/summary

Returns summary statistics for the assessment.

📌 Event Types (Enum)

The system supports the following structured event types:

QUESTION_START

QUESTION_SUBMIT

TIMER_EXPIRED

SUSPICIOUS_ACTIVITY

FACE_DETECTED

MULTIPLE_FACE

FACE_NOT_VISIBLE

🎯 Purpose of This Module

This module ensures:

Fairness in online assessments

Monitoring transparency

Structured audit trail

Admin-level reporting

👨‍💻 Developed By

Shubham Patel
Assessment Monitoring Logs Module
