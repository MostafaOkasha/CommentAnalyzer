# CommentAnalyzer

###### Note: This program is part of the Capital One Technical Assessment


<br>

## Introduction
The CommentAnalyzer Python3+ module allows any coding file with a valid extension
**with over 47 extensions supported** to be scanned and 
analyzed in order to count the following total numbers:
1. LOC (lines of code)
2. Comments (all)
3. Inline Comments
4. Multi-line comments (Block)
5. TODOs

This can be interpretted and run when new code is submitted by a developer into 
the build pipeline in order to encourage good practices and commenting.  
  
Be more self-aware of your commenting and install the CommentAnalyzer module into your automated build pipeline
checks!

## Getting Started

### Requirements
**extensions.py** is the only requirement. It contains all the supported file extensions 
and language syntax for comments. **See Configurations below for more detail**
### Installation
Download the package from the links below and either do one of the following:
1. Add **commentanalyzer.py** *and* **extensions.py** to Python Path
2. Place both these files in the same directory where your program needs them.
<br>

Then do the following:
```python
from commentanalyzer import *
or
import commentanalyzer
```
Don't worry, it's a single class and the probability of a name clash is probably low!

### How to use
It's very simple!

```python
from commentanalyzer import *

# Example:
filename = "tests/test_cases/test2.js"
test_class = CommentAnalyzer(filename)
test_class.analyze_code()
test_class.analysis_output('terminal')

# Output:
'''
Total # of lines: 40
Total # of comment lines: 23
Total # of single line comments: 5
Total # of comment lines within block comments: 18
Total # of block line comments: 4
Total # of TODO's: 1
'''
```

**Rule #1:** file name must have an extension somehow and not start with a '.'  
*e.g: ".ignore", ".ignore.java", "wowfile" wouldn't work**

**Rule #2:** Make sure the language you want to analyze is supported!  
-- **We support over 47 languages** and guess what? You can easily add your own extension 
and language syntax.

### Configurations
Here's how you can easily add your own language/extension and language comment syntax 
support.
Head over to:
##### extensions.py
When setting a new extension, check to see if the language commenting syntax is  
supported, if not you could add it similar to the example below.

There are 4 constants that can be set similar to the first line in the example below.  
These are:

1. BLOCK_ONLY: Languages that only have comments in the form of blocks. E.g: HTML: 
\<!-- comment \-->
2. SINGLE_ONLY: Languages that only have one symbol for comments. Python --> #
3. SINGLE_BLOCK: Languages that have both single comments and block comments. e.g: c
4. DUAL_SYNTAX: Languages that use 2 seperate language commenting syntax. 
**This isn't supported yet**

```python
STYLE_SYNTAX = {'cs'    : ('c_syntax',SINGLE_BLOCK), # C#
                others...}        

# Where the language syntax is as follows
OUTPUT_FORMAT = {'c_syntax'        : ('//',('/*','*/')),
                 others...}

# If I have my own language that uses single and block comments
# and it has a unique commenting syntax I can add it as follows:

STYLE_SYNTAX = {'cs'    : ('c_syntax',SINGLE_BLOCK), # C#
                'mopp'    : ('okasha_syntax',SINGLE_BLOCK), # NEW!
                 others...}        

# Where the language syntax is as follows
OUTPUT_FORMAT = {'c_syntax'        : ('//',('/*','*/')),
                 'okasha_syntax'   : ('^',('!^','^!')), #NEW!  
                 others...}

# okasha_syntax would be for a language as follows:
''' okasha_syntax_

^ This is a single comment

!^ This is
 ^ a multi
 ^ line comment ^!
create new(okasha_class) ^ In-line comment
'''
```
### Download Resources

1. *Google Drive* --> https://drive.google.com/file/d/1ekBpNlebM2eQukTn40k9oh0ukQTrNwx5/view?usp=sharing


## Testing Scope
**See tests.py** for a list of all unit tests among other full scope tests
## Thought Process

##### I. Breaking down the program requirements
###### First, I identify that the program is required to do the following:
1. Program runs every time engineer checks in code.
2. Counts total LOC (lines of code).
3. Counts total lines of comments.
4. After identifying a comment, it segregates the total number of single line and multi-line comments
5. lines of code with trailign comments count as both LOC and a comment.
6. Counts the total number of TODOs in all comments.
7. **NOTE:** File could be any valid program file.
8. Files without an extension could be ignored!
9. Files starting with a '.' can also be ignored.
<br>

##### II. Adding necessary Features
###### These will enhance scalability and provide a better program overall:

