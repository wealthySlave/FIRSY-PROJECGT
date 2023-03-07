import pyaudio
import openai
import tempfile
import wave

# Set up OpenAI API credentials
openai.api_key = "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"

# Set up PyAudio
audio = pyaudio.PyAudio()
stream = audio.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=12000)
file_format = pyaudio.get_format_from_width(audio.get_sample_size(pyaudio.paInt16))
stream.start_stream()

# Capture audio and send to OpenAI API for transcription
while True:
    data = stream.read(12000)
    with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as fp:
        with wave.open(fp, "wb") as wav:
            wav.setnchannels(1)
            wav.setsampwidth(audio.get_sample_size(pyaudio.paInt16))
            wav.setframerate(16000)
            wav.writeframes(data)
        fp.seek(0)
        transcript = openai.Audio.transcribe("whisper-1", fp)
        #text = transcript['transcriptions'][0]['text'].strip()
        print(transcript)
