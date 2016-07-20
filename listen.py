import speech_recognition as sr
import tempfile

while True:
    r = sr.Recognizer()

    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        # print(audio.sample_rate)
        # print(audio.sample_width)

        with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as f:
            f.write(audio.get_wav_data())

        try:
            print(r.recognize_google(audio, language='pl-PL', show_all=False))
        except sr.UnknownValueError:
            print("didn't hear anything familiar")
            pass
        except sr.RequestError:
            print("couldn't reach the service")
            pass
