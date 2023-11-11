import do_translation
def main(filename, number):
	file = open(filename, "r")
	file_contents = file.read()
	print(file_contents)
	do_translation.translate_func(file_contents, number)