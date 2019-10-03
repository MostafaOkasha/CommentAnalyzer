#!/usr/bin/env python
# encoding: utf-8
"""
extensions.py
"""

# Assuming TODO is shared among all languages
TODO = 'TODO'

# For languages that use multiple commenting syntax
# TODO: Implement dual syntax commenting analysis
DUAL_SYNTAX = 'DUAL_SYNTAX'

# For languages that have only single line comments and different begin and end comment syntax
DIFF_SINGLE = 'DIFF_SINGLE'
# Determine language syntax group by looking up file extensions
# Each tuple value bool --> True if support Block-Comments

                                                         # File type:
EXTENSIONS_STYLE = {'c'     : ('c_syntax',True),         # C
                    'cpp'   : ('c_syntax',True),         # C++
                    'cxx'   : ('c_syntax',True),         # C++ variation
                    'cc'    : ('c_syntax',True),         # C variation
                    'cs'    : ('c_syntax',True),         # C#
                    'asmx'  : ('c_syntax',True),         # C# variation
                    'h'     : ('c_syntax',True),         # C header
                    'hpp'   : ('c_syntax',True),         # C++ header
                    'js'    : ('c_syntax',True),         # JavaScript
                    'java'  : ('c_syntax',True),         # Java
                    'jav'   : ('c_syntax',True),         # Java variation
                    'j'     : ('c_syntax',True),         # Java variation
                    'ino'   : ('c_syntax',True),         # Arduino
                    'scala' : ('c_syntax',True),         # Scala
                    'css'   : ('c_syntax',True),         # CSS - Cascading StyleSheet
                    'sass'  : ('c_syntax',True),         # Syntaticall Awesome StyleSheet
                    'hss'   : ('c_syntax',True),         # CSS variation
                    'hss'   : ('c_syntax',True),         # CSS variation
                    'less'  : ('c_syntax',True),         # CSS variation
                    'ccss'  : ('c_syntax',True),         # CSS variation
                    'pcss'  : ('c_syntax',True),         # CSS variation
                    'as'    : ('c_syntax',True),         # Action Script
                    'swift' : ('c_syntax',True),         # Swift
                    's'     : ('c_syntax',True),         # GAS Assembly

                    'py'    : ('hash_syntax',False),     # Python
                    'sh'    : ('hash_syntax',False),     # Unix Shell
                    'bash'  : ('hash_syntax',False),     # Bash Script
                    'zsh'   : ('hash_syntax',False),     # Unix Shell/Bash variation
                    'ksh'   : ('hash_syntax',False),     # Unix Shell/Bash variation
                    'csh'   : ('hash_syntax',False),     # Unix Shell/Bash variation
                    'pl'    : ('hash_syntax',False),     # Perl
                    'r'     : ('hash_syntax',False),     # R Language

                    'html'  : ('xml_syntax',DIFF_SINGLE),# HTML
                    'htm'   : ('xml_syntax',DIFF_SINGLE),# HTML variation
                    'xhtml' : ('xml_syntax',DIFF_SINGLE),# HTML variation
                    'jhtml' : ('xml_syntax',DIFF_SINGLE),# HTML variation
                    'xml'   : ('xml_syntax',DIFF_SINGLE),# XML
                    'rss'   : ('xml_syntax',DIFF_SINGLE),# XML Variation
                    'svg'   : ('xml_syntax',DIFF_SINGLE),# XML Variation
                    
                    'matlab': ('matlab_syntax',True),    # Matlab
                    'yaws'  : ('matlab_syntax',False),   # Erlang
                    'tex'   : ('matlab_syntax',False),   # LaTeX

                    # TODO: Implement the following syntaxes and perform unit tests
                    # The following formats have not been completed yet.
                    'asm'   : ('assembly_syntax',False), # Assembly uses ; for single comments only
                    ##
                    'adb'   : ('ada_syntax',False),      # ADA file uses -- for comments, no block comments
                    'ads'   : ('ada_syntax',False),      # ADA variation
                    ##
                    'ps1'   : ('pwrshl_syntax',True),    # PowerShell # single and <# #> for multiple
                    ##
                    'vb'    : ('vb_syntax',False),       # Visual Basic syntax, every comment needs to start with ' and no block comment support available
                    ##
                    'hs'    : ('hs_syntax',False),       # Haskell file {- ... -}
                    ##
                    'asp'   : ('asp_syntax',False),      # ASP Classic comments are ' no BLOCK COMMENTS
                    'aspx'  : ('asp_syntax',True),       # ASP.NET ' for single and <%-- This is a Comment --%> for block
                    'axd'   : ('asp_syntax',True),       # ASP.NET variation
                    'asx'   : ('asp_syntax',True),       # ASP.NET variation
                    'asmx'  : ('asp_syntax',True),       # ASP.NET variation
                    'ashx'  : ('asp_syntax',True),       # ASP.NET variation
                    ##
                    'rb'    : ('rb_syntax',True),        # Ruby - # multi: =begin ... =end
                    'rhtml' : ('rb_syntax',True),        # Ruby Variation
                    ##

                    # TODO: Implementing dual syntax coverage
                    # PHP file uses c style as well as #
                    'php'   : ('c_syntax',DUAL_SYNTAX,'hash_syntax'),
                    ##
                    'sql'   : ('sql_syntax',DUAL_SYNTAX,'dash_syntax') # SQL files have multiple commenting syntax c_syntax and -- for a comment
                    }

# Dictionary of file type extensions and their appropriate comment tags. 
# Grouping different comment style syntax based on EXTENSIONS_STYLE
STYLE_SYNTAX = {'c_syntax'      : ('//',('/*','*/')),
                'hash_syntax'   : ('#'),
                'xml_syntax'    : ('<!--','-->'),
                'matlab_syntax' : ('%',('%{','%}'))
                }

# Printing format for analysis_output. Modify and add as required.
OUTPUT_FORMAT = {'loc' : 'lines',
                 'tot_comments' : 'comment lines',
                 'single_comments' : 'single line comments',
                 'block_comments' : 'comment lines within block comments',
                 'block_comment_lines' : 'block line comments',
                 'todos' : 'TODO\'s'
                 }