from os import getcwd
import sounddevice
from scipy.io.wavfile import write
from queue import Queue
import threading
import time


class RecordingService(threading.Thread):
    def __init__(self, audio_segments: Queue, duration=10):
        threading.Thread.__init__(self)
        self.audio_segments = audio_segments
        self.duration = duration
        self.sample_rate = 44100

    def run(self):
        while True:
            print("Started Recording")
            recording = sounddevice.rec(
                frames=self.duration * self.sample_rate, samplerate=self.sample_rate, channels=1)
            sounddevice.wait()
            print("finished recording")

            filename = f"{getcwd()}\\audioFiles\\{time.time()}.wav"
            write(filename=filename, rate=self.sample_rate, data=recording)

            self.audio_segments.put(filename)
