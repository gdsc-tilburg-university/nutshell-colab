import sounddevice
from os import getcwd
from scipy.io.wavfile import write

duration = 10
sample_rate = 44100

recording = sounddevice.rec(
    frames=duration * sample_rate, samplerate=sample_rate, channels=1)
print("Started Recording")

sounddevice.wait()
print("finished recording")

filename = f"{getcwd()}\\audio.wav"

write(filename=filename, rate=sample_rate, data=recording)
