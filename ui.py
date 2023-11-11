import tkinter as tk
from tkinter import ttk
from tkinter import Label, Spinbox
from tkinter import filedialog as fd
from tkinter.filedialog import asksaveasfile
from tkinter.messagebox import showinfo
import process_file


def ui():
	root = tk.Tk()
	root.title("Bulk translator")
	root.resizable(True,True)
	root.geometry("400x200")

	def quit():
		root.destroy()
		exit()

	def process():
		if tk.messagebox.askokcancel(title="Do you wish to continue?", message="The program usually hangs for a while when translating\nRead console for proggress info."):
			global filename
			try:
				number = int(number_picker.get())
			except Exception as e:
				print(e)
				tk.messagebox.showerror(title="Error",message="Operation cancelled.\nYou must specify the amount of translation steps.")
				return
			if filename == None or number == None or output_file ==None:
				tk.messagebox.showerror(title="Error",message="Operation cancelled.\nYou must specify all the fields.")
				
			process_file.main(filename, number)
		else:
			tk.messagebox.showinfo(title="Cancelled",message="Operation cancelled.")



	def select_file():
		filetypes = (("Text files","*.txt"),("Debug Types", "*.*"))
		global filename
		filename = fd.askopenfilename(title="Select source file",initialdir=".",filetypes=filetypes)
		print(filename)

	def select_output():
		global output_file
		output_file = asksaveasfile(initialfile = 'Untitled.txt',
		defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documents","*.txt")])
		print(output_file.name)


	select_source_button = ttk.Button(root,text="Select source file", command=select_file)

	select_source_button.pack(expand=True)

	select_output_button = ttk.Button(root,text="Select output file", command=select_output)

	select_output_button.pack(expand=True)

	number_label = Label(root,text="Number of translation steps")

	number_label.pack(expand=True)

	number_picker = Spinbox(root,bd=2)

	number_picker.pack()

	process_button = ttk.Button(root,text="Process", command=process)

	process_button.pack(expand=True)

	exit_button = ttk.Button(root,text="Exit", command=quit)

	exit_button.pack(expand=True)

	root.mainloop()