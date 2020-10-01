import sounddevice
from scipy.io.wavfile import write
fs=44100 #sample_rate
second=int(input("Enter the time duration in second: ")) #enter your required time..
print("Recording....\n")
record_voice=sounddevice.rec(int(second * fs),samplerate=fs,channels=2)
sounddevice.wait()
print("Finished...\ncheck in the given folder.")
write("Plese provide your reuired folder path..",fs,record_voice) # output will be shown.