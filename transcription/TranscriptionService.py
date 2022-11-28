import threading
from os import remove
import whisper
from queue import Queue


class TranscriptionService(threading.Thread):
    def __init__(self, audio_segments: Queue, transcribedTextQueue: Queue, model="small.en"):
        threading.Thread.__init__(self)
        self.audio_segments = audio_segments
        self.transcribedTextQueue = transcribedTextQueue
        self.model = whisper.load_model(model)

    def run(self):
        while True:
            filename = self.audio_segments.get()
            result = self.model.transcribe(filename)
            remove(filename)
            self.transcribedTextQueue.put(result.get("text"))
            self.audio_segments.task_done()
