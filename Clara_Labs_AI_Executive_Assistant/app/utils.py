
import speech_recognition as sr
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

def transcribe_audio(audio_file):
    r = sr.Recognizer()
    with sr.AudioFile(audio_file) as source:
        audio = r.record(source)
    try:
        text = r.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        return None
    except sr.RequestError:
        return None

def preprocess_text(text):
    tokens = word_tokenize(text)
    tokens = [token.lower() for token in tokens if token.isalpha()]
    stop_words = set(stopwords.words('english'))
    tokens = [token for token in tokens if token not in stop_words]
    return tokens

