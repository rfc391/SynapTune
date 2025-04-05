
import tkinter as tk
from tkinter import messagebox
from neuro_signal.data_handler import load_data
from neuro_signal.neurofeedback import provide_neurofeedback
from neuro_signal.tracking import track_attention

def run_load():
    result = load_data("example_file.txt")
    messagebox.showinfo("Data Loaded", str(result))

def run_feedback():
    result = provide_neurofeedback([1.2, 2.3, 3.4])
    messagebox.showinfo("Feedback", str(result))

def run_tracking():
    result = track_attention([0.1, 0.5, 0.3])
    messagebox.showinfo("Attention Score", str(result))

app = tk.Tk()
app.title("SynapTune GUI")

tk.Button(app, text="Load Data", command=run_load, width=30, height=2).pack(pady=10)
tk.Button(app, text="Provide Neurofeedback", command=run_feedback, width=30, height=2).pack(pady=10)
tk.Button(app, text="Track Attention", command=run_tracking, width=30, height=2).pack(pady=10)

app.mainloop()
