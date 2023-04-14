import pyaudio
import wave

# set the chunk size and recording format
chunk = 1024
format = pyaudio.paInt16
channels = 1
rate = 44100
record_seconds = 5
output_filename = "output.wav"

# create a PyAudio object
p = pyaudio.PyAudio()

# open the microphone and start recording
stream = p.open(format=format, channels=channels, rate=rate, input=True, frames_per_buffer=chunk)
frames = []
for i in range(0, int(rate / chunk * record_seconds)):
    data = stream.read(chunk)
    frames.append(data)

# stop recording and close the stream
stream.stop_stream()
stream.close()
p.terminate()

# save the recorded audio to a WAV file
wf = wave.open(output_filename, 'wb')
wf.setnchannels(channels)
wf.setsampwidth(p.get_sample_size(format))
wf.setframerate(rate)
wf.writeframes(b''.join(frames))
wf.close()
