import requests
requests = requests.post('http://127.0.0.1:5000/hello', data={'name': 'Fabel'})
print(response.text)