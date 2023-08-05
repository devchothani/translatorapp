import tkinter as tk
from tkinter import ttk
from googletrans import Translator

def translate_text():
    text = source_text.get("1.0", "end-1c")
    translator = Translator()
    translated = translator.translate(text, dest=destination_lang.get())
    translated_text.delete("1.0", tk.END)
    translated_text.insert(tk.END, translated.text)

# Create the main window
root = tk.Tk()
root.title("Language Translator")

# Create a frame for the source language text
source_frame = ttk.LabelFrame(root, text="Source Language")
source_frame.pack(pady=10)

source_text = tk.Text(source_frame, height=10, width=50)
source_text.pack()

# Create a frame for the destination language text
destination_frame = ttk.LabelFrame(root, text="Destination Language")
destination_frame.pack(pady=10)

translated_text = tk.Text(destination_frame, height=10, width=50)
translated_text.pack()

# Create a dropdown menu for selecting the destination language
destination_lang = ttk.Combobox(destination_frame, values=["en", "fr", "es", "de"])  # Add more languages as needed
destination_lang.set("en")
destination_lang.pack(pady=5)

# Create a Translate button
translate_button = ttk.Button(root, text="Translate", command=translate_text)
translate_button.pack(pady=10)

# Start the main event loop
root.mainloop()
