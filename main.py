from os import getcwd
import sounddevice
from scipy.io.wavfile import write
import whisper


def record_audio(duration=10, sample_rate=44100):

    recording = sounddevice.rec(
        frames=duration * sample_rate, samplerate=sample_rate, channels=1)
    print("Started Recording")

    sounddevice.wait()
    print("finished recording")

    filename = f"{getcwd()}\\audio.wav"
    write(filename=filename, rate=sample_rate, data=recording)

    return filename


def transcribe_audio(filename: str):
    model = whisper.load_model("base")
    result = model.transcribe(filename)
    return result.get("text")


audio_file = record_audio()
transcription = transcribe_audio(audio_file)

print(transcription)
