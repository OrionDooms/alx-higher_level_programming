#!/usr/bin/node
import sys
def Readme(file_path):
	try:
		with open(file_path, 'r', encoding='utf-8') as file:
			content = file.read()
			print(content)
	except Exception as e:
		print("Error reading file:", e)

if __name__ == "__main__":
	if len(sys.arg) != 2:
		print("Error")
	else:
		file_path = sys.argv[1]
		read_file(file_path)
