# This program checks on the code when it is merged into the build pipeline. This program runs everytime an engineer checks in code.
# 
# 

# Author: Mostafa Okasha
# Last Modified: September 02, 2019


# 1.) When a file is checked in, scan file to count total number of lines

# 2.) Scan file to identify comments, and count total lines of comments in the file.

# 3.) After identifying lines of comments, scan to seggregate total number of single line comments and the total number of multi-line comments

# 4.) Any line of code with both code and a comment should count both as a line of code and also a comment line


# 5.) From all the comments, identify the total number of TODOS


# NOTE:
# 	1.) Ignore files starting with '.'
# 	2.) We can check any valid program
# 	3.) If a file has no extension, then ignore it.
# 	
# 	Input: file name
# 	Output:
# Example:
# Total # of lines: 60
# Total # of comment lines: 28
# Total # of single line comments: 6
# Total # of comment lines within block comments: 22
# Total # of block line comments: 2
# Total # of TODO’s: 1
# 

with open(file_name, 'r', encoding='utf-8') as active_file:
	for line in active_file:
		if line.startswith():


class CheckFile(object):
	"""docstring for CheckFile"""
	def __init__(self, arg):
		super(CheckFile, self).__init__()
		self.arg = arg

'''[summary]

[description]
'''
if __name__ == '__main__':



