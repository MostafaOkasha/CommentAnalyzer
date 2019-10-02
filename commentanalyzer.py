# Author:       Mostafa Okasha (okashm@mcmaster.ca)
# Affiliation:  CapitalOne - Technical Assessment

"""  ------CommentAnalyzer Expansion------
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
# Python: multi line comment not stripped from the docstring. They are treated like string literals.
# Ruby: # multi: =begin ... =end
# SQL: --
# Swift: Just like C++
# XML/HTML: <!-- ... -->
# """

class CommentAnalyzer(object):
    """Determine quantitative values for different comment types

    Count the LOC (lines of code) and analyze it to determine the lines that are comments, 
    block comments, in-line comments and TODOs to provide a quantitive analysis of the code.
    """

    def __init__(self, filename: str = None):
        if filename is None:
            self.filename = ""
            self.file_extension = ""
        else:
            self.filename = filename
            self.file_extension = self.get_file_extension()

        self.check_in_status = False

        # Counter variables
        # use dictionary iteritems
        # collections.dequeue is much faster since it doesn't rebuild the list
        self.loc_count = 0              # LOC: Lines of Code
        self.comment_count = 0
        self.inline_comment_count = 0
        self.block_comment_count = 0

    # Determine file name validity
    # This is a seperate function to allow ease of modification in case
    # requirements criteria for acceptable filename formats change
    # TODO: Add these comments to the README
    # TODO: Run the analysis on your own code! SUPERB. 
    def validate_filename(self):
        if not self.filename.startswith('.') and '.' in self.filename:
            return True
        else:
            return False

    # Extract file extension
    def get_file_extension(self):
        if self.validate_filename():
            return self.filename.split(".")[-1]
        else:
            return False
