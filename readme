# RemindMeAPI

A lightweight Django REST API for scheduling reminders with email or SMS notifications. Create and manage reminders effortlessly using a simple POST endpoint, with data stored in a SQLite database. Ideal for developers building front-end applications or automation workflows.

## Features
- **Simple API**: Create reminders with a single POST request.
- **Flexible Notifications**: Support for `EMAIL` or `SMS` reminder types.
- **Lightweight Backend**: Uses SQLite for easy setup and minimal dependencies.
- **Admin Interface**: Manage reminders via Django’s built-in admin panel.
- **Developer-Friendly**: Clear documentation and easy integration.

## Tech Stack
- **Backend**: Django 4.2.16, Django REST Framework 3.15.2
- **Database**: SQLite
- **Python**: 3.8+
- **OS**: Windows (tested), Linux, macOS (compatible)

## Getting Started

### Prerequisites
- Python 3.8 or higher
- Git
- PowerShell (for Windows) or terminal (for Linux/macOS)

### Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/RemindMeAPI.git
   cd RemindMeAPI


Set Up Virtual Environment:
python -m venv venv
.\venv\Scripts\Activate.ps1  # Windows
# source venv/bin/activate  # Linux/macOS


Install Dependencies:
pip install -r requirements.txt


Run Migrations:
python manage.py makemigrations
python manage.py migrate


Create Superuser (Optional):
python manage.py createsuperuser


Start the Development Server:
python manage.py runserver

The API will be available at http://127.0.0.1:8000/api/reminders/, and the admin interface at http://127.0.0.1:8000/admin/.


Alternative Setup
Use the provided setup.ps1 script (Windows only) to automate the setup:
.\setup.ps1

API Usage
Endpoint

URL: http://127.0.0.1:8000/api/reminders/
Method: POST
Content-Type: application/json

Request Body
{
    "date": "2025-05-25",
    "time": "14:30:00",
    "message": "Doctor appointment",
    "reminder_type": "EMAIL"
}


Fields:
date: Date in YYYY-MM-DD format.
time: Time in HH:MM:SS format (24-hour).
message: Reminder description (string).
reminder_type: Either EMAIL or SMS.



Example Request
curl -X POST http://127.0.0.1:8000/api/reminders/ -H "Content-Type: application/json" -d '{"date":"2025-05-25","time":"14:30:00","message":"Doctor appointment","reminder_type":"EMAIL"}'

Example Response (HTTP 201)
{
    "date": "2025-05-25",
    "time": "14:30:00",
    "message": "Doctor appointment",
    "reminder_type": "EMAIL"
}

Testing with Python
Use the included test_api.py script:
pip install requests
python test_api.py

Admin Interface

URL: http://127.0.0.1:8000/admin/
Log in with the superuser credentials created during setup.
View and manage reminders in the "Reminders" section.

Project Structure
RemindMeAPI/
├── manage.py
├── requirements.txt
├── setup.ps1
├── test_api.py
├── db.sqlite3
├── remind_me_later/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   ├── wsgi.py
├── reminders/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations/
│   ├── models.py
│   ├── serializers.py
│   ├── urls.py
│   ├── views.py


