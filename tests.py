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

    filename = "extensions.py"
    test_class = CommentAnalyzer(filename)
    test_class.analyze_code()
    test_class.analysis_output('terminal')