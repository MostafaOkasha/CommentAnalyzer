# Author:       Mostafa Okasha (okashm@mcmaster.ca)
# Affiliation:  CapitalOne - Technical Assessment
#
# Please see the README.md or README.pdf document for more details on the inner-workings
# of this module. 
''' Quick Overview

CommentAnalyzer needs to be initiated with a file name. If the filename is invalid, 
it will return False and no output. The analysis_output method can output data in 
multiple formats. Every file format can be supported! extensions.py has a list of 
all supported file formats and anyone can add to that list as long as you follow
the rules for adding comment syntax and style.

   Enjoy! ~~
'''

"""  ------CommentAnalyzer Expansion------

Class:
@CommentAnalyzer:       This class will hold functions to allow code analysis to determine
                        quantity of LOC, Total Comments, In-line Comments, 
                        Block Comments and TODOs.

@validate_filename:     Validates the filename. False if it does not start with '.' or
                        if file has no extension. Can't run any of the other methods if so.

@get_file_extension:    Sets the filename extensions if filename has been validated.

@comment_single:        Analyzes comments for languages with single comment only syntax 
                        that have no block comments. See extensions.py for more info.

@comment_block:         Analyzes comments for languages with block comment only syntax 
                        that have no single comment syntax. Such as HTML.

@comment_block_single:  Analyzes comments for languages with both single comment and
                        block comment syntax.

@analyze_code:          Decides which methods from comment_single,comment_block and
                        comment_block_single should analyze the code based on extension.

@analysis_output:       Outputs the analysis report created by the analyze_code method.
                        Can output in several formats. See method for more info.

@requirements:          extensions.py only. It has important configurations for the
                        CommentAnalyzer class file extension support and useage.

"""
from extensions import *

