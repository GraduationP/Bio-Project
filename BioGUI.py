import tkinter as tk
import Bad_character_rule, Good_suffix, Indexing, Verify_sequence 
from reverse_complement import rev_comp_st
from KMP_algorithm import KMPSearch

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

def KMP(text, pattern):
    if text and pattern:  # Check if both fields are non-empty
        result_label.config(text=f"{KMPSearch(text, pattern)}")
    else:
        result_label.config(text="Please enter both Text and Pattern.")

# Create the main application window
app = tk.Tk()
app.title("Bioinformatics GUI")

# Set window size and position
app.geometry("700x400")  # Increased height to accommodate the results label
app.resizable(True, True)

# Set a cool background color (light blue)
app.configure(bg='#ADD8E6')

# Create title label with a customized font and color
title_font = ("Times", 32, "bold underline")
title_label = tk.Label(app, text="Bioinformatics", font=title_font, fg='dark blue', bg='#ADD8E6')  # Title label color and background
title_label.pack(side=tk.TOP, pady=20)

# Configure the title label for no highlight and no border
title_label.configure(highlightthickness=0, bd=0)

# Create labels for text and pattern
text_label = tk.Label(app, text="Text", font=("Arial", 12), fg='black', bg='#ADD8E6')
pattern_label = tk.Label(app, text="Pattern", font=("Arial", 12), fg='black', bg='#ADD8E6')

# Create input fields for sequences and text
text_entry = tk.Entry(app, width=30)
sequence_entry = tk.Entry(app, width=30)

# Create buttons for algorithms with FLAT relief for smoother appearance
BadCharacter_btn = tk.Button(app, text="Bad Character Search", command=lambda: bad_character(text_entry.get(), sequence_entry.get()), relief=tk.FLAT)
GoodSuffix_btn = tk.Button(app, text="Good Suffix Search", command=lambda: good_suffix(text_entry.get(), sequence_entry.get()), relief=tk.FLAT)
indexing_btn = tk.Button(app, text="Indexing Search", command=lambda: indexing(text_entry.get(), sequence_entry.get()), relief=tk.FLAT)
KMP_btn = tk.Button(app, text="KMP Search", command=lambda: KMP(text_entry.get(), sequence_entry.get()), relief=tk.FLAT)
reversing_btn = tk.Button(app, text="Reverse", command=lambda: reverse(text_entry.get(), sequence_entry.get()), relief=tk.FLAT)
verify_btn = tk.Button(app, text="Verify", command=lambda: verify(text_entry.get()), relief=tk.FLAT)

# Create Label widget for displaying results
result_label = tk.Label(app, text="", font=("Arial", 12), fg='green', bg='#ADD8E6')
result_label.pack(pady=10)

# Arrange widgets using pack layout
text_label.pack(pady=5)
sequence_entry.pack(pady=5)

pattern_label.pack(pady=5)
text_entry.pack(pady=5)

# Pack buttons together in the middle
BadCharacter_btn.pack(side=tk.LEFT, pady=10, padx=10)
GoodSuffix_btn.pack(side=tk.LEFT, pady=10, padx=10)
indexing_btn.pack(side=tk.LEFT, pady=10, padx=10)
KMP_btn.pack(side=tk.LEFT, pady= 10, padx=10)
reversing_btn.pack(side=tk.LEFT, pady=10, padx=10)
verify_btn.pack(side=tk.LEFT, pady=10, padx=10)

# Start the GUI event loop
app.mainloop()
