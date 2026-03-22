import sounddevice as sd
import soundfile as sf
import numpy as np


FS = 44100
FREQ = 700
WPM = 20
# from .encoder import encode



def wpm_to_unit(wpm:int):
    if wpm <= 0:
        raise ValueError("WPM must be positive")
    unit = (1.2 / wpm)*10


def generate_tone(freq, duration):
    t = np.linspace(0 , duration, int(FS * duration), False)
    tone = np.sin(2 * np.pi * freq * t)
    return tone


def generate_silence(duration):
    return np.zeros(int(FS * duration))


def morse_to_audio(morse, wpm = 20, frequency = 700):
    unit = 1.2 / wpm
    
    audio = []
    
    for symbol in morse:
        if symbol == ".":
            audio.extend(generate_tone(frequency, unit))
        elif symbol == "-":
            audio.extend(generate_tone(frequency, 3 * unit))
        elif symbol == " ":
            audio.extend(generate_silence(3 * unit))
        elif symbol == "/":
            audio.extend(generate_silence(7 * unit))
            
    return np.array(audio)
    

def play_audio(audio):
    sd.play(audio, FS)
    sd.wait()

def save_audio(audio, filename, FS):
    sf.write(filename, audio, FS)



a = morse_to_audio("...  ....  . -  . . -  . - .  - . - -  . -   /   . - - .   . - .   . -   - . -   . -   . . .   . . . .   /   . . . -   .   . - .   - -  . - ") 
print(a)
play_audio(a)