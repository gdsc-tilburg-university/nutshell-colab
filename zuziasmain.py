import sounddevice as sd
from os import getcwd
from scipy.io.wavfile import write


def record_audio(duration = 10, sample_rate=44100):
   
    recording = sd.rec(frames=duration * sample_rate,
                       samplerate=sample_rate, channels=1)
    print("Started recording")

    sd.wait()
    print("finished recording")

    filename = f"{getcwd()}/audio.wav"
    write(filename=filename, rate=sample_rate, data=recording)

    return filename


def transcribe_audio(filename: str):
    return 0

audio_file = record_audio()
transcription = transcribe_audio(audio_file)

print(transcription)