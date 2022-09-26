import requests

url1 = 'https://moodle.gowercollegeswansea.ac.uk/login/index.php'
url2 = 'https://myeilp.gowercollegeswansea.ac.uk/myEILPTimetable.aspx'

payload = {
    'username': 'geu21866554',
    'password': 'M#gcS$y7hV'
}

# Create a new session
session = requests.Session()
session.post(url1, data=payload)
response = session.get(url2)

print(response.text)
