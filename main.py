import requests

r = requests.get('https://www.python.org')

print(r.text)
print(r.status_code)
