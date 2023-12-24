import tkinter as tk
from tkinter import ttk
import Bad_character_rule, Good_suffix, Indexing, Verify_sequence
from reverse_complement import rev_comp_st
from KMP_algorithm import KMPSearch
from match import match
from translation import Translation_Table
from tkinter import filedialog


def bad_character(text, pattern):
    if text and pattern:  # Check if both fields are non-empty
        result_label.config(text=f"Match at {Bad_character_rule.search(text, pattern)[0]}, alighments: {Bad_character_rule.search(text, pattern)[1]}")
    else:
        result_label.config(text="Please enter both Text and Pattern.")

def good_suffix(text, pattern):
    if text and pattern:  # Check if both fields are non-empty
        result_label.config(text=f"{Good_suffix.search(text, pattern)} alighments: {Good_suffix.count}")
    else:
        result_label.config(text="Please enter both Text and Pattern.")
        
def indexing(pattern, text):
    if text and pattern:  # Check if both fields are non-empty
        result_label.config(text=f"{Indexing.search(text, pattern)}")
    else:
        result_label.config(text="Please enter both Text and Pattern.")
        
def reverse(text):
    result_label.config(text=f"{rev_comp_st(text)}")

def verify(text):
    result_label.config(text=f"{Verify_sequence.verify(text)}")
    
def matchS(pattern, text):
    if text and pattern:
        result_label.config(text=f"{match(pattern, text)}")
    else:
        result_label.config(text="Please enter both Text and Pattern.")

def translate(text):
    result_label.config(text=f"{Translation_Table(text)}")

def KMP(pattern, text):
    if text and pattern:  # Check if both fields are non-empty
        result_label.config(text=f"{KMPSearch(text, pattern)}")
    else:
        result_label.config(text="Please enter both Text and Pattern.")
        
def extract_dna_sequence(fasta_text):
    # Extract DNA sequence using regular expression
    indx = fasta_text.find('cds')
    return fasta_text[indx+3:]

def upload_fasta():
    file_path = filedialog.askopenfilename(filetypes=[("Fasta files", "*.fasta")])
    if file_path:
        with open(file_path, 'r') as file:
            sequence = file.read().replace('\n', '')
            sequence = extract_dna_sequence(sequence)
            text_entry.delete(0, tk.END)
            text_entry.insert(tk.END, sequence)

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
Verify_btn = ttk.Button(frame_top, text="Verify", command=lambda: verify(text_entry.get()))
Translate_btn = ttk.Button(frame_top, text="Translation", command=lambda: translate(text_entry.get()))
Match_btn = ttk.Button(frame_bottom, text="Match", command=lambda: matchS(text_entry.get(), sequence_entry.get()))
KMP_btn = ttk.Button(frame_bottom, text="KMP Search", command=lambda: KMP(text_entry.get(), sequence_entry.get()))
UploadFasta_btn = ttk.Button(frame_bottom, text="Upload Fasta", command=upload_fasta)

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
Translate_btn.pack(side=tk.LEFT, pady=10, padx=10)
UploadFasta_btn.pack(side=tk.LEFT, pady=10, padx=10)

# Pack frames
frame_top.pack(side=tk.TOP)
frame_bottom.pack(side=tk.TOP)

# Start the GUI event loop
app.mainloop()
