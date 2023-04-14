import requests
import random
api_key = '194775dc6dd9f7b8f5f0e77f1733a330'

city_list = ['bangkok', 'mumbai', 'kolkata', 'tokyo', 'chennai', 'dhaka', 
            'jaipur', 'beijing', 'delhi', 'punjab', 'pune', 'kashmir', 'lucknow', 'dubai', 'bangalore']

city = random.choice(city_list)

url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(f'Current temperature in {city}: {(data["main"]["temp"])}°C')
else:
    print(f'Error {response.status_code}: {response.reason}')