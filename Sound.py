import tkinter as tk
import numpy as np
import sounddevice as sd

# Sampling rate
sample_rate = 44100

# Duration of each note
note_duration = 0.5  # seconds

# Amplitude of the waveform
amplitude = 0.5

# Note frequencies for one octave (starting from middle C)
key_freqs = {
    'a': 261.63,  # C4
    's': 293.66,  # D4
    'd': 329.63,  # E4
    'f': 349.23,  # F4
    'g': 392.00,  # G4
    'h': 440.00,  # A4
    'j': 493.88,  # B4
    'k': 523.25   # C5
}

def play_tone(frequency, duration=note_duration):
    """Generate and play a sine wave for the given frequency and duration."""
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    waveform = amplitude * np.sin(2 * np.pi * frequency * t)
    sd.play(waveform, samplerate=sample_rate)
    sd.wait()

def on_key_press(event):
    key = event.char.lower()
    if key in key_freqs:
        freq = key_freqs[key]
        play_tone(freq)

# GUI Setup
root = tk.Tk()
root.title("🎹 Virtual Piano Synth")

label = tk.Label(root, text="Press keys A–K to play notes (C4 to C5)", font=('Arial', 16))
label.pack(pady=20)

# Show key mappings
info = "\n".join([f"{k.upper()} → {round(f)} Hz" for k, f in key_freqs.items()])
key_label = tk.Label(root, text=info, font=('Courier', 14))
key_label.pack()

# Bind key press
root.bind("<KeyPress>", on_key_press)

root.mainloop()
