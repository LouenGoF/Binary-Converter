import tkinter as tk
from tkinter import ttk
import threading
import time

language_dict = {
    "enter_text": "Enter text:",
    "enter_binary": "Enter binary:",
    "converted_text": "",
    "converted_binary": "",
    "convert_btn": "Convert",
    "text_to_binary": "Text to Binary",
    "binary_to_text": "Binary to Text"
}

def update_entry_text():
    if choice.get() == language_dict["text_to_binary"]:
        entry_label.config(text=language_dict["enter_text"])
    elif choice.get() == language_dict["binary_to_text"]:
        entry_label.config(text=language_dict["enter_binary"])

def convert_and_update():
    result_text.delete(1.0, tk.END)  # Efface le texte existant
    convert()
    result_text.insert(tk.END, converted_text)

def convert():
    global converted_text
    if choice.get() == language_dict["text_to_binary"]:
        text = entry.get()
        converted_text = ' '.join(format(ord(x), '08b') for x in text)
    elif choice.get() == language_dict["binary_to_text"]:
        binary = entry.get()
        binary_values = binary.split(' ')
        converted_text = ''.join(chr(int(val, 2)) for val in binary_values)

def slide_progress_bar():
    steps = 4
    for i in range(steps):
        progress_bar['value'] = (i + 1) * (100 / steps)
        ws.update_idletasks()
        time.sleep(0.5)  # Réduire le délai entre chaque étape
    convert_and_update()

ws = tk.Tk()
ws.title("Text-to-Binary Converter with Progress Bar")

# Label "Made by Louen"
made_by_label = ttk.Label(ws, text="Made by Louen GoF", font=("Helvetica", 12))
made_by_label.pack(pady=10)

# Frame pour le convertisseur
converter_frame = ttk.Frame(ws)
converter_frame.pack()

choice_frame = ttk.Frame(converter_frame)
choice_frame.pack(pady=10)

choice = tk.StringVar()
choice.set(language_dict["text_to_binary"])

ttk.Radiobutton(choice_frame, text=language_dict["text_to_binary"], variable=choice, value=language_dict["text_to_binary"], command=update_entry_text).pack(side=tk.LEFT)
ttk.Radiobutton(choice_frame, text=language_dict["binary_to_text"], variable=choice, value=language_dict["binary_to_text"], command=update_entry_text).pack(side=tk.RIGHT)

entry_frame = ttk.Frame(converter_frame)
entry_frame.pack(pady=10)

entry_label = ttk.Label(entry_frame, text=language_dict["enter_text"])
entry_label.grid(row=0, column=0)

entry = ttk.Entry(entry_frame)
entry.grid(row=0, column=1)

progress_bar = ttk.Progressbar(converter_frame, orient=tk.HORIZONTAL, length=250, mode='determinate')
progress_bar.pack(pady=10)

result_text = tk.Text(converter_frame, height=4, width=40)
result_text.pack(pady=10)

convert_button = ttk.Button(converter_frame, text=language_dict["convert_btn"], command=lambda: threading.Thread(target=slide_progress_bar).start())
convert_button.pack()

ws.mainloop()
