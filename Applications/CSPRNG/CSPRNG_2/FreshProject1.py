import pyaudio
import struct
import random

import requests
api_key = '194775dc6dd9f7b8f5f0e77f1733a330'

city_list = ['bangkok', 'mumbai', 'kolkata', 'tokyo', 'chennai', 'dhaka', 
            'jaipur', 'beijing', 'delhi', 'punjab', 'pune', 'kashmir', 'lucknow', 'dubai', 'bangalore']

city = random.choice(city_list)

url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
response = requests.get(url)

if response.status_code == 200:
    info = response.json()
    # print(f'Current temperature in {city}: {data["main"]["temp"]}°C')
else:
    print(f'Error {response.status_code}: {response.reason}')


# set the chunk size and recording format
chunk = 1024
format = pyaudio.paInt16
channels = 1
rate = 44100
record_seconds = 5

# create a PyAudio object
p = pyaudio.PyAudio()

# open the microphone and start recording
stream = p.open(format=format, channels=channels, rate=rate, input=True, frames_per_buffer=chunk)
frames = []
for i in range(0, int(rate / chunk * record_seconds)):
    data = stream.read(chunk)
    frames.append(data)

# print(frames)

# stop recording and close the stream
stream.stop_stream()
stream.close()
p.terminate()

# process the recorded audio to generate random numbers
random_numbers = []
for frame in frames:
    # unpack the audio data to get the amplitude values
    amplitude_values = struct.unpack(str(2 * chunk) + 'B', frame)
    # print(amplitude_values)
    # generate a random number based on the amplitude values
    random_number = sum(amplitude_values) % 100 
    temp = int(info["main"]["temp"])
    random_numbers.append(random_number * temp)

# print the generated random numbers
print(random_numbers)
