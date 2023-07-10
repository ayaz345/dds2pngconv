# chedsapp
# ched#1234 on discord
import os
from tkinter import Tk
from tkinter.filedialog import askdirectory
directory = askdirectory(title='select directory with .dds files')
print(directory)

for v in os.listdir(directory):
	f = os.path.join(directory, v)
	if os.path.isfile(f) and f[-4:]==".dds":
		pre, ext = os.path.splitext(f)
		os.rename(f, f"{pre}.png")