<h1 style="text-align:center ; color:navy">CommentAnalyzer</h1>

<h6 style="text-align:center">Note: This program is part of the Capital One Technical Assessment</h6>


<br>

## Introduction
The CommentAnalyzer Python module allows any coding file with a valid extension to be scanned and 
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

### Installation

### Download Resources

### Running Demo

## Testing Scope

## Thought Process

##### I. Breaking down the program requirements
###### First, I identify that the program is required to do the following:
1. Program runs every time engineer checks in code.
2. Counts total LOC (lines of code). (DONE)
3. Counts total lines of comments.
4. After identifying a comment, it segregates the total number of single line and multi-line comments
5. lines of code with trailign comments count as both LOC and a comment.
6. Counts the total number of TODOs in all comments.
7. **NOTE:** File could be any valid program file. (DONE)
8. Files without an extension could be ignored! (DONE)
9. Files starting with a '.' can also be ignored. (DONE)
<br>

##### II. Adding necessary Features
###### These will enhance scalability and provide a better program overall:

10. Allow the addition of other file extensions and comment syntax without the need for extra code.
11. Handle huge files without bottlenecking the system.
12. Handle the extreme Edge cases defined below (nested comments, weird variations, etc..)
13. Be easily integrated into an existing system.

Satisfying the above 13 requirements and more! 


## Assumptions
Since the programming will be recieving the file directly, we should not worry about 
leaks and securities within the class. This is convenient.
we can assume... blah blah

Block comments starting with a # are considered to be block comments if they take
a single line each and come right after each other (2+)

TODO: Needs to have the colon after



### Scalability
have a dict of file extensions and comments and comment blocks for different file extensions. 
This allows scalability for adding file types and different types.
### Maintainability




## Design Decisions
The convention is to always declare your instance variables in the initializer. 
This is to prevent something weird from happenning even if it takes more memory.  
<br>
Tested: memory tests with and without?

Local variables in functions are accessed more quickly than global variables
For this reason, having an instance variable as a counter for
each LOC/COMMENT/inline/block that's 4 instance variables
and potentially 4 times LOC slower access. It is best
to keep the instance variables set as 0 initially and then
when running the code, increment them locally then when done
post the final value to the instance variable equivelant.

file name validity check; checking first . faster than checking
. in entire name. This is simple, doesn't take
much processing anyway, very minute. but over
10,000+ tests might be problematic?
WHY NOT!


Built using Test Driven Development. Each method was
tested against all edge cases before
proceeding. Given the time constraints of the
assessment, this ensured working code
from teh very start.


## Scope

## Tests

## Edge Cases
// comment
/* comment */
// comment 1 //comment 2
/* comment //comment */
// comment /* comment */
print("//comment")
^ all rules should pass for this case as well.
""" comment """ comment """ comment """
the second comment is not actually in a comment,
even though it's trying to be. The first """ terminates
the comment

#//
#// /*
#some code()
#// */

file name: a.tar.gz
what then?

NESTED COMMENTS!!!!!!!!!!!!!!!!


some languages are more complex,
like COBOL: Astreisk in position 7 * to show that it's a comment.
This is a little more tricky and would require a seperate small function to determine
this. It's as simple as identifying the location of position 7 and determining 
that this line is a comment. Simple, but since it's barely used is out of the scope
of this program.
same with Basic, COBOL: REM comment and Fortran: which uses letter C  as comment

other languages to consider:

ALGOL 60: ;
Assembly: ;
ADA, mySQL: --
FORTRAN90: !
simple commenting, can be added to the extensions.py file.

Lua: -- single comment (just like Ada, Eiffel, Haskell, SQL, VHDL). block comment: --[[ ... ]]

For HTML when having a built in script:
\< script \>
then depending on script type inside, we need to be able to determine comment types
within that script and count it as that language's comment
example: script="javaScript"
for that portion of code, run the javaScript commenting style



## Adaptability
adapting to different file types and comment structures depending on the file type.
if the file type is unknown (just a name then what then?)

These methods are required anyway so might as well
make them accessible and usable to perform other functionalities
as well.
on why to initiate the object with or without a file name
## Installation

```console
git clone https://github.com/MostafaOkasha/CommentAnalyzer
cd CommentAnalyzer
bundle install
bundle exec jekyll serve
```

You can use <kbd>Option</kbd><kbd>C</kbd> to stop the server.

Check out the Jekyll installation page for more information on how to get started. You might face a few issues with the Gemfile if you're trying to clone this website, what I recommend is to download any Jekyll layout/theme and manually move over all your static HTML/CSS code while following the appropriate Jekyll structure.


---
###### Author: Mostafa Okasha (okashm@mcmaster.ca)
---

## Cheers!

Note: Built using Jekyll, Node.js, HTML5, CSS3

# License
