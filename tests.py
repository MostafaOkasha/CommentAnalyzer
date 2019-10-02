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
        file_name = "gitig.nore.c++"
        test_class = CommentAnalyzer(file_name)
        result = test_class.file_extension
        self.assertEqual(result, "c++")

    def test_2_file_extension(self):
        """
        Test CommentAnalyzer class's capability to detect valid file extensions
        """
        file_name = ".gitig.nore.c++"
        test_class = CommentAnalyzer(file_name)
        result = test_class.file_extension
        self.assertEqual(result, False)

    def test_3_file_extension(self):
        """
        Test CommentAnalyzer class's capability to detect valid file extensions
        """
        file_name = "LICENSE"
        test_class = CommentAnalyzer(file_name)
        result = test_class.file_extension
        self.assertEqual(result, False)

if __name__ == '__main__':
    unittest.main()
