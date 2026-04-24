import os
import requests
import random
import re

api_key = os.getenv('OPENWEATHER_API_KEY')

if not api_key:
    print('Error: OPENWEATHER_API_KEY environment variable is not set')
    exit(1)

# Validate API key format to prevent injection attacks
if not re.match(r'^[a-zA-Z0-9_-]+$', api_key):
    print('Error: Invalid API key format')
    exit(1)

city_list = ['bangkok', 'mumbai', 'kolkata', 'tokyo', 'chennai', 'dhaka', 
            'jaipur', 'beijing', 'delhi', 'punjab', 'pune', 'kashmir', 'lucknow', 'dubai', 'bangalore']

city = random.choice(city_list)

# Validate city name doesn't contain special characters
if not re.match(r'^[a-zA-Z0-9_-]+$', city):
    print('Error: Invalid city name')
    exit(1)

url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
response = requests.get(url, timeout=10)

if response.status_code == 200:
    data = response.json()
    # Check if required fields exist before accessing them
    if 'main' in data and 'temp' in data['main']:
        print(f'Current temperature in {city}: {data["main"]["temp"]}°C')
    else:
        print('Error: Unable to fetch weather data')
else:
    print(f'Error {response.status_code}: Unable to fetch weather data')