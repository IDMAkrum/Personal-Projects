import tkinter as tk
from tkinter import messagebox as mb

# button commands

def encode():
	"""Puts 'plain text' in label1 and 'cipher text' in label3."""
	global decoding
	if decoding:
		labels[2]["text"] = "Cipher text:"
		labels[0]["text"] = "Plain text:"
		decoding = False

def decode():
	"""Puts 'cipher text' in label1 and 'plain text' in label3."""
	global decoding
	if not decoding:
		labels[0]["text"] = "Cipher text:"
		labels[2]["text"] = "Plain text:"
		decoding = True 

def convert():
	"""Converts text from entry1 and places new text in entry3."""
	text = entries[0].get()
	key = entries[1].get()
	if not check_conditions(text, key):
		return
	key = generateKey(text, key)
	converted = shift_string(text, key, decoding)
	entries[2].delete(0, tk.END)
	entries[2].insert(0, converted)

# helper methods

def generateKey(string, key):
	"""Pads key to same length as text."""
	new_key = list(key)
	if len(string) == len(key):
		return key.upper()
	else:
		for i in range(len(string) - len(key)):
			new_key.append(key[i%len(key)])
		return("". join(new_key)).upper()

def shift_string(text, key, reverse):
	"""Shifts string either + key or - key if reverse."""
	new_string = []
	for i in range(0, len(text)):
		upper = text[i].isupper()
		ch = ord(text[i]) if upper else ord(text[i].upper())
		if not reverse:
			ch = (ch + ord(key[i])) % 26
		else:
			ch = (ch - ord(key[i]) + 26) % 26 
		ch += ord('A')
		ch = chr(ch) if upper else chr(ch).lower()
		new_string.append(ch)
	return("". join(new_string))

def check_conditions(text, key):
	"""Checks whether text and key are correctly formatted."""
	global decoding
	if len(text) == 0 and len(key) == 0:
		return False
	if len(text) == 0:
		if decoding:
			message = "Please fill in cipher text to decode."
		else:
			message = "Please fill in plain text to encode."
		mb.showerror("emptyfield", message)
		return False
	if len(key) == 0:
		mb.showerror("nokey",
			"Please fill in a key.")
		return False
	if not text.isalpha() or not key.isalpha():
		mb.showinfo("String support",
			"This application only supports alphabetic text (no numbers or special symbols).")
		return False
	return True

# main window
root = tk.Tk()
root.title("Vigenère Cipher - En/Decoder")
root.minsize(height=220, width=450)
root.geometry('520x265+430+200') # width x height + x + y
root.configure(bg="#b78d5a")

# global variable for whether the user is encoding or decoding
decoding = False

# frame for options
frm_options = tk.Frame(bg="#b78d5a")
frm_options.rowconfigure(0, minsize=50, weight=1)
frm_options.columnconfigure([0, 1], minsize=100, weight=1)
frm_options.pack(pady=5)

# option buttons
btn_encode = tk.Button(master=frm_options, text="Encode", 
	bg="#fff6d6", fg="#4e2d0b", 
	activebackground="#fff6d6", activeforeground="#4e2d0b",
	font="Helvetica 11 bold", command=encode)
btn_encode.grid(row=0, column=0, padx=15, ipadx=10)

btn_decode = tk.Button(master=frm_options, text="Decode",
	bg="#4e2d0b", fg="#fff6d6",
	activebackground="#4e2d0b", activeforeground="#fff6d6",
	font="Helvetica 11 bold", command=decode)
btn_decode.grid(row=0, column=1, ipadx=10)

# main frame for encoding/decoding window
frm_main = tk.Frame(relief=tk.GROOVE, borderwidth=3, bg="#fff6d6")
frm_main.rowconfigure([0, 1, 2, 3], minsize=30, weight=1)
frm_main.columnconfigure([0, 1], minsize=50, weight=1)
frm_main.pack()

# names of the entry fields
label_names = [
	"Plain text:",
	"Key:",
	"Cipher text:"
]

# lists for all labels and entry fields
labels = []
entries = []

# creating and placing all label and entry widgets in main frame
for idx, text in enumerate(label_names):
	label = tk.Label(master=frm_main, text=text,
		bg="#fff6d6", fg="#433321", font="Helvetica 10")
	entry = tk.Entry(master=frm_main, width=50, borderwidth=2,
		font="Helvetica 10")
	labels.append(label)
	entries.append(entry)

	if idx != 2:
		label.grid(row=idx, column=0, padx=5, pady=10, sticky="e")
		entry.grid(row=idx, column=1, padx=14, pady=10, sticky="e")
	else:
		label.grid(row=idx+1, column=0, padx=5, pady=10, sticky="e")
		entry.grid(row=idx+1, column=1, padx=15, pady=10, sticky="e")

# button for converting cipher text to plain text and vice versa
btn_convert = tk.Button(master=frm_main, text="Convert!",
	bg="#1d0c02", fg="white", 
	activebackground="#1d0c02", activeforeground="white",
	font="Helvetica 10 bold", command=convert)
btn_convert.grid(row=2, column=1, padx=60, ipadx=15, ipady=5)

def main():
	root.mainloop()

if __name__ == "__main__":
	main()