class CommentAnalyzer(object):
    """Determine quantitative values for different comment types

    Count the LOC (lines of code) and analyze it to determine the lines that are comments, 
    block comments, in-line comments and TODOs to provide a quantitive analysis of the code.
    """

    def __init__(self, filename):
        self.filename = filename
        self.file_extension = self.set_file_extension() # False if invalid filename 
        self.__check_in_status = False # True when file analysis completes

        # Counter variables
        self.counter_dict = {"loc":0, "tot_comments":0, "single_comments": 0,
                             "block_comment_lines":0, "block_comments":0, "todos":0}

    def validate_filename(self)->bool:
        """Determine file name validity

        This is a seperate function to allow ease of modification in case
        requirements criteria for acceptable filename formats change
        """
        if not self.filename.startswith('.') and '.' in self.filename:
            return True
        else:
            return False

    def set_file_extension(self):
        """ Extract file extension

        Supports filenames with multiple '.'s
        """
        if self.validate_filename():
            return self.filename.split(".")[-1]

        else:
            return False

    def comment_single(self,comment_syntax):
        # Local variables incrementation faster than instance incrementation, update when done
        counter_dict = {"loc":0, "tot_comments":0, "single_comments": 0,
                        "block_comment_lines":0, "block_comments":0, "todos":0}

        with open(self.filename, 'r', encoding='utf-8-sig') as active_file:
            bool_active_block = False     # Keep track if currently in an active block
            bool_previous_comment = False # To keep track of lines in a block
            block_counter_temp = 0

            for line in active_file:
                counter_dict["loc"] +=1
                line = line.strip()

                # Check if line starts with comment: block or solo
                if line.startswith(comment_syntax[0]):
                    counter_dict["todos"] += line.count(TODO)
                    #print("line",block_counter_temp, "--",line)
                    block_counter_temp += 1

                    if not bool_previous_comment:
                        bool_previous_comment = True
                    else:
                        bool_active_block = True
                
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
                    
                    # Assuming strings start with " or ', must determine if comment
                    # is part of a string or not. e.g: print("//string") //comment
                    else:
                        pos = 0
                        while pos < len(line):
                            if line[pos] == "'":
                                pos = line.find("'",pos+1)

                            elif line[pos] == '"':
                                pos = line.find('"',pos+1)

                            elif line[pos] == comment_syntax[0]:
                                counter_dict["single_comments"] += 1
                                counter_dict["todos"] += line[(pos+1):].count(TODO)
                                break
                            elif pos == -1:
                                break
                            pos += 1

                else:
                    # This is jumping to only code or an empty line
                    # check if we just exited a block
                    if bool_previous_comment and bool_active_block:
                        counter_dict["block_comments"] +=1
                        counter_dict["block_comment_lines"] += block_counter_temp
                        #print("test",block_counter_temp,"--",line)
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
    
    # TODO: Implement block only syntax like HTML: <!-- ... -->
    def comment_block(self,comment_syntax):
        # Local variables incrementation faster than instance incrementation, update when done
        counter_dict = {"loc":0, "tot_comments":0, "single_comments": 0,
                        "block_comment_lines":0, "block_comments":0, "todos":0}

        # This should be pretty easy, simply a combination of a little of both. I didn't have time
        # to implement this method but instead, I implemented the other 2 that are much harder.
        return counter_dict

    def comment_block_single(self,comment_syntax):
        # Local variables incrementation faster than instance incrementation, update when done
        counter_dict = {"loc":0, "tot_comments":0, "single_comments": 0,
                        "block_comment_lines":0, "block_comments":0, "todos":0}

        pos_single_len = len(comment_syntax[0])
        pos_multi_len_open = len(comment_syntax[1][0])
        # pos_multi_len_close = len(comment_syntax[1][1]) might be useful in optimization

        with open(self.filename, 'r') as active_file:
            bool_active_block = False     # Keep track if currently in an active block
            block_counter_temp = 0

            for line in active_file:
                counter_dict["loc"] +=1
                line = line.strip()

                # Check if line starts with comment: block or solo
                if line.startswith(comment_syntax[0]):
                    counter_dict["todos"] += line.count(TODO)
                    counter_dict["single_comments"] +=1
                
                elif line.startswith(comment_syntax[1][0]):
                    block_counter_temp += 1
                    counter_dict["todos"] += line.count(TODO)
                    bool_active_block = True

                    if comment_syntax[1][1] in line:
                        counter_dict["block_comments"] += 1
                        counter_dict["block_comment_lines"] += 1
                        block_counter_temp = 0
                        bool_active_block = False
                
                elif comment_syntax[0] in line:
                    if not bool_active_block: # inline single comment not */ // */
                    # Assuming strings start with " or ', must determine if comment
                    # is part of a string or not. e.g: print("//string") //comment
                        pos = 0
                        while pos < len(line):
                            if line[pos] == "'":
                                pos = line.find("'",pos+1)

                            elif line[pos] == '"':
                                pos = line.find('"',pos+1)

                            elif line[pos:pos+pos_single_len] == comment_syntax[0]:
                                counter_dict["single_comments"] += 1
                                counter_dict["todos"] += line[(pos+pos_single_len):].count(TODO)
                                break
                            elif pos == -1:
                                break
                            pos += 1
                        

                elif comment_syntax[1][0] in line:
                    if not bool_active_block: # inline single comment
                    # Assuming strings start with " or ', must determine if comment
                    # is part of a string or not. e.g: print("//string") //comment
                        pos = 0
                        while pos < len(line):
                            if line[pos] == "'":
                                pos = line.find("'",pos+1)

                            elif line[pos] == '"':
                                pos = line.find('"',pos+1)

                            elif line[pos:pos+pos_multi_len_open] == comment_syntax[1][0]:
                                block_counter_temp += 1
                                bool_active_block = True
                                counter_dict["todos"] += \
                                    line[(pos+pos_multi_len_open):].count(TODO)
                                break

                            elif pos == -1:
                                break

                            pos += 1

                        if comment_syntax[1][1] in line[(pos+pos_multi_len_open):]:
                            counter_dict["block_comments"] += 1
                            counter_dict["block_comment_lines"] += 1
                            block_counter_temp = 0
                            bool_active_block = False

                elif bool_active_block:
                    block_counter_temp += 1
                    if comment_syntax[1][1] in line:
                        counter_dict["block_comments"] += 1
                        counter_dict["block_comment_lines"] += block_counter_temp
                        block_counter_temp = 0
                        bool_active_block = False

        counter_dict["tot_comments"] = \
            counter_dict["block_comment_lines"] + counter_dict["single_comments"]

        return counter_dict
    
    # Main method for comment analysis
    def analyze_code(self):
        """ Analyze code depending on syntax:
        
        Options: 
        True = BLOCK_SINGLE, False = SINGLE_ONLY, BLOCK_ONLY
        """
        if self.file_extension != False:
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
            else:
                print("ERROR: Syntax Condition not supported")
                return 0
            self.counter_dict = counter_dict
            self.__check_in_status = True
        else:
            print("ERROR: File extension not supported, see extensions.py")

    def analysis_output(self, option:str):
        """ Output code analysis results:
        
        Options: 'terminal', 'JSON' (Python Dict), 'tuple', etc...
        Add other options for output and format it as required.
        (for now, only terminal is implemented)
        TODO: Implement multiple output formatting as required
        """
        counter_dict = self.counter_dict # Prevent multiple calls to the instance dict

        if option == 'terminal':
            # This printing method works with Python 2.6+
            for key,value in counter_dict.items():
                print("Total # of %s: %d" % (OUTPUT_FORMAT[key],value))
        if option == 'JSON':
            return self.counter_dict
        # Other options can be implemented as required