import random
import time
import requests

api_key = '194775dc6dd9f7b8f5f0e77f1733a330'
city_list = ['bangkok', 'mumbai', 'kolkata', 'tokyo', 'chennai', 'dhaka',
             'jaipur', 'beijing', 'delhi', 'punjab', 'pune', 'kashmir', 'lucknow', 'dubai', 'bangalore']

city = random.choice(city_list)

url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    # print(f'Current temperature in {city}: {data["main"]["temp"]}°C')
else:
    print(f'Error {response.status_code}: {response.reason}')

for i in data:
    print(f"{i} : {data[i]}")
# Measure the CPU fan noise for a certain period of time

def measure_noise():
    noise = []
    start_time = time.time()
    while time.time() - start_time < 5:  # measure for 5 seconds
        noise.append(random.random())
    return noise

# Use the CPU fan noise to generate random numbers

def generate_numbers():
    noise = measure_noise()
    random.seed(sum(noise))
    random_numbers = []
    for i in range(10):  # generate 10 random numbers
        random_numbers.append(random.random() * data["main"]["temp"] * data["wind"]["speed"])
    return random_numbers

# # Test the program
print(generate_numbers())
print(type(data["main"]["temp"]))
