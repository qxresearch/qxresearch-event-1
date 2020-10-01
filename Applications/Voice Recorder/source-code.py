import sounddevice
from scipy.io.wavfile import write
fs=44100 #sample_rate
second=int(input("Enter the time duration in second: ")) #enter your required time..
print("Recording....\n")
record_voice=sounddevice.rec(int(second * fs),samplerate=fs,channels=2)
sounddevice.wait()
print("Finished...\nPlease Check it...")
write("out.wav",fs,record_voice)