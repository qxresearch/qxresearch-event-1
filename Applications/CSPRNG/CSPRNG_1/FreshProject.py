import os
import random
import time
import requests
from urllib.parse import quote

api_key = os.getenv('OPENWEATHER_API_KEY')

if not api_key:
    print("Error: OPENWEATHER_API_KEY environment variable is not set.")
    exit(1)

city_list = ['bangkok', 'mumbai', 'kolkata', 'tokyo', 'chennai', 'dhaka',
             'jaipur', 'beijing', 'delhi', 'punjab', 'pune', 'kashmir', 'lucknow', 'dubai', 'bangalore']

city = random.choice(city_list)

# Validate city name before using in URL
if not isinstance(city, str) or len(city) == 0:
    print("Error: Invalid city name.")
    exit(1)

# Properly encode city name for URL safety to prevent injection
encoded_city = quote(city.lower())

url = f'http://api.openweathermap.org/data/2.5/weather?q={encoded_city}&appid={api_key}&units=metric'
response = requests.get(url, timeout=10)

if response.status_code == 200:
    data = response.json()
else:
    print(f'Error {response.status_code}: {response.reason}')
    exit(1)

for key in data:
    print(f"{key} : {data[key]}")

def measure_noise():
    noise = []
    start_time = time.time()
    while time.time() - start_time < 5:
        noise.append(random.random())
    return noise

def generate_numbers(data):
    noise = measure_noise()
    random.seed(sum(noise))
    random_numbers = []
    if "main" in data and "wind" in data:
        temp = data["main"].get("temp", 0)
        speed = data["wind"].get("speed", 0)
        for i in range(10):
            random_numbers.append(random.random() * temp * speed)
    return random_numbers

# Test the program
print(generate_numbers(data))

if "main" in data and isinstance(data.get("main", {}), dict) and "temp" in data["main"]:
    print(type(data["main"]["temp"]))