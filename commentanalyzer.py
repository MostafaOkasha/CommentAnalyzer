# Author:       Mostafa Okasha (okashm@mcmaster.ca)
# Affiliation:  CapitalOne - Technical Assessment
import re
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

# NOTE: CLASSMETHOD VS staticmethod. know the difference know when to use what
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
                             "block_comment_lines":0, "block_comments":0, "todos":0}

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


    @staticmethod
    def comment_in_string(line,comment_index):

    def comment_single(self,comment_syntax):
        # Local variables incrementation faster than instance incrementation, update when done
        counter_dict = {"loc":0, "tot_comments":0, "single_comments": 0,
                        "block_comment_lines":0, "block_comments":0, "todos":0}

        with open(self.filename, 'r') as active_file:
            bool_active_block = False     # Keep track if currently in an active block
            bool_previous_comment = False # To keep track of lines in a block
            block_counter_temp = 0

            for line in active_file:
                counter_dict["loc"] +=1
                line = line.strip()

                # Check if line starts with comment: block or solo
                if line.startswith(comment_syntax[0]):
                    counter_dict["todos"] += line.count("TODO")
                    block_counter_temp += 1

                    if not bool_previous_comment:
                        bool_previous_comment = True
                    else:
                        bool_active_block = True

                # Assuming strings start with " or ', must determine if comment
                # is part of a string or not. e.g: print("//string") //comment
                elif comment_syntax[0] in line:
                    if bool_previous_comment and bool_active_block:
                        counter_dict["block_comments"] += 1
                        counter_dict["block_comment_lines"] += block_counter_temp
                        block_counter_temp = 0 # Reset Block counter
                        bool_active_block = False
                        bool_previous_comment = False # Exiting a block

                    # Moving from a single line comment to code with a comment
                    elif bool_previous_comment:
                        counter_dict["single_comments"] +=1
                        bool_previous_comment = False
                        block_counter_temp = 0
                    
                    prev_comment_index = -1
                    while True:
                        comment_index = line.find(comment_syntax[0], prev_comment_index + 1)
                        prev_comment_index = comment_index
                        if comment_index == -1: break

                        # Look for comment literal outside of quotes ' ' and " "
                        if not comment_in_string(line,comment_index):
                            counter_dict["single_comments"] +=1
                            counter_dict["todos"] += line[comment_index + 1,:].count("TODO")
                            break

                else:
                    # This is only code or empty line
                    # check if we just exited a block and do:
                    # Moved from a block to a code with no comments in beginning of line

                    if bool_previous_comment and bool_active_block:
                        counter_dict["block_comments"] +=1
                        counter_dict["block_comment_lines"] += block_counter_temp
                        block_counter_temp = 0 # Reset Block counter
                        bool_active_block = False
                        bool_previous_comment = False

                    # Moving from a single line comment to code or empty line
                    elif bool_previous_comment:
                        counter_dict["single_comments"] +=1
                        bool_previous_comment = False
                        block_counter_temp = 0

            # In case folder ended with a block of code
            if bool_previous_comment and bool_active_block:
                        counter_dict["block_comments"] +=1
                        counter_dict["block_comment_lines"] += block_counter_temp
        
        counter_dict["tot_comments"] = \
            counter_dict["block_comment_lines"] + counter_dict["single_comments"]

        return counter_dict
    
    def comment_block(self,comment_syntax):
        # Local variables incrementation faster than instance incrementation, update when done
        counter_dict = {"loc":0, "tot_comments":0, "single_comments": 0,
                        "block_comment_lines":0, "block_comments":0, "todos":0}
        with open(self.filename, 'r') as active_file:
            bool_active_block = False # Keep track if currently in an active block
            bool_previous_comment = False # To keep track of lines in a block

            for line in active_file:
                counter_dict["loc"] +=1
                line = line.strip()

                if line != "" and not active_block: #only empty lines inside a block should count

                    # Check if line starts with comment: block or solo
                    if line.startswith(comment_syntax[0]):
                        counter_dict["tot_comments"] +=1
                        # If not true, this might be first comment in block
                        if not bool_previous_comment:
                            bool_previous_comment = True
                        else:
                            counter_dict["todos"] += line.count(TODO)

                # nothing to check here, just indent the block
                elif line == "" and active_block:
                    counter_dict["block_comment_lines"] +=1
        return counter_dict

    def comment_block_single(self,comment_syntax):
        # Local variables incrementation faster than instance incrementation, update when done
        counter_dict = {"loc":0, "tot_comments":0, "single_comments": 0,
                        "block_comment_lines":0, "block_comments":0, "todos":0}
        with open(self.filename, 'r') as active_file:
            bool_active_block = False # Keep track if currently in an active block
            bool_previous_comment = False # To keep track of lines in a block

            for line in active_file:
                counter_dict["loc"] +=1
                line.strip()

                if line != "" and not active_block: #only empty lines inside a block should count

                    # Check if line starts with comment: block or solo
                    if line.startswith(comment_syntax[0]):
                        counter_dict["tot_comments"] +=1
                        # If not true, this might be first comment in block
                        if not bool_previous_comment:
                            bool_previous_comment = True
                        else:
                            counter_dict["todos"] += line.count(TODO)

                # nothing to check here, just indent the block
                elif line == "" and active_block:
                    counter_dict["block_comment_lines"] +=1
        return counter_dict
    # Main method for comment analysis
    def analyze_code(self):

        style_name, syntax_condition = EXTENSIONS_STYLE[self.file_extension]
        comment_syntax = STYLE_SYNTAX[style_name]
        # comment_syntax is the comment styling (containing the symbols)
        # syntax_condition defines if language uses block comments, multi syntax, only block, etc..
        
        if syntax_condition == True:
            counter_dict = self.comment_block_single(comment_syntax)
        
        elif syntax_condition == False:
            counter_dict = self.comment_single(comment_syntax)
        
        elif syntax_condition == BLOCK_ONLY:
            counter_dict = self.comment_block(comment_syntax)

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