📝 Full-Stack To-Do List App

A modern full-stack To-Do List application with a React frontend and Flask + SQLite backend, featuring task creation, deletion, completion toggling, reminders, and due dates. The app is Dockerized for easy deployment and runs locally on your machine.

🚀 Features

Add Tasks – Create new tasks with title, description, due date, and optional reminder.

View Tasks – See a list of all tasks.

Toggle Completion – Mark tasks as completed or incomplete.

Delete Tasks – Remove tasks permanently.

Persistent Storage – Uses SQLite database via Flask-SQLAlchemy.

CORS Enabled – Frontend communicates smoothly with backend.

Docker Support – Run the entire app using Docker Compose.

🛠 Tech Stack
Layer	Technology
Frontend	React.js
Backend	Python Flask
Database	SQLite (via SQLAlchemy)
API	REST API (GET, POST, DELETE, PATCH)
Styling	CSS (Custom)
Container	Docker + Docker Compose

⚡ Installation & Setup (Local)
1️⃣ Clone the repository
git clone <your-repo-url>
cd todo

2️⃣ Backend Setup

cd backend

Create a virtual environment (recommended):

python -m venv venv
venv\Scripts\activate     # Windows
source venv/bin/activate  # macOS/Linux


Install dependencies:

pip install -r requirements.txt

Run Flask backend:

python app.py


Backend runs at: http://localhost:5000

3️⃣ Frontend Setup

Navigate to frontend folder:

cd ../frontend


Install dependencies:

npm install


Start React app:

npm start


Frontend runs at: http://localhost:3000

🐳 Using Docker Compose

Build and run both frontend and backend using Docker:

docker-compose up --build

Demo Vedio:
Youtube link: https://youtu.be/T-NRZCkTxak