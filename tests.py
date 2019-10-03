# Author:       Mostafa Okasha (okashm@mcmaster.ca)
# Affiliation:  CapitalOne - Technical Assessment

import unittest
from commentanalyzer import *

''' CommentAnalyzer Class tests

'''

class CommentAnalyzerTest(unittest.TestCase):
    
    def test_1_file_extension(self):
        """Capability to detect valid file extensions

        """
        filename = "gitig.nore.c++"
        test_class = CommentAnalyzer(filename)
        result = test_class.file_extension
        self.assertEqual(result, "c++")

    def test_2_file_extension(self):
        """
        filename with
        """
        filename = ".gitig.nore.c++"
        test_class = CommentAnalyzer(filename)
        result = test_class.file_extension
        self.assertEqual(result, False)

    def test_3_file_extension(self):
        """
        Test CommentAnalyzer class's capability to detect valid file extensions
        """
        filename = "LICENSE"
        test_class = CommentAnalyzer(filename)
        result = test_class.file_extension
        self.assertEqual(result, False)

    def test_4_file_extension(self):
        """
        Test CommentAnalyzer class's capability to detect valid file extensions
        """
        filename = "commentanalyzer.py"
        test_class = CommentAnalyzer(filename)
        result = test_class.file_extension
        self.assertEqual(result, "py")

    def test_1_loc_count(self):
        """
        Test CommentAnalyzer class's capability to detect valid file extensions
        """
        filename = "extensions.py"
        test_class = CommentAnalyzer(filename)
        test_class.analyze_code()
        result = test_class.counter_dict["loc"]
        self.assertEqual(result, 15)




if __name__ == '__main__':
    #unittest.main()
    print("extension.py")
    filename1 = "extensions.py"
    test_class = CommentAnalyzer(filename1)
    test_class.analyze_code()
    test_class.analysis_output('terminal')

    # extensions.py solution:
    # 115 lines of code (CORRECT)
    # total num of comments: 81 (82, it's counting '#' FIX)
    # single comments: 71
    # num of lines in blocks: 12 (DONE)
    # num of blocks: 6 = 6 (DONE)
    # num of todos: 3 = 4
    

    print(" ")
    print(" ")
    print("Test4")
    filename2 = "tests/test_cases/test4.py"
    test_class2 = CommentAnalyzer(filename2)
    test_class2.analyze_code()
    test_class2.analysis_output('terminal')
    # test 4 solution

    # 25 lines of code (CORRECT)
    # total num of comments: 14
    # single comments: 7
    # num of lines in blocks: 7
    # num of blocks: 3
    # num of todos: 6


    print(" ")
    print(" ")
    print("Test3")
    filename3 = "tests/test_cases/test3.py"
    test_class3 = CommentAnalyzer(filename3)
    test_class3.analyze_code()
    test_class3.analysis_output('terminal')

    # test 3 solution

    #Total # of lines: 61 = 61 (DONE)
    #Total # of comment lines: 19 = 16
    #Total # of single line comments: 9 = 7
    #Total # of comment lines within block comments: 10 = 9
    #Total # of block line comments: 3 = 3 (DONE)
    #Total # of TODO’s: 3 = 3 (DONE)
    