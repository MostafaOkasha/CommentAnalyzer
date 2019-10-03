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
BLOCK_ONLY = 'BLOCK_ONLY'
SINGLE_ONLY = False
SINGLE_BLOCK = True

# Determine language syntax group by looking up file extensions
# Each tuple value bool --> True if support Block-Comments

                                                                # File type:
EXTENSIONS_STYLE = {'c'     : ('c_syntax',SINGLE_BLOCK),        # C
                    'cpp'   : ('c_syntax',SINGLE_BLOCK),        # C++
                    'cxx'   : ('c_syntax',SINGLE_BLOCK),        # C++ variation
                    'cc'    : ('c_syntax',SINGLE_BLOCK),        # C variation
                    'cs'    : ('c_syntax',SINGLE_BLOCK),        # C#
                    'asmx'  : ('c_syntax',SINGLE_BLOCK),        # C# variation
                    'h'     : ('c_syntax',SINGLE_BLOCK),        # C header
                    'hpp'   : ('c_syntax',SINGLE_BLOCK),        # C++ header
                    'js'    : ('c_syntax',SINGLE_BLOCK),        # JavaScript
                    'java'  : ('c_syntax',SINGLE_BLOCK),        # Java
                    'jav'   : ('c_syntax',SINGLE_BLOCK),        # Java variation
                    'j'     : ('c_syntax',SINGLE_BLOCK),        # Java variation
                    'ino'   : ('c_syntax',SINGLE_BLOCK),        # Arduino
                    'scala' : ('c_syntax',SINGLE_BLOCK),        # Scala
                    'css'   : ('c_syntax',SINGLE_BLOCK),        # CSS - Cascading StyleSheet
                    'sass'  : ('c_syntax',SINGLE_BLOCK),        # Syntaticall Awesome StyleSheet
                    'hss'   : ('c_syntax',SINGLE_BLOCK),        # CSS variation
                    'hss'   : ('c_syntax',SINGLE_BLOCK),        # CSS variation
                    'less'  : ('c_syntax',SINGLE_BLOCK),        # CSS variation
                    'ccss'  : ('c_syntax',SINGLE_BLOCK),        # CSS variation
                    'pcss'  : ('c_syntax',SINGLE_BLOCK),        # CSS variation
                    'as'    : ('c_syntax',SINGLE_BLOCK),        # Action Script
                    'swift' : ('c_syntax',SINGLE_BLOCK),        # Swift
                    's'     : ('c_syntax',SINGLE_BLOCK),        # GAS Assembly

                    'py'    : ('hash_syntax',SINGLE_ONLY),      # Python
                    'sh'    : ('hash_syntax',SINGLE_ONLY),      # Unix Shell
                    'bash'  : ('hash_syntax',SINGLE_ONLY),      # Bash Script
                    'zsh'   : ('hash_syntax',SINGLE_ONLY),      # Unix Shell/Bash variation
                    'ksh'   : ('hash_syntax',SINGLE_ONLY),      # Unix Shell/Bash variation
                    'csh'   : ('hash_syntax',SINGLE_ONLY),      # Unix Shell/Bash variation
                    'pl'    : ('hash_syntax',SINGLE_ONLY),      # Perl
                    'r'     : ('hash_syntax',SINGLE_ONLY),      # R Language

                    'html'  : ('xml_syntax',BLOCK_ONLY),        # HTML
                    'htm'   : ('xml_syntax',BLOCK_ONLY),        # HTML variation
                    'xhtml' : ('xml_syntax',BLOCK_ONLY),        # HTML variation
                    'jhtml' : ('xml_syntax',BLOCK_ONLY),        # HTML variation
                    'xml'   : ('xml_syntax',BLOCK_ONLY),        # XML
                    'rss'   : ('xml_syntax',BLOCK_ONLY),        # XML Variation
                    'svg'   : ('xml_syntax',BLOCK_ONLY),        # XML Variation
                    
                    'matlab': ('matlab_syntax',SINGLE_BLOCK),   # Matlab
                    'yaws'  : ('matlab_syntax',SINGLE_ONLY),    # Erlang
                    'tex'   : ('matlab_syntax',SINGLE_ONLY),    # LaTeX

                    'asp'   : ('asp_syntax',SINGLE_ONLY),       # ASP Classic comments are ' no BLOCK COMMENTS
                    'aspx'  : ('asp_syntax',SINGLE_BLOCK),      # ASP.NET ' for single and <%-- This is a Comment --%> for block
                    'axd'   : ('asp_syntax',SINGLE_BLOCK),      # ASP.NET variation
                    'asx'   : ('asp_syntax',SINGLE_BLOCK),      # ASP.NET variation
                    'asmx'  : ('asp_syntax',SINGLE_BLOCK),      # ASP.NET variation
                    'ashx'  : ('asp_syntax',SINGLE_BLOCK),      # ASP.NET variation
                    
                    'asm'   : ('assembly_syntax',SINGLE_ONLY),  # Assembly uses ; for single comments only

                    'adb'   : ('ada_syntax',SINGLE_ONLY),       # ADA file uses -- for comments, no block comments
                    'ads'   : ('ada_syntax',SINGLE_ONLY),       # ADA variation

                    'ps1'   : ('pwrshl_syntax',SINGLE_BLOCK),   # PowerShell # single and <# #> for multiple

                    'vb'    : ('vb_syntax',SINGLE_ONLY),        # Visual Basic syntax, every comment needs to start with ' and no block comment support available
                    
                    'rb'    : ('rb_syntax',SINGLE_BLOCK),       # Ruby - # multi: =begin ... =end
                    'rhtml' : ('rb_syntax',SINGLE_BLOCK),       # Ruby Variation

                    # The following formats have not been completed yet.
                    'hs'    : ('hs_syntax',BLOCK_ONLY),       # Haskell file {- ... -}
                    
                    # TODO: Implementing dual syntax coverage
                    # PHP file uses c style as well as #
                    'php'   : ('c_syntax',DUAL_SYNTAX,'hash_syntax'),
                    'sql'   : ('sql_syntax',DUAL_SYNTAX,'dash_syntax') # SQL files have multiple commenting syntax c_syntax and -- for a comment
                    }

# Dictionary of file type extensions and their appropriate comment tags. 
# Grouping different comment style syntax based on EXTENSIONS_STYLE
STYLE_SYNTAX = {'c_syntax'        : ('//',('/*','*/')),
                'hash_syntax'     : ('#'),
                'assembly_syntax' :(';'),
                'pwrshl_syntax'   : ('#',('<#','#>')),
                'xml_syntax'      : ('<!--','-->'),
                'ada_syntax'      : ('--'),
                'matlab_syntax'   : ('%',('%{','%}')),
                'asp_syntax'      : ("'",('<%--','--%>')),
                'rb_syntax'       : ('-',('=begin','=end')),
                'vb_syntax'       : ("'")
                }

# Printing format for analysis_output. Modify and add as required.
OUTPUT_FORMAT = {'loc' : 'lines',
                 'tot_comments' : 'comment lines',
                 'single_comments' : 'single line comments',
                 'block_comment_lines' : 'comment lines within block comments',
                 'block_comments' : 'block line comments',
                 'todos' : 'TODO\'s'
                 }