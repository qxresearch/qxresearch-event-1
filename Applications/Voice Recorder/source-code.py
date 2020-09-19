import sounddevice
from scipy.io.wavfile import write
fs=44100 #sample_rate
seconds=10
print("recording...")
record_voice=sounddevice.rec(int(seconds * fs),samplerate=fs,channels=2)
sounddevice.wait()
write("out.wav",fs,record_voice)
