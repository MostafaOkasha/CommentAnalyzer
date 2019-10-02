# Author:       Mostafa Okasha (okashm@mcmaster.ca)
# Affiliation:  CapitalOne - Technical Assessment

"""  ------Class Methods Expansion------
#
# @CommentAnalyzer: This class will hold functions to allow code analysis to determine
#                   quantity of LOC, Total Comments, In-line Comments, Block Comments and TODOs
#
# @method1:         This does the following...
#
# @method1:         This does the following...
#
# @method1:         This does the following...
#
# @method1:         This does the following...
#
# @method1:         This does the following...
#
# @method1:         This does the following...
#
# @required enums.py, constants.py, blah blha


# MATLAB: % for single and %{ %} one multiline block
# C++/C/Java/JavaScript/ActionScript/JS/CSS: // and /* */
# Basic, COBOL: REM comment
# Fortran: C comment
# COBOL: Astreisk in position 7 *
# ALGOL 60: ;
# Assembly: ;
# ADA, mySQL: --
# FORTRAN90: !
# Perl/TCL/UNIX SHELL/mySQL: #
# VB .NET: '
# ALGOL: comment "ends with" ;
# Pascal: (* ... *) or { ... }
# Many languages: /* ... */
# Forth: ( ... )
# HTML: <!-- .... -->
# Haskell: {- ... -}
# XML ?
# NESTED COMMENTS!!!!!!!!!!!!!!!!
# Ada: -- some comment (up to end of line)
# Visual basic (microsoft stuff) use: ' (Quick Basic, Q Basic, Visual Basic, Visual Basic .NET, and VB Script)
# Latex: %
# Lua: -- single comment (just like Ada, Eiffel, Haskell, SQL, VHDL). block comment: --[[ ... ]]
# PHP: Uses # and C++ style as well. /* */ and //
# CSS: /* ... */
# ActionScript: just like java
# Ruby and Assembly like python
# 
# Powershell: # single and <# #> for multiple
# Python: """ well """ not stripped from the docstring. They are treated like string literals.
# Ruby: # multi: =begin ... =end
# SQL: --
# Swift: Just like C++
# XML/HTML: <!-- ... -->
# """

class CommentAnalyzer(object):
    """Determine quantitative values for different comment types

    Count the LOC (lines of code) and analyze it to determine the LOC that are comments, 
    block comments, in-line comments and TODOs to provide a quantitive analysis.
    """

    def __init__(self, file_name=""):
        self.file_name = file_name
        self.file_type = file_name.get_file_type();
        self.check_in_status = 0 # 0 for not checked

        # Counter variables
        # use dictionary iteritems
        # collections.dequeue is much faster since it doesn't rebuild the list
        self.loc_count = 0          # LOC: Lines of Code
        self.comment_count = 0
        self.inline_comment_count = 0
        self.block_comment_count = 0

    # Local variables in functions are accessed more quickly than global variables
    # 
    def get_file_type(self):
        if !startswith(self.file_name,'.'):
            #extract everything after the dor

    # TODO: hello

    @classmethod
    def make_sound(cls):
        # You can run this on the entire class and all instances of the class?
        print(hello)

    #when you need no access to the class, Python won't pass the class to it.
    @staticmethod
    def make_sound():
        print(hello)

    @property
    def engine_strain(self):
        if not self.engines:
            return 0
        elif self.shields:
            return self.engspeed * 2
        return self.eng_speed
    # property can be treated like an instance variable.
    # when you call object.engine_strain it will return 0 or double the engspeed
    # but you can't set it! you can't write object.engine_strain = 2
    # if it's just property, it is pretty much a getter. this below is a setter


    # Have a config.py where you can config your values for comments and file extension names

    @name_of_property.setter
    def engine_strain(self, value):
        print("giving it all I got")

    with open(file_name, 'r', encoding='utf-8') as active_file:
        for line in active_file:
            if line.startswith():
                print(hello)

    # This is a destructor
    def __del__(self):
        self.destruct = true






# This program checks on the code when it is merged into the build pipeline. This program runs everytime an engineer checks in code.
# 
# 

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



	#init that takes no arguments (no file name)
	#file name is the only input for our class

         #super(CheckFile, self).__init__()
        # self.arg = arg


# have a dict of file extensions and comments and comment blocks for different file extensions. This allows scalability for adding file types and different types. Look into templates <template> T to give in different values? no this makes no sense.
# 
# desctructor
 #   def reset_counter(self):

  #  def analyze_comment_type(self,self.line):

   # def analyze_line(self,self.line):

	#def extension_type(self):
		# IF FILE NAME STARTS WITH . then ignore, otherwise make sure file name has only one . and then output filename.ext. output ext as extension type

#Regular expression for multi-line comments
#//
#// /*
#some code()
#// */

#Edge Cases to consider:

# Determine Language group by looking at file extensions
# E.g: files of type: .c, .cpp, .h, .hpp, .js, .java, .scala processed as cSyntaxComment
#Circumstances for c style comments:
#"Inlines:"
#// single line comment taking up line solely
#some_code() // inline-comment


    #def check_in
    #def scan_file
    #def identify_comment
    #def seggregate_comments
    #def count_todo
   # def validate_file_type
    #def something_something(self):
		#with open(file_name, 'r', encoding='utf-8') as active_file:
			#for line in active_file:
				#if line.startswith():

                    '''[summary][description]
                    '''
#if __name__ == '__main__':