import tkinter as tk
from tkinter import ttk
import Bad_character_rule, Good_suffix, Indexing, Verify_sequence
from reverse_complement import rev_comp_st
from KMP_algorithm import KMPSearch
from match import match

def bad_character(pattern, text):
    if text and pattern:  # Check if both fields are non-empty
        result_label.config(text=f"{Bad_character_rule.search(text, pattern)}")
    else:
        result_label.config(text="Please enter both Text and Pattern.")

def good_suffix(pattern, text):
    if text and pattern:  # Check if both fields are non-empty
        result_label.config(text=f"{Good_suffix.search(text, pattern)}")
    else:
        result_label.config(text="Please enter both Text and Pattern.")
        
def indexing(text, pattern):
    if text and pattern:  # Check if both fields are non-empty
        result_label.config(text=f"{Indexing.search(text, pattern)}")
    else:
        result_label.config(text="Please enter both Text and Pattern.")
        
def reverse(text):
    result_label.config(text=f"{rev_comp_st(text)}")

def verify(text):
    result_label.config(text=f"{Verify_sequence.verify(text)}")
    
def matchS(text, pattern):
    if text and pattern:
        result_label.config(text=f"{match(pattern, text)}")
    else:
        result_label.config(text="Please enter both Text and Pattern.")

def KMP(text, pattern):
    if text and pattern:  # Check if both fields are non-empty
        result_label.config(text=f"{KMPSearch(text, pattern)}")
    else:
        result_label.config(text="Please enter both Text and Pattern.")

# Create the main application window
app = tk.Tk()
app.title("Bioinformatics GUI - Enhanced Design")

# Set window size and position
app.geometry("800x500")
app.resizable(True, True)

# Set background color
app.configure(bg='#F0F0F0')

# Create title label with a new font and color
title_font = ("Arial", 32, "bold")
title_label = tk.Label(app, text="Bioinformatics", font=title_font, fg='navy', bg='#F0F0F0')
title_label.pack(side=tk.TOP, pady=20)

# Create labels for text and pattern
text_label = tk.Label(app, text="Enter Text", font=("Arial", 12), fg='black', bg='#F0F0F0')
pattern_label = tk.Label(app, text="Enter Pattern", font=("Arial", 12), fg='black', bg='#F0F0F0')

# Create input fields for sequences and text
text_entry = tk.Entry(app, width=30)
sequence_entry = tk.Entry(app, width=30)

# Create two frames for buttons
frame_top = tk.Frame(app, bg='#F0F0F0')
frame_bottom = tk.Frame(app, bg='#F0F0F0')

# Create buttons for algorithms with improved styling
BadCharacter_btn = ttk.Button(frame_top, text="Bad Character Search", command=lambda: bad_character(text_entry.get(), sequence_entry.get()))
GoodSuffix_btn = ttk.Button(frame_top, text="Good Suffix Search", command=lambda: good_suffix(text_entry.get(), sequence_entry.get()))
Indexing_btn = ttk.Button(frame_top, text="Indexing Search", command=lambda: indexing(text_entry.get(), sequence_entry.get()))
Reverse_btn = ttk.Button(frame_top, text="Reverse", command=lambda: reverse(text_entry.get()))
Verify_btn = ttk.Button(frame_bottom, text="Verify", command=lambda: verify(text_entry.get()))
Match_btn = ttk.Button(frame_bottom, text="Match", command=lambda: matchS(text_entry.get(), sequence_entry.get()))
KMP_btn = ttk.Button(frame_bottom, text="KMP Search", command=lambda: KMP(text_entry.get(), sequence_entry.get()))

# Create Label widget for displaying results with improved styling
result_label = tk.Label(app, text="", font=("Arial", 12), fg='green', bg='#F0F0F0')
result_label.pack(pady=10)

# Arrange widgets using pack layout
text_label.pack(pady=5)
text_entry.pack(pady=5)

pattern_label.pack(pady=5)
sequence_entry.pack(pady=5)

# Pack buttons in frames
BadCharacter_btn.pack(side=tk.LEFT, pady=10, padx=10)
GoodSuffix_btn.pack(side=tk.LEFT, pady=10, padx=10)
Indexing_btn.pack(side=tk.LEFT, pady=10, padx=10)
Reverse_btn.pack(side=tk.LEFT, pady=10, padx=10)
Verify_btn.pack(side=tk.LEFT, pady=10, padx=10)
Match_btn.pack(side=tk.LEFT, pady=10, padx=10)
KMP_btn.pack(side=tk.LEFT, pady=10, padx=10)

# Pack frames
frame_top.pack(side=tk.TOP)
frame_bottom.pack(side=tk.TOP)

# Start the GUI event loop
app.mainloop()
