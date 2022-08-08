# chedsapp
# ched#1234 on discord

import os

directory = os.path.dirname(os.path.realpath(__file__))
print(directory)

# iterate over files in
for filename in os.listdir(directory):
	f = os.path.join(directory, filename)
	if os.path.isfile(f) and f[-4:]==".dds":
		print("Helo the next is f")
		print(f)
		pre, ext = os.path.splitext(f)
		os.rename(f, pre + ".png")
