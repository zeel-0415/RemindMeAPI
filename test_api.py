import requests

url = 'http://127.0.0.1:8000/api/reminders/'
data = {
'date': '2025-05-25',
'time': '14:30:00',
'message': 'Doctor appointment',
'reminder_type': 'EMAIL'
}
response = requests.post(url, json=data)
print(response.status_code, response.json())