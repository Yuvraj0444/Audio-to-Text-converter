import tkinter as tk
from tkinter import filedialog, messagebox
import speech_recognition as sr
from pydub import AudioSegment

def select_audio_file():
    file_path = filedialog.askopenfilename(
        filetypes=[("WAV files", "*.wav"), ("All files", "*.*")]
    )
    if file_path:
        try:
            transcribe_audio(file_path)
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

def transcribe_audio(file_path):
    try:
        audio = AudioSegment.from_wav(file_path)  # Change to from_wav for WAV files
        recognizer = sr.Recognizer()

        # No need to convert to WAV as it's already in WAV format

        with sr.AudioFile(file_path) as source:  # Directly use the input file
            audio_data = recognizer.record(source)

        text = recognizer.recognize_google(audio_data)
        transcription_text.delete("1.0", tk.END)
        transcription_text.insert("1.0", text)

    except Exception as e:
        messagebox.showerror("Error", f"Transcription failed: {e}")

def clear_text():
    transcription_text.delete("1.0", tk.END)

root = tk.Tk()
root.title("Audio to Text Converter")
root.geometry("400x300")

# File selection button
select_button = tk.Button(root, text="Select WAV File", command=select_audio_file)  # Change button text
select_button.pack(pady=10)

# Text area to display transcription
transcription_text = tk.Text(root, wrap="word", height=10)
transcription_text.pack(fill="both", expand=True)

# Clear button
clear_button = tk.Button(root, text="Clear Text", command=clear_text)
clear_button.pack(pady=5)

root.mainloop()
