<<<<<<< HEAD
<<<<<<< HEAD

# coding = utf-8

import webbrowser, sys, pyperclip

# Check if command line arguments were passed

if len(sys.argv) > 1:

	# Combine the arguments into a single string: calle, numero, ciudad, 
	# We have a list: we slice it to avoid first element (name of the script)
	address = " ". join(sys.argv[1:])

else:
	address = pyperclip.paste()

webbrowser.open("https://www.google.es/maps/place/" + address)

=======

# coding = utf-8

import webbrowser, sys, pyperclip

# Check if command line arguments were passed

if len(sys.argv) > 1:

	# Combine the arguments into a single string: calle, numero, ciudad, 
	# We have a list: we slice it to avoid first element (name of the script)
	address = " ". join(sys.argv[1:])

else:
	address = pyperclip.paste()

webbrowser.open("https://www.google.es/maps/place/" + address)

>>>>>>> caa7a19daf82ef17cbd26673297aabeac62a1417
=======

# coding = utf-8

import webbrowser, sys, pyperclip

# Check if command line arguments were passed

if len(sys.argv) > 1:

	# Combine the arguments into a single string: calle, numero, ciudad, 
	# We have a list: we slice it to avoid first element (name of the script)
	address = " ". join(sys.argv[1:])

else:
	address = pyperclip.paste()

webbrowser.open("https://www.google.es/maps/place/" + address)

>>>>>>> a3c79e1e64543b0d6f078d5527564506ecdfc6db
