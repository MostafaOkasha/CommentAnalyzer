# Author:       Mostafa Okasha (okashm@mcmaster.ca)
# Affiliation:  CapitalOne - Technical Assessment
from extensions import *

"""  ------CommentAnalyzer Expansion------

@CommentAnalyzer: This class will hold functions to allow code analysis to determine
                  quantity of LOC, Total Comments, In-line Comments, Block Comments and TODOs

@method1:         This does the following...

@method1:         This does the following...

@method1:         This does the following...

@method1:         This does the following...

@method1:         This does the following...

@method1:         This does the following...

@required:        extensions.py --> important configurations for CommentAnalyzer file extension
                  support and 

"""

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
            self.file_extension = self.get_file_extension() # False if invalid filename 

        self.check_in_status = False # True when file analysis completes

        # Counter variables
        # TODO: Change this, unnecessary repetition
        self.counter_dict = {"loc":0, "tot_comments":0, "single_comments": 0,
                             "block_comments":0, "block_comment_lines":0, "todos":0}

    def validate_filename(self)->bool:
        """Determine file name validity

        This is a seperate function to allow ease of modification in case
        requirements criteria for acceptable filename formats change
        TODO: Add these comments to the README
        TODO: Run the analysis on your own code! SUPERB.
        """
        if not self.filename.startswith('.') and '.' in self.filename:
            return True
        else:
            return False

    def get_file_extension(self):
        """ Extract file extension

        """
        if self.validate_filename():
            return self.filename.split(".")[-1]

        else:
            return False

    def has_comment(self, line):
        if "#" in line:
            return True
        else:
            return False

    # Main method for comment analysis
    def analyze_code(self):
        # Local variables incrementation faster than instance incrementation, update when done
        counter_dict = {"loc":0, "tot_comments":0, "single_comments": 0,
                        "block_comments":0, "block_comment_lines":0, "todos":0}
        comment_syntax = EXTENSIONS_SYNTAX[self.file_extension]
        with open(self.filename, 'r') as active_file:
            for line in active_file:
                counter_dict["loc"] +=1
                line.strip()
                if self.has_comment(line):
                    counter_dict["tot_comments"] +=1
        self.counter_dict = counter_dict
    
    def analysis_output(self, option:str):
        """ Output code analysis results:
        
        Options: 'terminal', 'JSON' (Python Dict), 'tuple', etc...
        Add other options for output and format it as required.
        (for now, only terminal is implemented)
        TODO: Implement multiple output formatting as required
        """
        counter_dict = self.counter_dict # To prevent multiple calls to the instance dict

        if option == 'terminal':
            # This printing method works with Python 2.6+
            for key,value in counter_dict.items():
                print("Total # of %s: %d" % (OUTPUT_FORMAT[key],value))