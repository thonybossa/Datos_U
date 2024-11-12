import requests

url = "https://www.datos.gov.co/resource/n4dj-8r7k.json"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f"Failed to retrieve data: {response.status_code}")