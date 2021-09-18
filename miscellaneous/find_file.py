import os, sys

def find_file(start, file_name: str):
	for relpath, dirs, files in os.walk(start):
		if file_name in files:
			full_path = os.path.join(start, relpath, file_name)
			print('full_path: ', full_path)
			abs_path = os.path.abspath(full_path)
			print('abs_path: ', abs_path)
			norm_path = os.path.normpath(abs_path)
			print('norm_path: ', norm_path)

if __name__ == '__main__':
	find_file(sys.argv[1], sys.argv[2])
	# Example: find_file('H:/', 'find_file.py')