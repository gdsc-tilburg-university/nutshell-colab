from recording.RecordingService import RecordingService
from transcription.TranscriptionService import TranscriptionService
from summarization.SummaryService import SummaryService
from frontend.main import renderGUI
from queue import Queue

if __name__ == "__main__":
    audioSegments = Queue()
    transcribedTextQueue = Queue()

    recorder = RecordingService(audioSegments, duration=15)
    transcriber = TranscriptionService(audioSegments, transcribedTextQueue)
    summarizer = SummaryService(transcribedTextQueue)

    recorder.start()
    transcriber.start()
    summarizer.start()

    renderGUI()
