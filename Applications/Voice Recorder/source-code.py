import sounddevice as sd
from scipy.io.wavfile import write
import datetime
import time

fs = 44100  # Sample rate

try:
    seconds = int(input("Enter recording duration (in seconds): "))
    
    if seconds <= 0:
        print("❌ Invalid input! Please enter a positive number.")
        exit()

    channels = int(input("Enter channels (1 = Mono, 2 = Stereo): "))
    if channels not in [1, 2]:
        print("❌ Invalid channel choice! Using default stereo (2).")
        channels = 2

    print("⏳ Recording will start in 3 seconds...")
    time.sleep(3)

    filename = f"recording_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.wav"

    print("🎤 Recording...")
    recording = sd.rec(int(seconds * fs), samplerate=fs, channels=channels)
    sd.wait()

    write(filename, fs, recording)

    print(f"✅ Finished! File saved as: {filename}")

except ValueError:
    print("❌ Please enter valid numeric input!")
except Exception as e:
    print("❌ Error:", e)