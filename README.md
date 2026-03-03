🛡️ AI Assessment Monitoring Logs Module
This module is part of the AI Interview and Assessment Monitoring System.
It implements structured logging for monitoring candidate activity during online assessments.

📌 Features
The system logs the following events:
✅ Question Start Time
✅ Question Submit Time
✅ Timer Expiry
✅ Suspicious Activity (Tab Switch Detection)
✅ Face Detection Events (Logging Layer)
✅ IP Address & User Agent Tracking
✅ Admin Monitoring Dashboard
✅ Summary Report API

🏗️ System Architecture
Frontend (React Assessment Page)
        ↓
FastAPI Backend (Logging API)
        ↓
PostgreSQL Database
        ↓
Admin Monitoring Dashboard

**🧰 Technologies Used**
**Backend**
FastAPI
SQLAlchemy
PostgreSQL
Pydantic
Uvicorn

**Frontend**
React.js
Fetch API

⚙️ Backend Setup Instructions
1️⃣ Clone the Repository
git clone https://github.com/shubham-3575/Assessment-Monitoring.git
cd ai_assessment_backend
2️⃣ Create Virtual Environment
python -m venv venv
Activate it:
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
Create a .env file in backend root:
DATABASE_URL=postgresql://username:password@localhost:5432/ai_assessment
Replace:
username → your PostgreSQL username
password → your PostgreSQL password
6️⃣ Run Backend Server
python -m uvicorn app.main:app --reload
Backend will start at:
http://127.0.0.1:8000
Swagger API Docs available at:
http://127.0.0.1:8000/docs

🎨 Frontend Setup Instructions
1️⃣ Go to Frontend Folder
cd ai_assessment_frontend
2️⃣ Install Dependencies
npm install
3️⃣ Start React App
npm start
Frontend runs at:
http://localhost:3000
🧪 How To Test The System
Option 1 – Automatic Logging
Open assessment page.
Refresh → QUESTION_START logs.
Switch tab → SUSPICIOUS_ACTIVITY logs.
Wait for timer → TIMER_EXPIRED logs.
Click submit → QUESTION_SUBMIT logs.
Option 2 – Using Swagger
Go to:
http://127.0.0.1:8000/docs
Use POST /log-event to manually add logs.
Option 3 – Admin Dashboard
Open frontend.
Enter Assessment ID (e.g., A202).
Click Fetch Logs.
Click Fetch Summary.
Admin dashboard will display:
Event timeline
Suspicious event count
Face detection events
Submission count

📊 API Endpoints
POST /log-event
Stores a monitoring event.
GET /logs/{assessment_id}
Fetch logs for a specific assessment.
GET /logs/{assessment_id}/summary
Returns summary statistics.

📌 Event Types (Enum)
The system supports these structured event types:
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
