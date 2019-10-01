

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



# New style object for backwards compatibility with Python 2 and Python 3. We are being Python agnostic.
# 


# OOP Approach: Same maintainability as Procedural approach
# but uses much more memory: Analyzed at
# 1235% more on average.
class CommentCounter(object):
        """docstring for CheckFile"""

	#init that takes no arguments (no file name)
	#file name is the only input for our class
	def __init__(self):
		super(CheckFile, self).__init__()
		self.arg = arg
		self.


# have a dict of file extensions and comments and comment blocks for different file extensions. This allows scalability for adding file types and different types. Look into templates <template> T to give in different values? no this makes no sense.
# 
# desctructor
# 
	def reset_counter(self):

	def analyze_comment_type(self,self.line):

	def analyze_line(self,self.line):

	def extension_type(self):
		# IF FILE NAME STARTS WITH . then ignore, otherwise make sure file name has only one . and then output filename.ext. output ext as extension type

Regular expression for multi-line comments
//
// /*
some code()
// */

Edge Cases to consider:

# Determine Language group by looking at file extensions
# E.g: files of type: .c, .cpp, .h, .hpp, .js, .java, .scala processed as cSyntaxComment
Circumstances for c style comments:
"Inlines:"
// single line comment taking up line solely
some_code() // inline-comment


    def check_in
    def scan_file
    def identify_comment
    def seggregate_comments
    def count_todo
    def validate_file_type
    def something_something(self):
		with open(file_name, 'r', encoding='utf-8') as active_file:
			for line in active_file:
				if line.startswith():





'''[summary]

[description]
'''
if __name__ == '__main__':



