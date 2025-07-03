🎫 Ticket Booking System

A web-based booking and appointment management system built with **Django**, allowing users to register, log in, and book services with calendar and time-slot selection. Admins can manage users and monitor all bookings from the admin panel.

---

## 📸 Screenshots

> Place your screenshots in `assets/` folder

| Registration | Login | Dashboard |
|--------------|-------|-----------|
| ![Register](![Screenshot 2025-07-03 205920](https://github.com/user-attachments/assets/2aab7cc6-8577-4ddf-8cb2-9a89dfe22f4b)) |![Login](![Screenshot 2025-07-03 205910](https://github.com/user-attachments/assets/d242c24e-2cc0-4b91-839d-01566ce4c444)) |![Admin](![Screenshot 2025-07-03 205930](https://github.com/user-attachments/assets/6a689458-2f73-4bd4-8896-4f484dd69baf)) |![Dashboard](![Screenshot 2025-07-03 205939](https://github.com/user-attachments/assets/c45a6229-3c46-46fb-a6ac-9217eece31e2)) |

---

## 🚀 Features

- ✅ User registration & login
- ✅ Profile with photo upload
- ✅ Book tickets with calendar & time-slot selection
- ✅ Real-time booking calendar using FullCalendar.js
- ✅ Admin panel for managing users and bookings
- ✅ WebSocket-based notifications (configurable)

---

## 🛠️ Tech Stack

| Layer       | Tools/Frameworks                     |
|-------------|--------------------------------------|
| Frontend    | HTML, CSS, Bootstrap, FullCalendar.js|
| Backend     | Django 5.2, SQLite/PostgreSQL         |
| Real-Time   | Django Channels (WebSockets) *(opt)* |
| Auth        | Django Auth System                   |

---

## 📁 Project Structure
ticket_booking_system/
│
├── booking/ # Main app
│ ├── migrations/
│ ├── templates/booking/
│ │ ├── base.html
│ │ ├── dashboard.html
│ │ ├── login.html
│ │ └── register.html
│ ├── static/booking/
│ ├── forms.py
│ ├── models.py
│ ├── views.py
│ ├── urls.py
│ └── consumers.py # For WebSockets (if enabled)
│
├── config/ # Django settings project
│ ├── settings.py
│ ├── urls.py
│ └── asgi.py / wsgi.py
│
├── db.sqlite3
├── manage.py
└── README.md


---

## ⚙️ Installation

1. **Clone the repo**
git clone https://github.com/Abhaytiwari303/ticket_booking_system.git
cd ticket_booking_system

#Create & activate virtual environment
python -m venv venv
venv\Scripts\activate   # On Windows

#  Install requirements
pip install -r requirements.txt

# Migrate database
python manage.py makemigrations
python manage.py migrate

# Create superuser
python manage.py runserver

# Access app
Frontend: http://127.0.0.1:8000/
Admin:    http://127.0.0.1:8000/admin/

## API Endpoints
| URL                  | Description                    |
| -------------------- | ------------------------------ |
| `/register/`         | User registration              |
| `/login/`            | Login page                     |
| `/dashboard/`        | User dashboard + booking       |
| `/api/booked-slots/` | JSON for booked calendar slots |
| `/admin/`            | Django admin dashboard         |



