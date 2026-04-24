import os
import pyaudio
import struct
import random
import re

import requests
api_key = os.getenv('OPENWEATHER_API_KEY', '')

# Validate API key before making requests
if not api_key or len(api_key) == 0:
    print("Warning: OPENWEATHER_API_KEY is not set. Using mock data.")
    info = {"main": {"temp": 25}}
else:
    # Additional validation for API key format to prevent credential exposure
    if not re.match(r'^[a-zA-Z0-9_-]+$', api_key):
        print("Warning: Invalid API key format. Using mock data.")
        info = {"main": {"temp": 25}}
    else:
        city_list = ['bangkok', 'mumbai', 'kolkata', 'tokyo', 'chennai', 'dhaka', 
                    'jaipur', 'beijing', 'delhi', 'punjab', 'pune', 'kashmir', 'lucknow', 'dubai', 'bangalore']
        
        city = random.choice(city_list)
        
        # Sanitize city parameter to prevent URL injection
        sanitized_city = re.sub(r'[^\w\s-]', '', city).strip()
        
        url = f'http://api.openweathermap.org/data/2.5/weather?q={sanitized_city}&appid={api_key}&units=metric'
        
        try:
            response = requests.get(url, timeout=10)
            
            if response.status_code == 200:
                info = response.json()
            else:
                print(f'Error {response.status_code}')
                info = {"main": {"temp": 25}}
        except requests.RequestException as e:
            print('Request failed')
            info = {"main": {"temp": 25}}

# set the chunk size and recording format
chunk = 1024
format = pyaudio.paInt16
channels = 1
rate = 44100
record_seconds = 5

# create a PyAudio object with proper error handling
try:
    p = pyaudio.PyAudio()
    
    # open the microphone and start recording with error handling
    try:
        stream = p.open(format=format, channels=channels, rate=rate, input=True, frames_per_buffer=chunk)
        
        frames = []
        for i in range(0, int(rate / chunk * record_seconds)):
            data = stream.read(chunk, exception_on_overflow=False)
            frames.append(data)
        
        # stop recording and close the stream properly
        stream.stop_stream()
        stream.close()
    except Exception as e:
        print('Microphone access failed')
        frames = []
    
    p.terminate()
except Exception as e:
    print('PyAudio initialization failed')
    frames = []

# process the recorded audio to generate random numbers
random_numbers = []
if len(frames) > 0 and info is not None:
    for frame in frames:
        # unpack the audio data to get the amplitude values
        try:
            amplitude_values = struct.unpack(str(2 * chunk) + 'B', frame)
            # generate a random number based on the amplitude values
            random_number = sum(amplitude_values) % 100 
            temp = int(info["main"]["temp"]) if "main" in