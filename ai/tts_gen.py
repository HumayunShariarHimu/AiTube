from gtts import gTTS

def generate_voice(text, filename="assets/voice.mp3"):
    tts = gTTS(text=text, lang='bn')
    tts.save(filename)