📚 Student Teacher Appointment System

This project helps students schedule appointments with teachers for guidance, project discussions, and academic support. It streamlines the communication process between students and teachers with a user-friendly interface and a secure backend API.

🚀 Tech Stack

Frontend: HTML, CSS, JavaScript, ReactJS

Backend: Python, Django REST Framework (DRF)

API: REST API with JWT Authentication

🎯 Features

🔑 Authentication: Secure Login, Logout, and Registration

👨‍🎓 Student Dashboard: Book and manage appointments with teachers

👨‍🏫 Teacher Dashboard: View and manage student appointment requests

🔄 DRF API: Token-based authentication (Access & Refresh tokens)

🖼️ Screenshots
1️⃣ Registration Page

Allows new users (students/teachers) to register into the system.

<img width="1920" height="1007" alt="Registration Page" src="https://github.com/user-attachments/assets/b60d5bdb-8350-415d-a19b-1dbccf5733e6" />
2️⃣ Login Page

Users can log in securely using their credentials.

<img width="1920" height="1017" alt="Login Page" src="https://github.com/user-attachments/assets/9edf999f-f767-48fa-9e58-80247b2e7b8d" />
3️⃣ Student Appointment Page

Students can book an appointment with available teachers.

<img width="1920" height="1080" alt="Student Appointment Page" src="https://github.com/user-attachments/assets/8364c23e-5b6c-47a6-ac92-802fec344af5" />
4️⃣ DRF API Backend

The backend is powered by Django REST Framework with JWT Authentication.

<img width="1920" height="1080" alt="DRF API Backend" src="https://github.com/user-attachments/assets/74c0dfe3-c2ed-4e94-91fe-1b862308b378" />
⚙️ Installation & Setup
1. Clone the repository
git clone https://github.com/<your-username>/student-teacher-appointment.git
cd student-teacher-appointment

2. Backend Setup (Django + DRF)
cd backend
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

3. Frontend Setup (React)
cd frontend
npm install
npm start
