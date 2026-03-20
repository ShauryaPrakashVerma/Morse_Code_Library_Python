import sounddevice as sd
# from sounddevice import 
import numpy as np

# from .encoder import encode


def audio_encode() -> None:
    fs = 40000  # Sample rate
    duration = 0.1  # try even 0.05

    t = np.linspace(0, duration, int(fs * duration), endpoint=False)
    x = np.sin(2 * np.pi * 440 * t)

    # 🔥 Apply envelope (VERY IMPORTANT)
    fade_duration = 0.01  # 10 ms
    fade_samples = int(fs * fade_duration)

    envelope = np.ones_like(x)

    # Fade-in
    envelope[:fade_samples] = np.linspace(0, 1, fade_samples)

    # Fade-out
    envelope[-fade_samples:] = np.linspace(1, 0, fade_samples)

    x = 0.5 * x * envelope  # apply envelope + volume

    # Play audio
    sd.play(x, fs)
    sd.wait()
    
def generate_tone(freq, duration, sr=44100):
    t = np.linspace(0, duration, int(sr * duration), False)
    return np.sin(2 * np.pi * freq * t)

def silence(duration, sr=44100):
    return np.zeros(int(sr * duration))
audio_encode()