10. Allow the addition of other file extensions and comment syntax without the need for extra code.
11. Handle huge files without bottlenecking the system.
12. Handle the extreme Edge cases defined below (nested comments, weird variations, etc..)
13. Be easily integrated into an existing system.

For it to run everytime code is checked in, it must be a portable module that can 
be easily imported. A Python class module seemed suitable for this although a C++ 
version of this class can be easily created for easier integration with C based systems 
that do not support running external Python modules.

Initially, I identified many, many scenarios where the code would break.


## Assumptions
1. Since the programming will be recieving the file directly, we should not worry about 
leaks and securities within the class. This is convenient. I assumed that all strings 
will use either single quotes or double quotes (' or "). This is ideal since when 
checking for in-line comments, I consider the scenario where something like this 
could occur:

2. I assumed that for a single comment to be part of a block, the space prior to the 
comment is irrelavent.

3. Comment lines can have multiple TODOs. This is also counted during the analysis.


```python
    print("hello#") # Comment
```
I check and make sure that the comment is not inside a source code string.

Block comments starting with a # are considered to be block comments if they take
a single line each and come right after each other two times or more.
```python
# Block comment
# Block comment

# Single comment

def my_func(self) # in-line comment_
```




## Maintainability
Having simple methods that are seperate and that do not depend on one another 
allows for changes to be easily made to the class without affecting the entire 
functionality of other class methods. I built this class while thinking about LEGO.



## Design Decisions
Some decisions and thoughts I had while building this program:

1. The convention is to always declare your instance variables in the initializer. 
This is to prevent something weird from happenning even if it takes more memory.  

2. Local variables in functions are accessed more quickly than global variables
For this reason, having an instance variable as a counter for
each LOC/COMMENT/inline/block that's 4 instance variables
and potentially 4 times slower access. It is best
to keep the instance variables set as 0 initially and then
when running the code, increment them locally then when done,
post the final value to the instance variable equivelant.

3. A lot of design decisions are mentioned within the code.

4. How to deal with some weird edge cases. This is explained more below.
```python
    print("abc#def#") # Comment inside a # comment and TODO: help
```
I start from reading each individual character from left to right, once I find 
a string literal (' or "), I jump the index to the next occurance of that apostraphe 
signalling the end of the string in order to avoid counting comments inside a string as
comments. 


This program was built using Test Driven Development (TDD). Each method was
tested against all edge cases before proceeding. Given the time constraints of the
assessment, this ensured working code early on.


## Scope
Consider this:
```python
    print("#hello#") # Comment inside a # comment and TODO: help
```
My program deals with this. Here are some other edge cases I considered.


### Edge Cases
Some edge cases I considered:
```c
// comment 1 //comment 2
/* comment //comment */
print("//comment")

// /*
print(this is actually a comment)
*/ // BAM! Another comment

NESTED COMMENTS!!!!!!!!!!!!!!!!

```

some languages are more complex,
like COBOL: Astreisk in position 7 * to show that it's a comment.
This is a little more tricky and would require a seperate small function to determine
this. It's as simple as identifying the location of position 7 and determining 
that this line is a comment. Simple, but since it's barely used is out of the scope
of this program.
same with Basic, COBOL: REM comment and Fortran: which uses letter C  as comment

#### IMPORTANT
Considering HTML, when you do something like:
```html
<body>
    <span> hello </span> <!-- comment -->
</body>

<script>
// some javaScript comment...now what?

</script>
```

Depending on script type inside, we need to be able to determine comment types
within that script and count it as that language's comment.  

**The solution:**  
For that portion of code, identify that the program has entered a script and treat
the commenting here differently (well, java == c_syntax commenting)

A lot of edge cases are considered but due to the added complexity, are out of the 
scope of this program.



## Adaptability

Adapting to different file types and comment structures depending on the file type was 
one of the main decision factors when designing this program. The idea was that a 
template code that takes in any commenting format would be ideal. I realized that
multiple languages have very different commenting syntax but fell into 4-5 categories 
of commenting style:

1. Block comments only: Like HTML \<!-- comment -->
2. Single comments only: Like Python #
3. Both: Like C (// for single) and (/* block */)

But there was more... Some languages had 2 commenting styles? PHP I'm talking to you!
And many languages used a location based comment style.   
ALGOL and FORTRAN need to have their comment symbol in a specific location for it to
count as a comment, which adds a nice flavor of complexity to this program. 
Unfortunately, this wasn't taken care of here!

By allowing anyone to add any comment style and extension, the scope of this program
are limitless!

---
###### Author: Mostafa Okasha (okashm@mcmaster.ca)
---

## Cheers!

Built using Python 3.7

