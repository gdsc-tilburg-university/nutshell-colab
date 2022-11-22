from os import getcwd, remove
import sounddevice
from scipy.io.wavfile import write
import whisper
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


class TranscriptionService(threading.Thread):
    def __init__(self, audio_segments: Queue, model="small.en"):
        threading.Thread.__init__(self)
        self.audio_segments = audio_segments
        self.model = whisper.load_model(model)

    def run(self):
        while True:
            filename = self.audio_segments.get()
            result = self.model.transcribe(filename)
            remove(filename)
            print(result.get("text"))
            self.audio_segments.task_done()


if __name__ == "__main__":
    audio_segments = Queue()

    recorder = RecordingService(audio_segments, duration=15)
    transcriber = TranscriptionService(audio_segments)

    recorder.start()
    transcriber.start()


# def record_audio(duration=10, sample_rate=44100):

#     recording = sounddevice.rec(
#         frames=duration * sample_rate, samplerate=sample_rate, channels=1)
#     print("Started Recording")

#     sounddevice.wait()
#     print("finished recording")

#     filename = f"{getcwd()}\\audio.wav"
#     write(filename=filename, rate=sample_rate, data=recording)

#     return filename


# def transcribe_audio(filename: str):
#     model = whisper.load_model("base")
#     result = model.transcribe(filename)
#     return result.get("text")


# audio_file = record_audio()
# transcription = transcribe_audio(audio_file)

# print(transcription)
