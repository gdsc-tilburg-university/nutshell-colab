import sounddevice as sd
from os import getcwd
from scipy.io.wavfile import write
import whisper

import threading
from queue import Queue
import time

class RecordingService(threading.Thread):
    def __init__(self, audio_segments):
        threading.Thread.__init__(self)
        self.audio_segments = audio_segments

    def run(self):
        while True:
            self.audio_segments.put(time.time())
            time.sleep(1)

class TranscriptionService(threading.Thread):
    def __init__(self, audio_segments):
        threading.Thread.__init__(self)
        self.audio_segments = audio_segments


    def run(self):
        while True:
            result = self.audio_segments.get()
            print(result)
            self.audio_segments.task_done()

audio_segments = Queue()
recorder = RecordingService(audio_segments)
transcriber = TranscriptionService(audio_segments)

recorder.start()
transcriber.start()



# def record_audio(duration = 10, sample_rate=44100):
   
#     recording = sd.rec(frames=duration * sample_rate,
#                        samplerate=sample_rate, channels=1)
#     print("Started recording")

#     sd.wait()
#     print("finished recording")

#     filename = f"{getcwd()}/audio.wav"
#     write(filename=filename, rate=sample_rate, data=recording)

#     return filename


# def transcribe_audio(filename: str):
#     model = whisper.load_model("base")
#     result = model.transcribe(filename)
#     return result.get("text")

# audio_file = record_audio()
# transcription = transcribe_audio(audio_file)

# print(transcription)
