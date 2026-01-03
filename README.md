# 🩺 Medical Booking API

A Django + Django REST Framework project for managing medical appointments, users, and notifications.  
Built with role‑based access (Admin, Doctor, Patient) and seeded demo data for easy testing.

---

## 🚀 Features
- JWT authentication with role‑based access
- Admin, Doctor, and Patient user roles
- Appointment scheduling and status tracking
- Notification system (appointment reminders)
- Seed command for demo data
- Thunder Client collection for quick API testing

---

## 📦 Setup

Clone the repo and install dependencies:

```bash
git clone <your-repo-url>
cd medical-booking-clean
pip install -r requirements.txt
Run migrations and seed demo data:

bash
python manage.py migrate
python manage.py seed_demo
python manage.py runserver
👤 Demo Accounts
Role	Username	Password
Admin	admin	admin123
Doctor	dr_1..dr_3	test123
Patient	patient_1..patient_5	test123
🔑 Authentication
Obtain a JWT token:

http
POST /api/token/
Content-Type: application/json

{
  "username": "admin",
  "password": "admin123"
}
Use the access token in headers:

Code
Authorization: Bearer <your_access_token>
📡 API Endpoints
Users
GET /users/ → list all users

GET /users/?role=doctor → filter doctors

GET /users/?role=patient → filter patients

GET /users/{id}/ → retrieve single user

PUT /users/{id}/ → update user (admin only)

DELETE /users/{id}/ → delete user (admin only)

Appointments
GET /appointments/ → list appointments

POST /appointments/ → create appointment

GET /appointments/{id}/ → retrieve appointment

PATCH /appointments/{id}/ → update status

DELETE /appointments/{id}/ → cancel appointment

Notifications
GET /notifications/ → list notifications

PATCH /notifications/{id}/ → mark as read

DELETE /notifications/{id}/ → delete notification



🎥 Loom Demo Checklist
When recording for mentors:

Show repo structure and models.

Run seed_demo and show seeded data in Django Admin.

Demonstrate JWT login in Thunder Client.

Show role‑based access:

Doctor → sees only their patients’ appointments.

Patient → sees only their own appointment.

Admin → sees everything.

Walk through endpoints with headers set.

🛠 Tech Stack
Django

Django REST Framework

SimpleJWT

SQLite (dev)

📖 Notes
All endpoints require JWT authentication.

Seed command ensures reproducible demo data.

Thunder Client collection makes mentor testing seamless.

Code

---

This README is **mentor‑ready**: it explains setup, accounts, endpoints, and demo flow in a clean, professional way.  
