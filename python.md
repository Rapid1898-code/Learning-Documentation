# PYTHON
---

#### MODULE, GENERAL [jump to...](#module-general)
#### VIRTUALENV [jump to...](#virtualenv)
#### SHORTCUTS INTELLIJ IDEA IDE, GITHUB, CHROME, WINDOWS [jump to...](#shortcuts-intellij-idea-ide-github-chrome-windows)
#### OPERATORS, INPUTS, ARGUMENTS [jump to...](#operators-inputs-arguments)
#### RANDOM, SECRETS [jump to...](#random-secrets)
#### STRING [jump to...](#string)
#### REGEX [jump to...](#regex)
#### LIST [jump to...](#list)
#### TUPEL [jump to...](#tupel)
#### DICTIONARY [jump to...](#dictionary)
#### SETS [jump to...](#sets)
#### CONTROL STRUCTURES and ITERATIONS [jump to...](#control-structures-and-iterations)
#### FUNCTIONS, DECORATORS [jump to...](#functions-decorators)
#### GENERATORS, YIELD [jump to...](#generators-yield)
#### LAMBDA, MAP, FILTER [jump to...](#lambda-map-filter)
#### CLASSES, DATACLASSES [jump to...](#classes-dataclasses)
#### TXT FILES [jump to...](#txt-files)
#### JSON FORMAT [jump to...](#json-format)
#### XML FORMAT [jump to...](#xml-format)
#### URLLIB [jump to...](#urllib)
#### MODULE - CSV [jump to...](#module---csv)
#### MOUDLE - ZIPFILE - handling ZIP files [jump to...](#moudle---zipfile---handling-zip-files)
#### MODULE - GSPREAD - API for Google Sheets [jump to...](#module---gspread---api-for-google-sheets)
#### MODULE - OPENPYXL - working with excel worksheets [jump to...](#module---openpyxl---working-with-excel-worksheets)
#### MODULE - XLWINNGS - working on the fly with open excel worksheets [jump to...](#module---xlwinngs---working-on-the-fly-with-open-excel-worksheets)
#### MODULE - WIN32COM - creating worksheets as pdf from xlsx [jump to...](#module---win32com---creating-worksheets-as-pdf-from-xlsx)
#### MODULE - PyPDF2 - working with pdfs [jump to...](#module---pypdf2---working-with-pdfs)
#### MYSQL - MARIADB - HEIDISQL [jump to...](#mysql---mariadb---heidisql)
#### MYSQL - MARIADB - SQL [jump to...](#mysql---mariadb---sql)
#### SQL ALCHEMY [jump to...](#sql-alchemy)
#### SQLITE3 SQL [jump to...](#sqlite3-sql)
#### MODULES - DATES, DATETIME, CALENDAR, TIMEIT, TIME, SYS, CTYPES [jump to...](#modules---dates-datetime-calendar-timeit-time-sys-ctypes)
#### MODULE - CURRENCYCONVERTER - currency conversion [jump to...](#module---currencyconverter---currency-conversion)
#### MODULE - PYCOUNTRY - Countries, Currency, Language [jump to...](#module---pycountry---countries-currency-language)
#### MODULES - SMTPLIB, MIMEText - sending emails [jump to...](#modules---smtplib-mimetext---sending-emails)
#### MODULE - PATHLIB - interacting with the operating system [jump to...](#module---pathlib---interacting-with-the-operating-system)
#### MODULE - OS - interacting with the operating system [jump to...](#module---os---interacting-with-the-operating-system)
#### MODULE - LOGGING [jump to...](#module---logging)
#### MODULE - UNITTEST [jump to...](#module---unittest)
#### MODULE - COLLECTIONS - counter, defaultdic [jump to...](#module---collections---counter-defaultdic)
#### MODULE - ITERTOOLS - products, combinations [jump to...](#module---itertools---products-combinations)
#### MODULE - NUMPY - basis for different other modules [jump to...](#module---numpy---basis-for-different-other-modules)
#### MODULE - PANDAS - analyzing and working with data [jump to...](#module---pandas---analyzing-and-working-with-data)
#### MODULE - MATPLOTLIB - working with charts [jump to...](#module---matplotlib---working-with-charts)
#### MODULE - SELENIUM - browser automatization [jump to...](#module---selenium---browser-automatization)
#### MODULE - BEAUTIFUL SOAP - webscraping [jump to...](#module---beautiful-soap---webscraping)
#### MODULE - REQUESTS - workings with APIs [jump to...](#module---requests---workings-with-apis)
#### MODULE - PYQT - making GUIs [jump to...](#module---pyqt---making-guis)
#### MODULE - TKinter - making GUIs [jump to...](#module---tkinter---making-guis)
#### MODULE - PYGAME - making games [jump to...](#module---pygame---making-games)
#### MODULE - PYTHONCOM - make new formula in excel with python-function [jump to...](#module---pythoncom---make-new-formula-in-excel-with-python-function)
#### MODULE - FLASK, ZAPPA, AWS - making an API [jump to...](#module---flask-zappa-aws---making-an-api)
#### MODULE - ICECREAM - print for debugging [jump to...](#module---icecream---print-for-debugging)
#### PYINSTALLER - generate python programs to executables [jump to...](#pyinstaller---generate-python-programs-to-executables)



---
## MODULE, GENERAL
[jump to top...](#python)<br><br>
<br>Import python module
```markdown
import math
```
Import specific function of a module
```markdown
from math import ceil
```
Import a module with abbreviation
```markdown
import numpy as np
```
When directly called - programm is running from here
```markdown
if __name__ == '__main__':
```
Check which python version is installed
```markdown
python --version
```

<br>Use modules / functions from other folder
```markdown
import sys, os
sys.path.append(os.path.join('C:/', 'Users\path_to_module'))	# Create Path to module
import RapidTechTools as rtt        # Import Module RapidTechTools
```



---
## VIRTUALENV
[jump to top...](#python)<br><br>
<br>Install virtualenv
```markdown
pip install virtualenv
```
Global packages installed
```markdown
pip list
```
Shows where the python-file is (Windows)
```markdown
where python
```
Shows where the python-file is (Linux)
```markdown
which python
```
Create new virtual environment pj1_env
```markdown
virtualenv env
```

<br>Activate environment
```markdown
venv\Scripts\activate
    when activated: pip list    #  Now only shows the installed modules for the virtual environment
    pip install package         #  Only installs in the activated virtual environment
```

<br>Extracts all the modules / dependencies to a txt-file
```markdown
pip freeze --local > requirements.txt
```
Go back to the global environment
```markdown
deactivate
```
Create new virtual env with specific python-version
```markdown
virtualenv -p C:\..path to..\Python37\python.exe py37_env
```
Activate new virtual env named py37_env
```markdown
py37_env\Scripts\activate
```
Shows the used python version in the virtual env
```markdown
python --version
```
Install all the packages from requirements.txt
```markdown
pip install -r requirements.txt
```



---
## SHORTCUTS INTELLIJ IDEA IDE, GITHUB, CHROME, WINDOWS
[jump to top...](#python)<br><br>
Shortcuts Intellij Idea
<br>https://www.shortcutfoo.com/app/dojos/intellij-idea-win/cheatsheet
```markdown
Ctrl /					# Comment / Uncomment line ("/" on numblock)
Ctrl Alt F7				# Find usages
Ctrl F 		   			# Find in File
Ctrl R  	   			# Replace in File
Ctrl Shift R			# Replace in Path (in all Files)
F2						# Jump to the next error
F3						# Find next
Ctrl G					# Goto line
Ctrl D					# Copy / Duplicate lines
Alt Shift Down/Up		# Move line
Ctrl E					# Recent opened files
Ctrl TAB				# Switch windows in IDE
Ctrl (Shift) W			# Select / deselect parts of the code step by step
Alt Enter				# Suggestions for fix error, function informations
Alt 1					# Open the project windows (on the left side)
Alt F7					# Show usage of the variable, function, class
Esc						# Focus back on the editor window
Ctrl Shift -	   		# Collapse all functions
Ctrl -					# Collapse block ("-" on numblock)
Ctrl +					# Expand block ("+" on numblock)
Ctrl A					# Select whole file
Ctrl (Shift) Z			# Undo (backwards) / Redo (forwards)
Ctrl Shift Left			# Select word to the beginning
Ctrl Shift Right		# Select word to the end
Ctrl Left				# Go one word left
Ctrl Right				# Go one word right
Ctrl Y                  # Delete current line
Ctrl Del                # Delete to end of word
Ctrl Backspace          # Delete to beginning of word
lorem + TAB             # Create lorem text for html-code
p>lorem + TAB           # Create lorem text inside <p>-tags
```

<br>Shortcuts Chrome
<br>https://www.makeuseof.com/tag/google-chrome-shortcuts-pdf/
```markdown
F5                  # Refresh site
Ctrl Tab            # Go tab right
Ctrl Shift Tab      # Go tab left
Ctrl F5             # Clear Cache and reload page
```

<br>Shortcuts Win10
<br>https://fossbytes.com/windows-keyboard-shortcuts-cheat-sheet-for-windows-10/
```markdown
Alt Tab         # Focus on other window
Ctrl C          # Copy
Ctrl X          # Cut
Ctrl VALUES     # Paste
```

<br>Git Ignore Files/Folders:
```markdown
when doing a commit - right click + add to .gitignore		# file will be created when not exists
individual file will be ignored
to ignore a whole folder with all files in it - add /* to the folder => eg. /prg/dist/*
```

<br>Add directory to GitHub
```markdown
Select directory => <VCS> => <Import into Version Control> => <Create Git Repository>
Commit the files / new directory
<VCS> => <Import into Version Control> => <Share Project on GitHub>
<VCS> => <Git> => <Push>
```

<br>Change name of repository on github.com
```markdown
select repository => settings => rename
```



---
## OPERATORS, INPUTS, ARGUMENTS
[jump to top...](#python)<br><br>
<br>Import module for math calculations
```markdown
import math
```
Import module for reading arguments from the command line
```markdown
import sys
```
Using some numpy functions
```markdown
import statistics as stat
```
Result without Decimals (=> 2)
```markdown
5 // 2
```
Modulo / Rest of the division (=> 1)
```markdown
7 % 2
```
Assigment of several varaibles
```markdown
d,e,f = 4,5,6
```
Change / swap 2 values
```markdown
a,b = b,a
```
Increase value by one
```markdown
a += 1
```
For better readability - "_" are possible using long num-values (will be ignored)
```markdown
i = 1_000_000
```
Value is rounded to two decimal places => 77.23
```markdown
round (77.2321, 2)
```
Conversion to String / Float / Int
```markdown
str(5), float("5"), int("5")
```
Outputs absolute value => 2
```markdown
abs(-2)
```
Wait for pressing ENTER (or a keyboard stroke) to follow along
```markdown
input("ENTER to continue")
```
Input age and change to int
```markdown
int(input("Alter?"))
```
Returns the type of a variable
```markdown
type(var)
```
Shows all available methods and attributes for the object as list
```markdown
dir(var)
```
Check if x has type format float
```markdown
isinstance(x,float)
```
Check if x has type format string
```markdown
isinstance(x,str)
```
Set var to max-value (float infinite)
```markdown
x = float("inf")
```
Calculates the sqrt of the value => i3
```markdown
math.sqrt(9)
```
Check if a variable exists
```markdown
if "myVar" in locals():
```
Check for argument which is given when starting the program
```markdown
sys.argv[1:].upper()
```
Print "Text" (with a linebreak \n at the end)
```markdown
print("Text")
```
Print with end-statement (next print will be in the same line
```markdown
print("Text", end="-")
```
Print linebreak \n
```markdown
print()
```
python test.py arg1 arg2 arg3
```markdown
example starting program
```
Show the arguments from the command line when starting the program eg. ['test.py', 'arg1', 'arg2', 'arg3']
```markdown
str(sys.argv)
```
Len of the arguments - eg. 4 (program test.py itself and 3 arguments following)
```markdown
len(sys.argv)
```
Find the minimum value => 3
```markdown
min(3,5,7)
```
Find the maximum value => 7
```markdown
max(3,5,7)
```
Find the mean value => 5 (with statistic-module - input must be given as list)
```markdown
stat.mean([3,5,7])
```
Stop program at this point (helpful in test-situations)
```markdown
exit()
```



---
## RANDOM, SECRETS
[jump to top...](#python)<br><br>
random: unsecure, reproducable with seeds
secret: secure, not reproducable<br>
Import random module - fast, but not very secure
```markdown
import random
```
Random int number between 1 and 6 like a cube
```markdown
random.randint(1,6)
```
Random float number between 1 and 3
```markdown
random.uniform(1,3)
```
Random value between 0 and 1 in float format - eg. 0.16394553
```markdown
random.random()
```
Random float in the range from 1 to 10
```markdown
random.uniform(1,10)
```
Random value for standard deviation
```markdown
random.normal(0,1)
```
Choose random entry from a list
```markdown
random.choice(list)
```
Choose 3 random (unique) entries from the list
```markdown
random.sample(list,3)
```
Choose 3 random entries from the list (possible to be the same)
```markdown
random.choices(list,k=3)
```
Shuffle the content of a list
```markdown
random.shuffle(l)
```
Can reproduce the same results (unsecure)
```markdown
random.seed(1)
```
generate a random uppercase 6-char string
```markdown
"".join(random.choices(string.ascii_uppercase, k=6))
```
Import secrets module - for security reasons (is slower)
```markdown
import secrets
```
Random int in the range from 0-10 (10 excluded)
```markdown
secrets.randbelow(10)
```
Random int with 4 bits (highest possible value is 15 - 1111)
```markdown
secrets.randbits(4)
```
Random choice (which is not reproducable)
```markdown
secrets.choice(l)
```



---
## STRING
[jump to top...](#python)<br><br>
ordered, immutable, text representation
s = "this is a test"							# Define a string
s = "this \n text"								# String with linebreak \n
s = "this \t text" 								# String with tab between the words

<br>Define string over more lines in editor with
```markdown
s = '''this \
	and this'''
```

<br>first char of a string
```markdown
c = s[0]
```
last char of a string
```markdown
c = s[-1]
```
Insert variable in string oldest method (%s for string, %i for int, %f for float, %.2f for 2 decimals)
```markdown
s = "text %s bla" % var
```
Insert variable in string old method (:.2f for 2 decimals)
```markdown
s = "text {} bla".format(var)
```
Insert variable in string new method
```markdown
s = f"text {var} bla"
```
Multiple use
```markdown
"{0} like, {0} especially {0} but {1}".format("Joe", "noodles")
```
Returns the index where the text is found
```markdown
s.find ("ist")
```
Counts the occurrence of a text
```markdown
s.count ("i")
```
Return all findings of the search string ("/") in the other string (txt)
```markdown
[n for n in range(len(txt)) if txt.find('/', n) == n]
```
Returns all indexwa as a list (needs import re)
```markdown
[x.start() for x in re.finditer('ist', s)]
```
Lowercase the whole string
```markdown
s = s.lower()
```
Capitalize the whole string
```markdown
s = s.upper()
```
Capitalize the first char
```markdown
s = s.capitalize()
```
Capitalize the first char of all words
```markdown
s = s.title()
```
Check if the string is starting with char "H"
```markdown
s.startswith("H")
```
Check if the string is ending with char "H"
```markdown
s.endswith("H")
```
Split the words in a list
```markdown
s.split()
```
', 1)[0]								=> Split till the first occurence of "=>"
```markdown
s.split('
```
Split sentences after line breaks
```markdown
s.splitlines()
```
Delete all whitespaces at the beginning and the end
```markdown
s = s.strip()
```
Replacement of two strings
```markdown
s = s.replace("e","X")
```
TRUE if the whole string are digits
```markdown
s.isdigit()
```
True if the whole string are no digits
```markdown
s.isalpha()
```
TRUE if string2 is in strings1
```markdown
s2 in s
```
Change string to list with all single chars
```markdown
l = list(s)
```
Convert char to ASCII value
```markdown
ord(char)
```
Convert ASCII value to char (eg. 65=A, 97=a)
```markdown
chr(ascii)
```
Outputs hashvalue oif the string (needs import hashlib)
```markdown
hashlib.md5(s).encode('utf-8')).hexdigest()
```
Execute statement in a string => hello
```markdown
exec(print("hello"))
```
Gives the value of an expression => 4
```markdown
eval("2+2")
```
Reverse a string
```markdown
my_string[::-1]
```
Print string with special characters
```markdown
repr(s)
```



---
## REGEX
[jump to top...](#python)<br><br>
<br>import regex module
```markdown
import re
```
Information about regex handling
```markdown
https://medium.com/factory-mind/regex-tutorial-a-simple-cheatsheet-by-examples-649dc1c3f285
```
Find str with 4xdigits + "-"char + 2xdigits
```markdown
pattern = re.compile("^[0-9]{4}-[0-9]{2}$")
```
Check if pattern matches - <> None when matches
```markdown
pattern.match(s)
```
Find str with 4xdigits + "-"char + 2xdigits
```markdown
pattern2 = re.compile("[0-9]{4}-[0-9]{2}")
```
Find str with 3 to 4 xdigits + "-"char + 2xdigits
```markdown
pattern2 = re.compile("[0-9]{3,4}-[0-9]{2}")
```
Check with fullmatch (^ and $ not necessary) - <> None when matches
```markdown
pattern.fullmatch(s)
```
Char "." has to cherck with "\n" (is a wildcard letter in regex)
```markdown
pattern3 = re.compile ("[0-9]{1}\.[0-9]{3}")
```
Replace all digits in string with blank
```markdown
re.sub("\d","",s)
```
Insert blank before every capitalized word eg. "CostOfRevenue" => "Cost Of Revenue"
```markdown
re.sub(r'([a-z](?=[A-Z])|[A-Z](?=[A-Z][a-z]))', r'\1 ', "txt")
```

Read string an try to match with groups<br>
Define pattern => as many digits (endless) + " " + one lowercase cahr + ":" + as many digits (endless)
```markdown
pattern = "([0-9]+) ([a-z]:([a-z]+)"
```
Check if elem fits the pattern => returns <re.Match object; span=(0, 19), match="3 n: nnnlncrnnnnn">
```markdown
match = re.search(pattern, elem)
```
Assign the value of the first group => 3
```markdown
value = match.group(1)
```
Show the full string => "3 n: nnnlncrnnnnn"
```markdown
all = match.group(0)
```



---
## LIST
[jump to top...](#python)<br><br>
ordered, mutable, allows duplicate elements<br>
Define empty list
```markdown
l = []
```
Define several empty lists (NOT use l1=l=l3=[] => this would be the SAME list)
```markdown
l1,l2,l3,l4 = ([] for i in range(4))
```
check for True if list has an element
```markdown
if l
```
check for False if list is empty (same would be if l == []
```markdown
if not l
```
Define list with content
```markdown
l = [4,5,6]
```
Define list - content is list from 0 to 19
```markdown
l = list(range(20))
```
Define list with 8 empyt strings
```markdown
l = ["" for x in range(8)]
```
Uppercase the whole list
```markdown
l = [x.upper(for x in l)]
```
Define a nested list with 5x5
```markdown
l = [["" for x in range(5)] for x in range(5)]
```
Add both lists together (to a new list)
```markdown
l1 + l2
```
Add 1 element to the list at the back
```markdown
l.append(1)
```
Add several elements to the list at the back
```markdown
l.extend([6,5,4])
```
Insert an element at the index-position 3
```markdown
l.insert(3, "xyz")
```
Returns first index position of element "xyz"
```markdown
l.index("xzy")
```
Delete last element from list
```markdown
l.pop()
```
Delete first element from list
```markdown
l.pop(0)
```
Sort list ascending
```markdown
l.sort()
```
Sort list descending
```markdown
l.sort(reverse=True)
```
Sort list and store it in a different independent list
```markdown
l_sort = sorted(l)
```
Sort list descending and store it in a different independent list
```markdown
l_sort = sorted(l, reverse=True)
```
Check if a list is sorted (by ascending)
```markdown
if sorted(l) == l
```
Check if a list is sorted by descending
```markdown
if sorted(l, reverse=True) == l
```
Sort list by len of elements
```markdown
l.sort(key=len)
```
Define nested list
```markdown
l = [[1,4,3], [2,2,4], [3,1,5]]
```
Sort the nested list for the 2nd element ascending
```markdown
l.sort(key=lambda x: x[1])
```
Sort the nested list for the 2nd element descending
```markdown
l.sort(key=lambda x: x[1], reverse=True)
```
Reverse the complete list
```markdown
l.reverse()
```
Reverse complete list and store it in different independent list
```markdown
l_reverse = reversed(l)
```
Delete element at index position 2
```markdown
del l[2]
```
Delete first element with this value from the list
```markdown
l.remove("abc")
```
Delete complete content of the list (same as l = [])
```markdown
l.clear()
```
Find smallest element in the list
```markdown
min(l)
```
Find greatest element in the list
```markdown
max(l)
```
Find longest string in the list
```markdown
max(mylist, key=len)
```
Find lenght of longest string in the list
```markdown
len(max(mylist, key=len))
```
Sum of all elements in the list
```markdown
sum(l)
```
Pair Sorting from 2 lists (1 with 1, 2 with 2, 3 mit 3, aso.)
```markdown
2xls_sum  = [sum(pair) for pair in zip(l1, l2)]
```
Count of elements in list
```markdown
len(l)
```
Count of occurence of the element "a" in the list
```markdown
l.count("a")
```
No seperate copy of the list (updates in both lists)
```markdown
l2 = l1
```
Separate individual copy of the list (no updates in both lists)
```markdown
l2 = l.copy()
```
Separate individual copy of the list - 2nd variant
```markdown
l2 = l[:]
```
Separate individual copy of the list - 3rd variant
```markdown
l2 = list(l)
```
First element
```markdown
l[0]
```
Last element
```markdown
l[-1]
```
Last 3 elements
```markdown
l[-3:]
```
Elements from index position 2 to 3
```markdown
l[2:4]
```
Elements from 0 to 1 (exclusive index position 2)
```markdown
l[:2]
```
Elements from index position 2 to the end of the list
```markdown
l[2:]
```
Every second element [start:end:step]
```markdown
l[::2]
```
Check if element is in list
```markdown
9 in l
```
Check if any elements from the list are in the string
```markdown
if any(x in string for x in ["ab","cd","de"]):
```
Check if all elements from the list are in the string
```markdown
if all(x in string for x in ["ab","cd","de"]):
```
Check if all elements from the list are NOT in the string
```markdown
if all(x not in string for x in ["ab","cd""]):
```
Iterate through list content
```markdown
for i in l:
```
Iterate through list with index
```markdown
for i in range(len(l)):
```
Iterate through list with index and content
```markdown
for idx, cont in enumerate(l):
```
Iterate through 2 lists pair-wise (stops when the shorter list is reached)
```markdown
for x,y in zip(l1,l2):
```
Create string with elements joined together with ", " eg. ["a","b","c"] => a, b, c
```markdown
', '.join(l)
```
Define list
```markdown
a = [1,2,3,4,5]
```
List is mapped with the lambda function => [2,4,6,8,10]
```markdown
list(map(lambda x: x*2, [1,2,3,4,5]))
```
Also possible with list comprehension => [2,4,6,8,10]
```markdown
c=[x*2 for x in [1,2,3,4,5]]
```
List is filtered with lambda for even numbers => [2,4]
```markdown
list(filter(lambda x: x%2==0, [1,2,3,4,5]))
```
Also possible with list comprehension => [2,4]
```markdown
c=[x for x in [1,2,3,4,5] if x%2==0]
```
Build paris as tuple => (1,4),(2,5),(3,6)
```markdown
zip([1,2,3],[4,5,6])
```
Remove duplicates from a list
```markdown
list(set(x))
```
Change elements in list to int
```markdown
list(map(int,l))
```

<br>rotate list for n places
```markdown
def rotate(l, n):
    return l[-n:] + l[:-n]
```

<br>Iterate over 2 lists at the same time using zip
```markdown
animal = ['Cat', 'Dog', 'Fish', 'Goat']
age = [1, 2, 2, 6]
z = zip(animal, age)
for animal, age in z: ...
```



---
## TUPEL
[jump to top...](#python)<br><br>
ordered, immutable, allows duplicate elements
working can be more efficient than with lists - especially with big data - regarding space and runtime<br>
Create a tuple
```markdown
t = (4,5,6)
```
Create a tuple from a list
```markdown
t = tuple([3,4,4]
```
Selection / slicing of elements - same as with lists
```markdown
t[]
```
Change tuple to list
```markdown
l = list(t)
```
Change list to tuples
```markdown
t = tuple(l)
```
Assigning vars to tuple-elements (a=0, b=1, c=2)
```markdown
a,b,c = (0,1,2)
```
Assigning to tuple-values (f=0, m=[1,2,3], l=4)
```markdown
f,*m,l = (0,1,2,3,4)
```



---
## DICTIONARY
[jump to top...](#python)<br><br>
key-value pairs, unordered (till version 3.7), mutable<br>
Define empty dict
```markdown
d = {}
```
Define dict with content
```markdown
d = {"one": 1, "two": 2, "three": 3}
```
2nd way to defince a dict with content
```markdown
d = dict(one=1,two=2,three=3)
```
Define dict with content (with dupels)
```markdown
d = dict([("one",1),("two",2),("three",3)])
```
Define dict with content (with pairs in nested list)
```markdown
d = dict([["one",1],["two",2],["three",3]])
```
Define dict with 2 different lists (1x keys and 1x values)
```markdown
d = dict(zip(["one","two","three"], [1,2,3]))
```
Access value with key element (error when the key is not in the dict)
```markdown
d["two"]
```
BETTER: Acesss value with get for key element (no error when the key is not in the dict - returns second parameter instead)
```markdown
d.get("two","N/A")
```
Access value - same as get - but also initialize the key when it is not in the dict - with the second parameter)
```markdown
d.setdefault("two","N/A")
```
Find key for specific value (v) in dict
```markdown
key = list(d.keys())[list(d.values()).index(v)]
```
Read keys from dict to list
```markdown
list(d.keys())
```
Read values from dict to list
```markdown
list(d.values())
```
Count of entries in dict
```markdown
len(d)
```
Check if key is in dict (true / false)
```markdown
"three" in d
```
New entry for dict (key = "four", value = 4)
```markdown
d["four"] = 4
```
Delete specific key in dict
```markdown
del d["one"]
```
Rename dict-keyname
```markdown
mydict[new_key] = mydict.pop(old_key)
```
Combine 2 dicts (if key is in both dicts - the second value will be taken)
```markdown
combined_dict = {**d1, **d2}
```
Check if key is in dict
```markdown
if "xyz" in d:
```
Copying a dict (all changes will be made in BOTH dicts)
```markdown
d2 = d
```
Copying a dict (dicts will be handled seperate)
```markdown
d2 = d.copy()
```
Copying a dict 2nd method (dicts will be handled seperate)
```markdown
d2 = dict(d)
```
Dict d get updated with d2 (all existing keys are overwritten - and new added)
```markdown
d.update(d2)
```
Iterate through dict keys
```markdown
for key in d.keys():
```
Iterate through sorted dict keys ascending
```markdown
for key in sorted(d.keys()):
```
Iterate through sorted dict keys descending
```markdown
for key in sorted(d.keys(),reverse=True):
```
Iterate through dict values
```markdown
for val in d.values():
```
Iterate through keys and values of the dict
```markdown
for key, val in d.items():
```
Sort dict descending according to values (=item[1])
```markdown
d = {k: v for k, v in sorted(d.items(), key=lambda item: item[1], reverse=True)}
```
Sort dict ascending according to keys (=item[0])
```markdown
d = {k: v for k, v in sorted(d.items(), key=lambda item: item[0])}
```
Dict sorted: 1st value-desc (x[0]) - 2nd key-ascnd (-x[0])
```markdown
d = {k: v for k, v in sorted(d.items(), key=lambda x: (-x[1],x[0]))}
```



---
## SETS
[jump to top...](#python)<br><br>
unordered, mutable, no duplicates<br>
Define empty set - {} would define a dict and not a set
```markdown
s=set()
```
Define set with content
```markdown
s = {1,1,2,2,3,4}
```
Define empty set - returns: {"o","l","H","e"}
```markdown
s = set("Hello")
```
Define second set
```markdown
s2 = {1,7,8}
```
Add element in set1
```markdown
s.add(5)
```
Add several elements to set1
```markdown
s.update([10,11,12])
```
Intersection of 2 sets (same as: s.intersection(s2))
```markdown
s & s2
```
Untion of 2 sets (same as: s.union(s2))
```markdown
s | s2
```
Difference of 2 sets (same as: s.difference(s2))
```markdown
s - s2
```
True if s is subset from s2 (same as: s.issubset(s2))
```markdown
s <= s2
```
Check if element is in set
```markdown
3 in s
```
Clear the set
```markdown
s.clear()
```
Delete lowest elmeent in set
```markdown
s.pop()
```
Delete element 5 from set - but key error possible
```markdown
s.remove(5)
```
Delete element 5 from set - NO key error possible
```markdown
s.discard(5)
```
Iterate through set content
```markdown
for i in s:
```
Copying a set (all changes will be made in BOTH sets)
```markdown
s2 = s1
```
Copying a set (set will be handled seperate)
```markdown
s2 = s.copy()
```
Copying a set 2nd method (set will be handled seperate)
```markdown
s2 = set(s)
```
Define a frozenset - no changes are possible in the set - union, intersection aso. will work
```markdown
s = frozenset(1,2,3)
```



---
## CONTROL STRUCTURES and ITERATIONS
[jump to top...](#python)<br><br>
If / elif / else
```markdown
if x > 10: pass
elif x > 10: pass
else: pass
```

<br>Use 2 conditions in one line (instead of (a>10 and a<20)
```markdown
if (10 < a < 20)...
```
Connecting different control structures with logical and &
```markdown
if a<10 & b>10 & c==4...
```

<br>5 iterations from 0 to 4
```markdown
for i in range(5):
```
5 iterations from 0 to 4 (start, end, step)
```markdown
for i in range(0, 5, 1)
```
Iterations descending from 4 to 0
```markdown
for i in range(4, -1, -1)
```

<br>While loop with break condition
```markdown
while x < 4:
```
Endless while loop - has to be exited with break
```markdown
while True:
```
Break loop completely
```markdown
break
```
Break actual loop run - continue with next loop run
```markdown
continue
```



---
## FUNCTIONS, DECORATORS
[jump to top...](#python)<br><br>
description of the function in form of a docstring
```markdown
def printNumAbbr(value):
'''
eg. Make abbreviaton for numeric value in thousands (K), millions (M), billions (B) or trillions (T)
:param value: numeric value which should be abbreviated
:return: string value with maximum possible abbreviation
'''
```

<br>Define function - with default value 0 if no input is given
```markdown
def add(x=0,y=0):
    erg = x+y                   	# Calculation in function
    return erg                  	# Return value from the function
```

<br>Optional argument in the funtction (first element is must - second optional)
```markdown
def pet (animal,n1=None,n2="x")
pet("Cat")                      	# Calling function with n1=None and n2 = "x"
pet("Cat","name")					# Calling function with n1=name and n2 = "X"
pet("Cat",n2="xyz") 				# Calling function with n1=None and n2 = "xyz" (third parameter has to be named when calling)
```

<br>Function with infinite arguments
```markdown
def varargs(*args): print(args)
varargs(1,2,3)                  	# Outputs (1,2,3)

def keyword_args(**kwargs):
    print(kwargs)
keyword_args("a"=3, "b"=4)      	# Outputs {"a":3, "b":4}
```

<br>decorator template
```markdown
def my_decorator(func):				# Define decorator
  @functools.wraps(func)
  def wrapper(*args,**kwargs):		# Decorator with * arguments
	  #Do...					 	# Do something before the functions
	  result=func(*args,**kwargs)	# Run the function
	  #Do...					 	# Do something after the functions
	  return result					# Return the results from the function
  return wrapper
```

<br>decorator
```markdown
extend behaviour of a function with a decorators
def start_end_decorator(func):		# Define the decorator with function "func" as input-parameter
	def wrapper():					# Inside the decorator a wrapper function has to be defined
		print("Start")				# Decorated code which is executed before the core code from the function
		func()						# Calling the function itself
		print("End")				# Decorated code which is executed after the core code from the function
	return wrapper					# Results from the decorator have to be given back
@start_end_decorator				# Defines this decorator for the following function "print_name"
def print_name():					# Normal content of the function
	print("xyz")					# Core functionality of the function
print_name()						# Now when the function is executed - outputs not only "xyz" - also "Start" before and "End" after
```

<br>decorator with function arguments
```markdown
def start_end_decorator(func):		# Define the decorator with function "func" as input-parameter
	def wrapper(*args,**kwargs):	# Inside the decorator a wrapper function has to be defined
		print("Start")				# Decorated code which is executed before the core code from the function
		result = (*args,**kwargs)	# Calling the function itself
		print("End ")				# Decorated code which is executed after the core code from the function
		return result
	return wrapper					# Results from the decorator have to be given back
@start_end_decorator				# Defines this decorator for the following function "add5"
def add5(x):						# Normal content of the function with one argument
	return x + 5					# Core functionality of the function
result = add5(10)					# Outputs "Start" => "End" => 15
print(result)
```



---
## GENERATORS, YIELD
[jump to top...](#python)<br><br>
very memory efficient
<br>Defines the generator with 3 yield statements
```markdown
def mygenerator():
	yield 3
	yield 2
	yield 1
```

<br>Creates the generator and stores in g (=generator type)
```markdown
g = mygenerator()
```
Outputs 3,2,1
```markdown
for i in g: print(i)
```
Outputs 3
```markdown
print(next(g))
```
Outputs 2
```markdown
print(next(g))
```
Sum-Function can also use a generator => result is 6
```markdown
sum(g)
```
Sorted-Function can use generator => returns list with sorted elements [1,2,3]
```markdown
sorted(g)
```



---
## EXCEPTIONS
[jump to top...](#python)<br><br>
try / except
```markdown
try:
	a = 5 / 0
except Exception as e:
	print("Exception: ",e)						# Prints exception "division by zero"
```

<br>assert / raise
```markdown
x = -5
assert (x>=0), "x is not positive"				# Checks / Assert some condition => prints "x is not positive"
if x<0: raise Exception("x should positive")	# Raises an exception => prints "Exception: x should be positive"
```



---
## LAMBDA, MAP, FILTER
[jump to top...](#python)<br><br>
<br>functions with one argument - add10(5) => 15
```markdown
add10 = lambda x: x+10
```
functions with two arguments for multiplying - mult(2,7) => 14
```markdown
mult = lambda x,y: x*y
```
p = [(1,2),(15,1),(5,-1),(10,4)]<br>
output is sorted with first element then second element => [(1,2),(5,-1),(10,4),(15,1)]
```markdown
sorted(p)
```
output is sorted by the second element => [(5,-1),(15,1),(1,2),(10,4)]
```markdown
sorted(p,key=lambda x:x[1])
```
output is sorted by the sum of both => [(1,2),(5,-1),(10,4),(15,1)]
```markdown
sorted(p,key=lambda x:x[0]+x[1])
```
a = [1,2,3,4,5]<br>
list is mapped with the lambda function => [2,4,6,8,10]
```markdown
list(map(lambda x: x*2,a))
```
also possible with list comprehension => [2,4,6,8,10]
```markdown
c=[x*2 for x in a]
```
list is filtered with lambda for even numbers => [2,4]
```markdown
list(filter(lambda x: x%2==0,a))
```
also possible with list comprehension => [2,4]
```markdown
c=[x for x in a if x%2==0]
```



---
## CLASSES, DATACLASSES
[jump to top...](#python)<br><br>
Define a class
```markdown
class Human(object):
  species = "Homo Sapiens"    # Fix variable / class variable for all instances of the class
  def __init__(self,name):    # Constructor - automatically applied when an instance is created
      self.name = name		  # Name is assigned to the instance of the classe (self.)
	  self.tresor = []		  # Tresor is assigned as list to the instance of the class (self.)
  def say(self, msg):         # Methode of the class
      return "{name}: {message}".format(name=self.name, message=msg)
	  elf.tresor.append(msg)  # Tesor of the instance gets a new value in the list
  @classmethod                # Class methode - is used by all instances
  def get_species(cls):
      return cls.species
  @staticmethod               # Static methode - is called without class or method
  def grunt():
      return "*grunt*"
```

<br>Create instance of the class
```markdown
i = Human(name="Ian")
```
Call the methode of the class (output: "Ian: Hi")
```markdown
print(i.say("Hi"))
```
Create additonal instance of the class
```markdown
j = Human(name="Joel")
```
Call the methode of the class (output: "Joel: Hallo")
```markdown
print(i.say("Hallo"))
```
Output "Homo Sapiens"
```markdown
i.get_species()
```
Same output  "Homo Sapiens"
```markdown
j.get_species()
```
Change of the class variable - applies for all instances
```markdown
Human.species = "Was Neues"
```
Aufruf der statischen Methode => Ausgabe: "*grunt*"
```markdown
Human.grunt()
```

<br>Dataclasses
```markdown
from dataclasses import dataclass		# import dataclass necessary
@dataclass								# define a dataclass
class Coordinate:						# class is defined an need NO __init__, __repr__, __eq__
    x: int								# __init__ no necessary - values get assigned automatically
    y: int = 10							# __repr__ print for the string-represantion is automatic => Coordinate(x=4, y=5)
a = Coordinate(4, 5)
@dataclass (frozen=True)				# defines a unmutable instance
asdict(dc)								# converts the dataclass to a dict
astuple(dc)								# converts the dataclass to a tuple
```



---
## TXT FILES
[jump to top...](#python)<br><br>
<br>Read textfile - and print it
```markdown
with open ("fn.txt","r") as f: print(f.read()
```
Open File for Read and Write
```markdown
with open ("fn.txt","r+") as f: print(f.read()
```

<br>Read textfile - stored in list per line
```markdown
with open("fn.txt","r") as f:
    lines = [x.strip() for x in f.readlines()]          # Whitespaces are eliminated with strip()
```

<br>Writing in textfile
```markdown
with open("fn.txt","w") as obj: obj.write("Ein neuer Text")
```
Append text in the next line
```markdown
with open("fn.txt","a") as obj: obj.write("\nNoch ein Text")
```
Check if file allready exists
```markdown
if os.path.exists(fn) == False:
```
Create and initialize file when not exisiting
```markdown
with open (fn,"a") as f: f.write("init")
```
Read content to string
```markdown
f.read()
```
Set the current postion in the file to beginning
```markdown
f.seek(0)
```
Write s to the f-file opened
```markdown
f.write(s)
```


<br>Try/Except - checks if file can be saved
```markdown
while True:
try:                         							# otherwise outputs a error message
    writer.save ()
    break
except Exception as e:
    print ("Error: ", e)
	traceback.print_exc()                               # Outputs the detailed error message
    input ("File Open not possible - pls close and press <Enter>")
```



---
## JSON FORMAT
[jump to top...](#python)<br><br>
<br>Import json-module
```markdown
import json
```
Assign JSON-filename
```markdown
fn = "numbers.json"
```
Reading informations in json-format
```markdown
with open(fn) as data: info = json.loads(data)
```
Convert / Encode a dict to a json-file (with indent for better reading)
```markdown
json_format = json.dumps(d,indent=2)
```
Convert / Encode a dict to a json-file (with sorting the keys)
```markdown
json_format = json.dumps(d,sort_keys=True)
```
Writing information in json-format (e.g. after updating the values/format)
```markdown
with open(fn,"w") as data: json.dump(person, data)
```
Convert / Decode a json-file to a dict
```markdown
person = json.loads(json_format)
```
Reading information in json-format
```markdown
with open(fn.json,"r") as data: d=json.load(file)
```

<br>Example for json-file
```markdown
{
	"firstName" : "Chuck",
	"lastName" : "Doe",
	"hobbies": ["running","swimming","singing"],
	"age": 28,
	"hasChildren": true
	"children" = [
		{
			"firstName" : "Alex"
			"age" : 5
		},
		{
			"firstName" : "Bob"
			"age" : 7
		}
	]
}
```
<br>Read name value => "Chuck"
```markdown
info["firstName"]
```
Iterate trough the json-file (eg. many children)
```markdown
for item in children:
```



---
## XML FORMAT
[jump to top...](#python)<br><br>
<br>Import xml-module
```markdown
import xml.etree.ElementTree as ET
```
<br>Example for xml-file
```markdown
<persons>
	<person>
		<name>Chuck</name>
		<phone type="int1"> +1 734 555"</phone>
		<email hide="yes"/>
	</person>
	...
</persons>
```
<br>Read xml-file into tree
```markdown
tree = ET.fromstring(data)
```
Read name text => "Chuck"
```markdown
tree.find("name").text
```
Read hide value from email => yes
```markdown
tree.find("email".get("hide"))
```

<br>Iterate trough xml-file (eg. many persons)
```markdown
lst = persons.findall("persons/person")
for item in lst:
```



---
## URLLIB
[jump to top...](#python)<br><br>
https://pymotw.com/2/urlparse/<br>
Import Module for URL parsing
```markdown
import from urllib.parse import urlparse
```
https://docs.python.org/3/library/urllib.request.html#module-urllib.request<br>
Import Module for request
```markdown
import urllib.request
```
Parse HTML-link1
```markdown
u = urlparse("http://google.com/search")
```
Returns "http"
```markdown
u.scheme
```
Returns "/search"
```markdown
u.path
```
Returns "google.com"
```markdown
u.netloc
```



---
## MODULE - CSV
[jump to top...](#python)<br><br>
<br>Import CSV-Module
```markdown
import csv
```
<br>Open csv-file in writemode
```markdown
with open("test.csv","w",newline=" ") as fp:
    a = csv.writer (fp, delimiter=",")                    # Define csv-writer with ","-delimiter
    data = [["A", "B"],["100", "24"],["120", "33"]]       # Data for writing in nested list form
    a.writerows (data)                                    # Writing individual rows
```

<br>Read csv-data from a HTML-link
```markdown
import urllib.request
import codecs
url = link                                                      # direct link to a csv html file
ftpstream = urllib.request.urlopen(url)
csvfile = csv.reader(codecs.iterdecode(ftpstream, 'utf-8'))     # output is nested list
```



---
## MOUDLE - ZIPFILE - handling ZIP files
[jump to top...](#python)<br><br>
<br>Import zip module
```markdown
import zipfile
```
Read Zip-File
```markdown
zf = zipfile.ZipFile('example.zip', 'r')
```
List of string with the names of the files in the Zip-File
```markdown
zf.namelist()
```
Open file vom Zip-File (eg. CSV-File which is in the Zip-File)
```markdown
zf.open (file_name)
```



---
## MODULE - GSPREAD - API for Google Sheets
[jump to top...](#python)<br><br>
API for GoogleSheets / Tutorial explaining handling
<br>https://techwithtim.net/tutorials/google-sheets-python-api-tutorial/
```markdown
# Create a project on https://console.cloud.google.com/
# See further setup in tutorial
import gspread                                                      # import module
from oauth2client.service_account import ServiceAccountCredentials  # import module for account credentials
from pprint import pprint                                           # import module for better output formatting
scope = ["https://spreadsheets.google.com/feeds",
         'https://www.googleapis.com/auth/spreadsheets',
         "https://www.googleapis.com/auth/drive.file",
         "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name
    ("creds.json", scope)
```

<br>Credentials Mgmt for GoogleSheets
```markdown
client = gspread.authorize(creds)
```
Open the spreadhseet
```markdown
sheet = client.open("testpython").sheet1
```
Get a list of all records
```markdown
data = sheet.get_all_records()
```
Count of all used rows in the sheet
```markdown
len(data)
```
Show all data with pprint - pretty print
```markdown
pprint(data)
```
Get row 3 (starts counting from 1 - not 0)
```markdown
row = sheet.row_values(3)
```
Get col E (starts counting from 1 - not 0)
```markdown
col = sheet.col_values(5)
```
Get values from col B rows 4 and 5
```markdown
col = sheet.col_values(2)[3:5]
```
Get the value from row 1 and col B
```markdown
cell = sheet.cell(1,2).value
```
Update cell from row 2 and col B
```markdown
sheet.update_cell(2,2, "CHANGED")
```
Insert new row at row number 2
```markdown
sheet.insert_row(["new1","new2","new3"],2)
```
Append new row at the end
```markdown
sheet.append_row(["new1","new2","new3"])
```
Sorting the sheet (Range + col1 asc + col2 desc)
```markdown
sheet.sort((1, 'asc'), (2, 'des'), range='A2:G20')
```
Define cell area / cell row
```markdown
cell_list = worksheet.range('A1:G1')
```
Define new values for area / row
```markdown
new_values = [1,2,3,4,5]
```
Write new values to cell area / cell row
```markdown
for i, val in enumerate(new_values): cell_list[i].value = val
```
Upate cell area / cell row
```markdown
worksheet.update_cells(cell_list)
```

<br>Gspread Formatting
<br>https://pypi.org/project/gspread-formatting/
```markdown
# Set format for area:
	from gspread_formatting import *
	fmt = cellFormat(
		backgroundColor=color(1, 0.9, 0.9),
		textFormat=textFormat(bold=True, foregroundColor=color(1, 0, 1)),
		horizontalAlignment='CENTER'
		)
	format_cell_range(worksheet, 'A1:J1', fmt)
# Conditional formatting
	from gspread_formatting import *
	worksheet = some_spreadsheet.worksheet('My Worksheet')
	rule = ConditionalFormatRule(
		ranges=[GridRange.from_a1_range('A1:A2000', worksheet)],
		booleanRule=BooleanRule(
			condition=BooleanCondition('NUMBER_GREATER', ['100']),
			format=CellFormat(textFormat=textFormat(bold=True), backgroundColor=Color(1,0,0))
		)
	)
	rules = get_conditional_format_rules(worksheet)
	rules.append(rule)
	rules.save()

	# or, to replace any existing rules with just your single rule:
	rules.clear()
	rules.append(rule)
	rules.save()
```



---
## MODULE - OPENPYXL - working with excel worksheets
[jump to top...](#python)<br><br>
<br>https://openpyxl.readthedocs.io/en/stable/api/openpyxl.worksheet.worksheet.html#openpyxl.worksheet.worksheet.Worksheet.PAPERSIZE_A3
```markdown
Documentation:
```
Import module for loading a workbook
```markdown
from openpyxl import load_workbook
```
Import module for creating a workbook
```markdown
from openpyxl import Workbook
```
Load xlsx
```markdown
wb = load_workbook(("Test.xlsx"))
```
Create new workbook
```markdown
wb = openpyxl.Workbook()
```
Create new worksheet (at the end)
```markdown
wb.create_sheet("ws")
```
Create new worksheet (at the beginning)
```markdown
wb.create_sheet("ws",0)
```
Create new worksheet (at the second last position)
```markdown
wb.create_sheet("ws",-2)
```
All worksheets from the
```markdown
wb.sheetnames
```
Select specific worksheet in workbook
```markdown
ws = wb["sheet1"]
```
Select active worksheet from workbook
```markdown
ws = wb.active
```
Change worksheet name
```markdown
ws.title = "xyz"
```
Value from specific cell
```markdown
ws["A1"].value
```
Value from specific cell (other method)
```markdown
ws.cell(row=1, column=1).value
```
Assign value to specific cell
```markdown
ws["A1"] = 97
```
Assign formula to specific cell (only english names for function and arguments must be sepearted by "," and not ";")
```markdown
ws["A1"] = "=SUBTOTAL(1,I6:I10000)"
```
Save workbook to xlsx
```markdown
wb.save("Test2.xlsx")
```

<br>Loop trough specific area and print the cell values
```markdown
for row in ws["A1":"C3"]:
    for cell in row: print(cell.value)
```

<br>Loop trough specific column and print the cell values
```markdown
for cell in ws["C"]: print(cell.value)
```
Insert column before col 3
```markdown
ws.insert_cols(3)
```
Insert 2 columns before col 3
```markdown
ws.insert_cols(3,2)
```
Insert row before row 7
```markdown
ws.insert_rows(7)
```
Insert 5 rows before row 10
```markdown
ws.insert_rows(10,5)
```
Delete column C
```markdown
ws.delete_cols(3)
```
Delete column F to H
```markdown
ws.delete_cols(6,3)
```
Delete row 5
```markdown
ws.delete_rows(5)
```
Delete row 5 to 7
```markdown
ws.delete_rows(5,3)
```
Move the cells from D4:F10 up one row and right two columns
```markdown
ws.move_range("D4:F10", rows=-1, cols=2)
```
Append the values at the bottom of the sheet
```markdown
ws.append([1,"A",2,"C"])
```
Returns dimension of the worksheet eg. "A1:M24"
```markdown
ws.dimensions
```
Returns max column / row count of the worksheet
```markdown
ws.max_column / ws.max_row
```
Returns min column / row count of the worksheet (which contains data)
```markdown
ws.min_column / ws.min_row
```
Rows 1:3 to be printed at the top of every page
```markdown
ws.print_title_rows(1:3)
```
Delete worksheet in workbook
```markdown
del wb["sheet4"]
```
Define filters in columns A5 to Q5
```markdown
ws.auto_filter.ref = "A5:Q5"
```
Set filter to values "X","Y","Z" in column 2
```markdown
ws.auto_filter.add_filter_column(2,["X","Y","Z"])
```
Sort elements in filter for columsn B2 to B15
```markdown
ws.auto_filter.add_sort_condition("B2:B15")
```
Close workbook
```markdown
wb.close()
```
<br>Iterate trough worksheet row by row
```markdown
for row in ws.iter_rows():
    for cell in row: print(cell.value)
```

<br>Iterate trough worksheet row by row (from A1 to C6 - 6 lines)
```markdown
for row in ws.iter_rows
	(min_row=1,min_col=1,max_row=6,max_col=3):
```

<br>Iterate trough worksheet col by col
```markdown
for col in sheet.iter_cols():
    for cell in col: print(cell.value)
```

<br>Iterate trough worksheet col by col (from A1 to C6 - 3 lines)
```markdown
for col in ws.iter_cols
	(min_row=1,min_col=1,max_row=6,max_col=3):
```

<br>Read whole worksheet to a nested list
```markdown
data_list = []
for row in ws.iter_rows ():
    zeile = []
    for cell in row:
        if cell.value is None:
            zeile.append ('')
        else:
            zeile.append (cell.value)
    data_list.append (zeile)
```

<br>Saving a nested list in XLSX
```markdown
import pandas as pd
from openpyxl import load_workbook
cont = [[row1_cell1, row1_cell2], [row2.cell1,row3_cell3]]      # Nested list for saving
book = load_workbook ("fn.xlsx")                                # load existing XLSX - skip when overwriting
writer = pd.ExcelWriter ("fn.xlsx", engine='openpyxl',          # Define writer from pandas
                         options={'strings_to_numbers': True})
pd.DataFrame (cont).to_excel (writer, sheet_name="WS1",			# Prepare Data for XLSX and worksheet1
                              header=False, index=False)
pd.DataFrame (cont).to_excel (writer, sheet_name="WS2",			# Prepare Data for XLSX and worksheet2
                              header=False, index=False)
writer.save()                                                   # Save XLSX with the new worksheets
writer.close()													# Close writer
```

<br>Checking if xlsx is open while trying to save
```markdown
while True:
    try:
        writer.save ()
        writer.close ()
        break
    except Exception as e:
        print ("Error: ", e)
		traceback.print_exc()
        input ("Datei kann nicht geöffnet werden - bitte schließen und <Enter> drücken!")
```

<br>Read column to a list
```markdown
mylist = []
for col in ws['A']:
     mylist.append(col.value)
```

<br>Automatic adjustment of the columns accoring to best fit
```markdown
column_widths = []
ws = writer.sheets[stock]
for row in content:                                    # Determination of the longest value per column
    for i, cell in enumerate (row):
        if len (column_widths) > i:
            if len (str (cell)) > column_widths[i]:
                column_widths[i] = len (str (cell))
        else:
            column_widths += [len (str (cell))]
    for i, column_width in enumerate (column_widths):  # Col 0 and 1 with fixed length - rest according to longest value in col
        if i == 0:
            ws.column_dimensions[get_column_letter (i + 1)].width = 35
        elif i == 1:
            ws.column_dimensions[get_column_letter (i + 1)].width = 32
        else:
            ws.column_dimensions[get_column_letter (i + 1)].width = column_width + 2
```

<br>Formating the xlsx
when a cell is formated 2 times - it gets overwritten)<br>
import openpyxl.styles
```markdown
from openpyxl.styles import Font, PatternFill, Border, Side, Alignment
```
import formatting, styles
```markdown
from openpyxl import formatting, styles
```
bold font
```markdown
bold = Font (bold=True)
```
yellow background (use color picker)
```markdown
bg_yellow = PatternFill (fill_type="solid", start_color='fbfce1', end_color='fbfce1')
```
grey background (use color picker)
```markdown
bg_grey = PatternFill (fill_type="solid", start_color='babab6', end_color='babab6')
```
blue background (use color picker)
```markdown
bg_green = PatternFill (fill_type="solid", start_color='8af542', end_color='8af542')
```

<br>define border on very side
```markdown
frame_all = Border (left=Side (style='thin'), right=Side (style='thin'),
                    top=Side (style='thin'), bottom=Side (style='thin'))
```

<br>border only on top and bottom
```markdown
frame_upanddown = Border (top=Side (style='thin'), bottom=Side (style='thin'))
```
font size 14
```markdown
size14 = Font (bold=True, size="14")
```
define left alignment
```markdown
left_allign = Alignment (horizontal="left")
```
define right alignment
```markdown
right_allign = Alignment (horizontal="right")
```

<br>define right alignment for area
```markdown
for row in ws["D1":"G34"]:
    for cell in row: cell.alignment = right_allign
```

<br>define full border for several areas
```markdown
areas = ["A7:G19","A27:G31"]
```

<br>format area
```markdown
for area in areas:
    for row in ws[area]:
        for cell in row:
			cell.border = frame_all
			cell.number_format = "0"															=> define number format without decimals
			cell.number_format = "0.000E+00"													=> define number format with 3 decimals
```

<br>set background and size for several specific cells
```markdown
for i in ["A6","D6","E6","A26","D26","E26"]:
    ws[i].fill = bg_green
    ws[i].font = size12
```

<br>freeze worksheet at cell B2 for right and down scrolling
```markdown
freeze = ws["B2"]
ws.freeze_panes = freeze
```

<br>fit xlsx to one page for printing - 1st part
```markdown
ws.sheet_properties.pageSetUpPr.fitToPage = True
```
fit xlsx to one page for printing - 2nd part
```markdown
ws.page_setup.fitToHeight = False
```
set page to landscape horizontal
```markdown
ws.set_printer_settings(paper_size=1, orientation = 'landscape')
```
set page to landscape horizontal
```markdown
ws.set_printer_settings(paper_size=1, orientation = 'portrait')
```
Define red color background
```markdown
red_color = 'ffc7ce'
```
Define red color font
```markdown
red_color_font = '9c0103'
```
Define red_font with size / bold / red color
```markdown
red_font = styles.Font (size=14, bold=True, color=red_color_font)
```
Define red_fill with color red / fill type solid
```markdown
red_fill = styles.PatternFill (start_color=red_color, end_color=red_color, fill_type='solid')
```

<br>Define conditional formating for area, <0, => fill with red background
```markdown
ws.conditional_formatting.add ('A1:Z100',
	formatting.rule.CellIsRule (operator='lessThan',formula=['0'],fill=red_fill))
```

<br>Define conditional formating for area, <0, => use red font
```markdown
ws.conditional_formatting.add ('A1:G25',
	formatting.rule.CellIsRule (operator='lessThan',formula=['0'],fill=red_fill,font=red_font))
```

<br>Conditional formating for more than one area
```markdown
for area in ["B1:B100","C2:G100"]:
	ws.conditional_formatting.add (area, ...)
```

<br>Conditional formating according to a formula
```markdown
ws.conditional_formatting.add('E1:E10',
	FormulaRule(formula=['ISBLANK(E1)'], stopIfTrue=True, fill=redFill))
```

<br>Conditional formating according to a formula
```markdown
ws.conditional_formatting.add('D2:D10',
	FormulaRule(formula=['E1=0'], font=myFont, border=myBorder, fill=redFill))
```



---
## MODULE - XLWINGS - working on the fly with open excel worksheets
[jump to top...](#python)<br><br>
Update XLSX in reealtime<br>
Import module
```markdown
import xlwings as xw
```
Read XLSX
```markdown
wb = xw.Book ("name.xlsx")
```
Read specific worksheet
```markdown
ws = wb.sheets["name_sheet"]
```
Updates specific cell
```markdown
ws["A1"].value = "xyz"
```
Iterate trough cells an set them to "" / None
```markdown
for i in ws.range("A3:A7"): i.value = ""
```
Read specific cells to list
```markdown
l = ws.range("A2:A100").value
```
Read cells
```markdown
cells = ws.range("A2:A100")
```
Update the value of a cell
```markdown
cells[1].value = "new value"
```
Writeback the updates to cells
```markdown
ws.range("A2:A100").value = l
```
Sort worksheet in the first col (function see below)
```markdown
xl_col_sort(ws,1)
```
Reads the color of a cell and returns a rgb-tuple eg. (146, 208, 80)
```markdown
ws["C8"].color
```
Remove background from a cell
```markdown
ws["C8"].color = None
```
Assigns background color for a range of cells
```markdown
ws.Range("A1:C3").color = (255,255,255)
```


<br>Sorting workssheet in given col
```markdown
def xl_col_sort(sheet,col_num):
    sheet.range((2,col_num)).api.SortKey1=sheet.range((2,col_num)).api, Order1=1)
    return
```



---
## MODULE - WIN32COM - creating worksheets as pdf from xlsx
[jump to top...](#python)<br><br>
Create Worksheets as PDF from XLSX<br>
Import Win32 Module
```markdown
import win32com.client
```
Import OS Module
```markdown
import os
```
Define Input-XLSX
```markdown
inp = os.getcwd() + "\\" +"excel.xlsx"
```
Define Output-PDF
```markdown
out = os.getcwd() + "\\" +"ws.pdf"
```
Initialize Excel Application
```markdown
o = win32com.client.Dispatch("Excel.Application")
```
Do everything hidden
```markdown
o.Visible = False
```
Open XLSX
```markdown
wb = o.Workbooks.Open(inp)
```
Create PDF from the active worksheet in the xlsx
```markdown
wb.ActiveSheet.ExportAsFixedFormat (0, out)
```
Close XLSX
```markdown
wb.Close(True)
```
Number of Worksheets
```markdown
wb.Sheets.Count
```
Select 3 different worksheets by number (for exporting afterwards)
```markdown
wb.WorkSheets ([3,4,8]).Select()
```
Assign worksheet 4
```markdown
ws = wb.Worksheets[4]
```
No Zooming
```markdown
ws.PageSetup.Zoom = False
```
Fit to 1 height
```markdown
ws.PageSetup.FitToPagesTall = 1
```
Fit to 1 width
```markdown
ws.PageSetup.FitToPagesWide = 1
```
Select specific print area
```markdown
ws.PageSetup.PrintArea = "A1:G50"
```



---
## MODULE - PyPDF2 - working with pdfs
[jump to top...](#python)<br><br>
Working with PDFs
<br>Read PDF informations / metadata
```markdown
from PyPDF2 import PdfFileReader        # Import Module for PDF Reading
with open (fn, 'rb') as f:
    pdf = PdfFileReader (f)				# Read PDF informations
    info = pdf.getDocumentInfo ()		# Read PDF infos^
    number_of_pages = pdf.getNumPages ()    # Read number of pages
	print(info)							# Outputs all informations
	print(info.title)					# Outputs title of the pdf
	print(info.author)					# Outputs author of the pdf
```

<br>Read Text from Pdf
```markdown
page = pdf.getPage (7)		# Select page 8
text = page.extractText ()	# Extract text
print (text)				# print (text
```

<br>Split PDFs
```markdown
from PyPDF2 import PdfFileWriter		    # Import Module for PDF Writing
pdf_writer = PdfFileWriter()				# Create new instance of PDF writer
pdf_writer.addPage(page)                    # Add Page to writer
with open(output_filename, 'wb') as out:	# Write splitted PDF
	pdf_writer.write(out)
```

<br>Merge PDFs
```markdown
from PyPDF2 import PdfFileMerger		    # Import Module for PDF Merging
pdf_merger = PdfFileMerger()				# Create new instance of PDF merger
pdf_merger.append(path)                     # Append Page for merging
with open(output_path, 'wb') as fileobj:	# Write merged PDF
	pdf_merger.write(fileobj)
```

<br>Rotate clockwise
```markdown
page.rotateClockwise(90)
```
Rotate counter clockwise
```markdown
page.rotateCounterClockwise(90)
```
Overlaying / Watermarking two pages
```markdown
page.mergePage(watermark_page)
```



---
## MYSQL - MARIADB - HEIDISQL
[jump to top...](#python)<br><br>
<br>Data where the MariaDB-database is stored
```markdown
C:\Program Files\MariaDB 10.3\data
```
Data where the MySQL-database is stored
```markdown
C:\ProgramData\MySQL\MYSQL Server 8.0\data
```
Shows the database-version in the column header
```markdown
HeidiSQL - Datei / Verbindungsmanager
```

<br>Transfer whole table from local db to hosted db
```markdown
right click on table / tables to transfer and select "export database as sql"
for "output" select "Server: A2Hosting" (connection to the hosted server)
for "database" select "rapidtec_stockdb" (name from the db on the hosted server)
for "data" select "replace existing data"
press "export" (wait till the rows-column shows 100%)
```



---
## MYSQL - MARIADB - SQL
[jump to top...](#python)<br><br>
<br>Import module for mysql access
```markdown
import mysql.connector
```
Define connection
```markdown
mydb = mysql.connector.connect (host="localhost",user="root",passwd="pwd")
```
Set Cursor on mySQL
```markdown
mycursor = mydb.cursor()
```
Creates database "db"
```markdown
mycursor.execute("CREATE DATABASE db")
```

<br># Show databases and informations
```markdown
mycursor.execute("SHOW DATABASES")
    for db in mycursor: print(db)
```

<br>Create new table with 2 cols
```markdown
mycursor.execute("CREATE TABLE students (name VARCHAR(255),age INTEGER(10))")
```
Show tables and informations
```markdown
mycursor.execute("SHOW TABLES") for tb in mycursor: print(tb)
```
Insert row in table with the 2 values using sql injection
```markdown
sqlFormula = "INSERT INTO students (name, age) VALUES (%s, %s)"
```
Define a row with values to insert
```markdown
student1 = ("Rachel", 22)
```
Execute the sql statement to add one row
```markdown
mycursor.execute(sqlFormula,student1)
```
Commit the change (otherwise no update will be saved to db)
```markdown
mydb.commit()
```
Define more rows with values
```markdown
students = [("Tom", 22),("Mark", 29),("Clara", 52)]
```
Execute the sql statement to add more row (from list / tuple)
```markdown
mycursor.executemany(sqlFormula,students)
```
Select col "age" from table "students"
```markdown
mycursor.execute("SELECT age FROM students")
```
Read all rows according the above select statement
```markdown
myresult = mycursor.fetchall()
```
Read one / first row according the above select statement
```markdown
myresult = mycursor.fetchone()
```
Output the read row / table informations
```markdown
for row in myresult: print(row)
```
Define select (greater than)
```markdown
sql = "SELECT * FROM students WHERE age > 25"
```
Define select (with like clausel)
```markdown
sql = "SELECT * FROM students WHERE name LIKE 'M%'"
```
Execute SQL
```markdown
mycursor.execute(sql)
```
Define select (with sql injection)
```markdown
sql = "SELECT * FROM students WHERE name = %s"
```
Execute SQL with parameters
```markdown
mycursor.execute(sql, ("Mike", ))
```
Update row where name = "xyz"
```markdown
sql = "UPDATE students SET age = 82 WHERE name='xyz'"
```
Limit the output to 5 rows
```markdown
sql = "SELECT * FROM students LIMIT 5"
```
Limit the output toi 5 rows and starting with element 2
```markdown
sql = "SELECT * FROM students LIMIT 5 OFFSET 2
```
Output content - ascending order
```markdown
sql = "SELECT * FROM students ORDER BY name"
```
Output content - descending order
```markdown
sql = "SELECT * FROM students ORDER BY name DESC"
```
Delete row with name "xyz"
```markdown
sql = "DELETE FROM students WHERE name = 'xyz'"
```
Drop whole table (if exists helps if there no table anymore)
```markdown
sql = "DROP TABLE IF EXISTS students"
```

=>Read ticker for specific ticker
```markdown
sql = "SELECT ticker FROM stock_main where ticker=%s"      # Or Select * to get all values from the table
cont = [(summary["symbol"])]
c.execute(sql,cont)
data = c.fetchall()
```



---
## SQL ALCHEMY
[jump to top...](#python)<br><br>
<br>Import MODULE
```markdown
from sqlalchemy import create_engine
```
Define access to the MySQL-DB (username, pw, dbname)
```markdown
engine = create_engine("mysql+pymysql: //user:pw@localhost/dbname?host=localhost?port=3306")
```
Establish connection
```markdown
conn = engine.connect()
```
Read all existing tables from the databasen - returns list
```markdown
engine.table_names()
```
Read data from db - returns list with tupels as rows
```markdown
conn.execute("SELECT * FROM actor").fetchall()
```
Close connection at the end
```markdown
conn.close()
```
Close sql engine at the end
```markdown
engine.dispose()
```

<br>Tabelle anlegen in MySQL DB
```markdown
from sqlalchemy import Table, Column, Integer, String, Float, MetaData
meta = MetaData()
students = Table(
   'students', meta,
   Column('id', Integer, primary_key = True),
   Column('name', String(45)),
   Column('lastname', String(45)),
)
meta.create_all(engine)
```

<br>Create INSERT / UPDATE / DELETE / SELECT statements
```markdown
students.insert()                                           # Creates INSERT Statement according due the whole students structure
	=> shows: INSERT INTO students (id, name, lastname, floatvar) VALUES (:id, :name, :lastname, :floatvar)
students.insert().values(name = 'Karan')                    # Creates INSERT Statement for specific attribute
	=> shows: INSERT INTO students (name) VALUES (:name)
students.update()                                           # Creates UPDATE Statement
	=> shows: UPDATE students SET id=:id, name=:name, lastname=:lastname, floatvar=:floatvar
students.delete()                                           # Creates DELETE Statement
	=> shows: DELETE FROM students
students.select()                                           # Creates SELECT Statement
	=> shows: SELECT students.id, students.name, students.lastname, students.floatvar  FROM students
```

<br>Execute SQL command - INSERT
```markdown
conn = engine.connect()                                     # Insert one row
ins = students.insert().values name = 'Brauneder', lastname = 'Karl')
result = conn.execute(ins)
result.inserted_primary_key                                 # Shows the inserted primary key
conn.execute(students.insert(), [                           # Insert more rows
   {'name':'Krankl', 'lastname' : 'Hans'},
   {'name':'Herzog','lastname' : 'Andreas'},
])
```

<br>Execute SQL command - SELECT
```markdown
s = students.select()                                       # Creates select statement for SELECT *
result = conn.execute(s)                                    # Excenute select statement
for row in result: print(row)                               # Outputs the result rows for select
s = students.select().where(students.c.id > 10)             # Creates select statement with WHERE clausel
```

<br>Execute SQL with Textual SQL
```markdown
from sqlalchemy.sql import text
t = text("SELECT name FROM students")
result = conn.execute(t)
for row in result: print(row)
t = text("select students.name, students.lastname from students where students.name between :x and :y")
result = conn.execute(t, x = 'A', y = 'L')                  # Select statement with where-parameters
```

<br>Using Aliases
```markdown
from sqlalchemy.sql import alias, select
st = students.alias("a")
s = select([st]).where(st.c.id > 2)
conn.execute(s).fetchall()
```

<br>Execute UPDATE statement
```markdown
conn = engine.connect()
stmt=students.update().where(students.c.lastname=='Khanna').values(lastname='Kapoor')
conn.execute(stmt)
s = students.select()
conn.execute(s).fetchall()
```

<br>Execute DELETE statementconn = engine.connect()
```markdown
stmt = students.delete().where(students.c.lastname == 'Khanna')
conn.execute(stmt)
s = students.select()
conn.execute(s).fetchall()
```



---
## SQLITE3 SQL
[jump to top...](#python)<br><br>
<br>Create a database or connect to one
```markdown
conn = sqlite3.connect("address_book.db")
```
Create a cursor (for working with the db)
```markdown
c = conn.cursor()
```
<br>Create a table in the database
```markdown
```
attr1 text,
attr2 text,
```markdown
```

<br>Insert rows into database
```markdown
c.execute(INSERT INTO tbl VALUES (:attr1,:attr2,:attr3)",
		{
			"attr1": field1.get(),
			"attr2": field2.get(),
			"attr3": field3.get()
		})
```

<br>Select rows from database
```markdown
c.execute"SELECT * FROM adresses")
```
Delete row from database - get key from delete_box widget (eg. tkinter-module)
```markdown
c.execute("DELETE from addresses WHERE oid = " + delete_box.get())
```
Fetch all rows
```markdown
records = c.fetchall()
```
Fetch only one row
```markdown
c.fetchone()
```
Fetch the first 50 rows
```markdown
records = c.fetchmany(50)
```
Commit Changes
```markdown
conn.commit()
```
Close Connection
```markdown
conn.close()
```



---
## MODULES - DATES, DATETIME, CALENDAR, TIMEIT, TIME, SYS, CTYPES
[jump to top...](#python)<br><br>
Standardmodules from python no pip install necessary
<br>Overview % parsing commands
https://www.programiz.com/python-programming/datetime/strptime
https://rdrr.io/r/base/strptime.html
<br>Import module datetime and timedelta
```markdown
from datetime import datetime, timedelta
```
Import module dat
```markdown
from datetime import date
```
Conversion string to datetime in format dd.mm.jjjj
```markdown
datetime.strptime(s, "%Y-%m-%d")
```
Conversion datetime to string in format  dd.mm.jjjj
```markdown
datetime.strftime(dt, "%Y-%m-%d")
```
Convert dateformat from string in one line (1st from - 2nd to)
```markdown
dt.strftime((dt.strptime(tmp,"%m/%d/%Y")),"%Y-%m-%d")
```
Check if variable is of type datetime.date or datetime.datetime
```markdown
isinstance(x, date)
```
Check if variable is of type datetime.datetime
```markdown
isinstance(x, datetime)
```
Define date as "2020-07-24"
```markdown
date = date(2020,7,24)
```
Define date+time as "2020-03-05 19:27:23"
```markdown
dt = datetime(2020,3,5,19,27,23)
```
Actual date+time in format 2020-06-09 20:11:13
```markdown
now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
```
Actual date in format 2020-06-09
```markdown
now = datetime.now().strftime("%Y-%m-%d")
```
Actual date in datetime format
```markdown
tday = datetime.today()
```
Actual date as date format
```markdown
tday = datetime.today().date()
```
Year / month / day from the datetime
```markdown
dt.year, dt.month, dt.day
```
Returns weekday (monday=1, sunday=7)
```markdown
tday.isoweekday()
```
Calculates last friday (+2 for FR, +1 SA, 0 SU, -1 MO, -2 TU, -3 WE, -4 TH)
```markdown
last_friday = day - timedelta(days=tday.isoweekday() + 2)
```
Creates timedelta for 7 days
```markdown
tdelta = timedelta(days=7)
```
Creates timedelta for 1 minute
```markdown
tdelta = timedelta(seconds=60)
```
7 days are added to the actual day
```markdown
tday + tdelta
```
Previous 1-day-back-date for date
```markdown
newdate = date - timedelta(days=1)
```
Timedelta for two dates
```markdown
date2-date1
```
Difference in days
```markdown
daysDiff = abs(dt2-dt1).days
```
Difference in minutes
```markdown
minDiff = (date2-date1).total_seconds() / 60
```
Generate ISO-format from datetime
```markdown
datetime.fromisoformat('2020-07-10 02:00:00').timestamp()
```
Generate ISO-format from actual date
```markdown
iso_dt = datetime.fromisoformat(str(datetime.now())).timestamp()
```
Generate Datetime from ISO-format=>
```markdown
date = datetime.fromtimestamp(1594339200000 / 1e3)
```
Shows size of the list / tuple in bytes
```markdown
sys.getsizeof(l) or sys.getsizeof(t)
```

<br>Using german names / deutsche namen for month- and day-names
```markdown
import locale
locale.setlocale(category=locale.LC_ALL,locale="German")
```

<br>Check last day of month & first weekday of month
```markdown
import calendar
calendar.monthrange(year,month)                         # return tuple - 1st: weekday first day - 2nd: ultimo day
```

<br>Check if date and timezone has summmer time / daylight time
```markdown
import pytz
def is_dst(dt=None, timezone="UTC"):
    if dt is None:
        dt = datetime.utcnow()
    timezone = pytz.timezone(timezone)
    timezone_aware_date = timezone.localize(dt, is_dst=None)
    return timezone_aware_date.tzinfo._dst.seconds != 0
is_dst()													# False => UTC has no daylight time
is_dst(datetime(2019, 1, 1), timezone="US/Eastern")			# False => at this date US/Eastern has no daylight time
is_dst(datetime(2019, 4, 1), timezone="US/Eastern")			# True => at this date US/Eastern has daylight time
is_dst(datetime(2019, 1, 1), timezone="CET")				# False => at this date CET has no daylight time
is_dst(datetime(2019, 4, 1), timezone="CET")				# True => at this date CET has daylight time
```

<br>Timing a specific activity
```markdown
import timeit
start = timeit.default_timer()                          # Start timer
stop = timeit.default_timer()                           # Stop timer
round(stop-start,2)										# Stopped time in seconds and rounded to 2 decimals
round((stop-start)/60,2)                                # Stopped time in minutes and rounded to 2 decimals
timeit.timeit(stmt="[0,1,2]",number=1000000)     		# Checking the time for creating the list for 1mio times
```

<br>Countdown while waiting
```markdown
import time, import sys
time.sleep(3)                                           # Delay for 3 seconds
for i in range (30, 0, -1):                             # Delay for 30 seconds - countdown in one row
    sys.stdout.write (str (i) + ' ')                    # Countdown output
    sys.stdout.flush ()
    time.sleep (1)
```

<br>Check which os system running
```markdown
from sys import platform
if platform == "linux"                                  # Program is excecuting from Linux
if platform == "win32":                                 # Program ix excecuting from Windows
if platform == "darwin":                                # Program is excecuting from Mac
```

<br>Read monitor resolution
```markdown
import ctypes
user32 = ctypes.windll.user32
screensize = user32.GetSystemMetrics(0),                # 1st parameter is width, 2nd parameter is height
    user32.GetSystemMetrics(1)
```


---
## MODULE - CURRENCYCONVERTER - currency conversion
[jump to top...](#python)<br><br>
<br>Import Module
```markdown
from currency_converter import CurrencyConverter
```
Import Module for rate-checks for specific date
```markdown
from datetime import date
```
Read Function CurrencyConverter
```markdown
c = CurrencyConverter()
```
Convert 100 USD to AUD with for actual date
```markdown
c.convert(100, 'USD', 'AUD')
```
Convert 100 USD to AUD for date 2013-03-21
```markdown
c.convert(100, 'USD', 'AUD', date=date(2013, 3, 21))
```
Check begin and end-date for all rates for BGN
```markdown
first_date, last_date = c.bounds['BGN']
```
Read all possible currencies in a set
```markdown
c.currencies
```



---
## MODULE - PYCOUNTRY - Countries, Currency, Language
[jump to top...](#python)<br><br>
<br>Description about the module
```markdown
https://pypi.org/project/pycountry/
```
Problems with some added python modules (eg. pycountry) with pyinstaller => see pyinstaller description<br>
Install moduel
```markdown
import pycountry
```
List of all countries with several informations
```markdown
list(pycountry.countries)
```
Searching for country-informatns for "DE"
```markdown
c = pycountry.countries.get(alpha_2='DE')
```
Outputs => DE
```markdown
c.alpha_2
```
Outputs => DEU
```markdown
c.alpha_3
```
Outputs number of the coutnry => 276
```markdown
c.numeric
```
Outputs full name of the country => Germany
```markdown
c.name
```
Outputs the official name => "Federal Republic of Germany!
```markdown
c.official_name
```
List of all currencies
```markdown
list(pycountry.currencies)
```
List of all languages
```markdown
list(pycountry.languages)
```
List of all historic countries which not more exists
```markdown
list(pycountry.historic_countries)
```
List of all subdivided countries
```markdown
list(pycountry.subdivisiones)
```



---
## MODULES - SMTPLIB, MIMEText - sending emails
[jump to top...](#python)<br><br>
sending emails
if you have 2-Factor-Authentification you must generate a App-Password for GMail<br>
Import smtplib
```markdown
import smtplib
```
Import MIMEText
```markdown
from email.mime.text import MIMEText
```
SMTP-Server and port number from the mail provider (e.g. GMail)
```markdown
s = smtplib.SMTP('smtp.gmail.com', 587)
```
Response 250 means connection is ok
```markdown
print(s.ehlo())
```
Response 250 means connection is ok
```markdown
print(s.starttls())
```
Not the real pw - only the app-generated pw from gmail
```markdown
print(s.login('sender@gmail.com', 'xyz123'))
```
Message of the email
```markdown
msg = MIMEText("This is the text of the mail")
```
One recipient
```markdown
sender = ['sender@gmail.com']
```
One or more recipient
```markdown
recipients = ['recip1@gmail.com']
```
Or more recipients
```markdown
recipients = ['recip1@gmail.com','recip2@r-software.at']
```
Subject
```markdown
msg['Subject'] = "Subject of Mail"
```
From
```markdown
msg['From'] = sender
```
One or more recipients
```markdown
msg['To'] = ", ".join(recipients)
```
Sending email
```markdown
s.sendmail(sender, recipients, msg.as_string())
```
Closing connection
```markdown
s.quit()
```



---
## MODULE - PATHLIB - interacting with the operating system
[jump to top...](#python)<br><br>
<br>Import module
```markdown
from pathlib import Path
```
Current working directory
```markdown
Path.cwd()
```
Creates new folder (no error message if folder allready exists with exist_ok=True)
```markdown
Path("folder").mkdir(parents=True, exist_ok=True)
```



---
## MODULE - OS - interacting with the operating system
[jump to top...](#python)<br><br>
<br>Import module
```markdown
import os
```
Shows alls attributs and methods of the library
```markdown
print(dir(os))
```
Change the directory
```markdown
os.chdir("C:/temp")
```
Current working directory
```markdown
os.getcwd()
```
Outputs the entire content of the current working dir
```markdown
for f in os.listdir(): print(f)
```
Outputs the elements seperated in name + extension
```markdown
for f in os.listdir(): fn, ext = os.path.splitext(f)
```
Change the filenmae
```markdown
os.rename(filename, new_name)
```
Cut and paste file from path1 to path2
```markdown
os.rename(path1+fn, path2+fn)
```
Copy file from source to destination
```markdown
os.system("copy source.txt destination.txt")
```
Creates new folder (also possible with makedirs => is prefered)
```markdown
os.mkdir("folder")
```
Creates new folder and subfolders
```markdown
os.makedirs("folder/subfolder")
```
Delete file
```markdown
os.remove (file)
```
Delete folder (prefered cause deleting ist dangerous)
```markdown
os.rmdir ("folder")
```
Delete folder and subfolders
```markdown
os.removedirs ("folder/subfolder")
```
Outputs the statistics of the file (size, modification time,...)
```markdown
os.stat("file")
```
Outputs dirpath - all the dirs - and all the files
```markdown
for dirpath,dir,fileos in os.walk()
```
Get home dir of the actual user
```markdown
os.environ.get("HOME")
```
Outputs only the filename => file.txt
```markdown
os.path.basename("temp/file.txt")
```
Outputs only the dir => temp/
```markdown
os.path.dirname("temp/file.txt")
```
Outputs filename and dir as a tupel => ("temp/","file.txt")
```markdown
os.path.split("temp/file.txt")
```
Checks if filename exists in the filesystem
```markdown
os.path.exists("temp/file.txt")
```
Checks if folder exists
```markdown
os.path.isdir("xyz")
```
Checks if element is a file
```markdown
os.path.isfile("xyz")
```
Put all filenames to a list from the actual working dir
```markdown
os.listdir()
```
Change file to hidden
```markdown
os.popen('attrib +h ' + fn).read().close()
```

<br>find home-directory for the actual user
```markdown
from os.path import expanduser
home = expanduser("~")
```



---
## MODULE - LOGGING
[jump to top...](#python)<br><br>
general Logging Layers: debug => info => warning => error => critical<br>
importing module
```markdown
import logging
```
Create & Config - w overwrites every time
```markdown
logging.basicConfig(filename="fn.log",format='%(asctime)s %(message)s', filemode='w')
```
Level every log > INFO possible (but not DEBUG)
```markdown
logging.basicConfig(filename="fn.log",level=logging.INFO)
```
getLogger-Name / Level / Time / Message
```markdown
...format="%(name)"s-%(levelname)s:%(asctime)s-%(message)s
```
Creating an object with specific name
```markdown
logger=logging.getLogger(logname)
```
Setting the threshold of logger to DEBUG
```markdown
logger.setLevel(logging.DEBUG)
```
Debug message
```markdown
logger.debug("Harmless debug Message")
```
Info message
```markdown
logger.info("Just an information")
```
Warning message
```markdown
logger.warning("Its a Warning")
```
Error message
```markdown
logger.error("Did you try to divide by zero")
```
Critical error message
```markdown
logger.critical("Internet is down")
```

<br>Example with 2 logging levels
```markdown
logger=logging.getLogger(__name__)							 # Creating an object with the name of the py-file
stream_h = logging.StreamHandler()							 # Defining a handler for streamdata in the console
file_h = logging FileHandler("file.log"						 # Defining a handler for logging to a file
stream_h.setLevel(logging.WARNING)							 # Set Stream-Logging to Warning-Level
file_h.setLevel(logging.ERROR)								 # Set File-Logging to Error-Level
	=> Error-Messages will go to both stream and file - Warning-Messages only to stream and not to file
formatter = logging.formatter								 # Defining the format for outputting
	"%(name)s - %(levelname)s - %(message)s")
stream_h.setFormatter(formatter)							 # Setting format for stream-logging
file_h.setFormatter(formatter)								 # Setting format for file-logging
logger.addHandler(stream_h)									 # Adding Stream-handler to logger
logger.addHandler(file_h)									 # Adding File-handler to logger
```

<br>logging using RotatingFileHandler
<br>https://stackoverflow.com/questions/24505145/how-to-limit-log-file-size-in-python	# Explanation about handling
```markdown
from logging.handlers import RotatingFileHandler             # importing file handler
log_formatter = logging.Formatter('%(asctime)s               # Define format for output in logfile
    %(levelname)s %(funcName)s(%(lineno)d) %(message)s')
my_handler = RotatingFileHandler(logFile, mode='a',          # Define handler with maxBytes and backupCount
    maxBytes=5*1024*1024, backupCount=2, encoding=None,      # When the log grows more then maxBytes...
    delay=0)                                                 # ...itgenerates a new logfile-version
my_handler.setFormatter(log_formatter)                       # Setting the format
my_handler.setLevel(logging.INFO)                            # Setting the threshold of logger to INFO
logger = logging.getLogger('root')                           # Creating an object with name
logger.setLevel(logging.INFO)                                # Setting the threshold of logger to INFO
logger.addHandler(my_handler)                                # Define handler with definition above
```


---
## MODULE - UNITTEST
[jump to top...](#python)<br><br>
<br>Importing module
```markdown
import unittest
```
Import the function which will be tested
```markdown
from prg import func
```
Define the class for testing the function
```markdown
class TestFunc(unittest.TestCase):
```
Define the first testcase - must begin with test*
```markdown
def testcase1(self):
```
call the function
```markdown
erg = func("x",3)
```
check if result is ok
```markdown
self.assertEqual("3x")
```
starting the unittest
```markdown
if __name__ == '__main__': unittest.main()
```
many methods: https://docs.python.org/3/library/unittest.html<br>
Check if equal
```markdown
self.assertEqual(a,b)
```
Check if not equal
```markdown
self.assertNotEquale(a,b)
```
Check if true
```markdown
self.assertTrue(x)
```
Check if false
```markdown
self.assertFalse(x)
```
Check if i in list
```markdown
self.assertIn(i,list)
```
Check if i not in list
```markdown
self.assertNotIn(i,list)
```



---
## MODULE - COLLECTIONS - counter, defaultdic
[jump to top...](#python)<br><br>
Counter, namedtuple, OrderedDict, defaultdict, deque

<br>COUNTER
```markdown
from collections import Counter
colors = ['blue', 'blue', 'red', 'red', "red"]
counter = Counter(colors)									# Creates dict with counts => {'red': 3, 'blue': 2} in ordered form
counter.most_common(1) 		                           		# Outputs the element with the most counts as tuple
counter["red"})            		                            # Outputs the occurence of the value "red" => 3
```

<br>NAMEDTUPLE
```markdown
from collections import namedtuple
Point = namedtuple("Point","x,y")							# Creates class with tumple
pt = Point(1,-4)											# Creates Point(x=1,y=-4)
print(pt.x, pt.y)											# Shows 1 and -4
```

<br>ORDEREDDICT
```markdown
not necessary anymore in the newer python versions
is allready implemented in the regular dict-type)
```

<br>DEFAULTDIC
```markdown
d = defaultdict(int)	# Create defaultdict and define default-type
d["xyz"]				# No key error when when key not in the dict => default-type value 0 is outputed
```

<br>DEQUE
```markdown
from collections import deque      # import collections deque module
d = deque()				# Create deque (optimized for working with elements at the end or beginning of the list)
d.append(1)				# Add element at the end
d.appendleft(2)			# Add element at the beginning
d.extend([1,2]			# Add list of elements at the end
d.extendleft([1,2])		# Add list of elements at the beginning (in reversed order so 2,1)
d.pop()					# Delete element at the end
d.popleft()				# Delete element at the beginning
d.clear()				# Clear entire list
d.rotate(2)				# Shift all elements 2 places to the right
d.rotateleft(-1)			# Shift all elements 1 place to the left
```



---
## MODULE - ITERTOOLS - products, combinations
[jump to top...](#python)<br><br>
- product, permutations, combinations, accumulate, groupby, infinite iterators
<br>- from itertools import product, permutations, combinations, combinations_with_replacement, accumulate, groupby
- from itertools import count, cycle, repeat<br>
necessary for the func-operator
```markdown
import operator
```
all combis for carthesian product => [(1,3),(1,4),(2,3),(2,4)]
```markdown
product([1,2],[3,4])
```
all with 3 elements => (0,0,0),(0,0,1),(0,1,0),(0,1,1), aso.
```markdown
product([0, 1], repeat=3)
```
all combis of this 2 strings => [("a","1"),("a","2"),("b","1"),("b","2")]
```markdown
product('ab', '12')
```
all different orderings => [(1,2,3),(1,3,2),(2,1,3),(2,3,1),(3,1,2),(3,2,1)]
```markdown
permutations ([1,2,3])
```
all different orderings with 2 elements => [(1,2),(1,3),(2,1),(2,3),(3,1),(3,2)]
```markdown
permutations([1,2,3],2)
```
all possible combis for a defined length => [(1,2),(1,3),(1,4),(2,3),(2,4),(3,4)]
```markdown
combinations([1,2,3,4],2)
```
all combis also with itself => [(1,1),(1,2),(1,3),(2,2),(2,3),(3,3)]
```markdown
combinations_with_replacement([1,2,3],2)
```
accumulates every number with the next => [1,3,6,10]
```markdown
accumulate([1,2,3,4])
```
using operator .mul for multiplication every number the next => [1,2,6,24]
```markdown
accumulate([1,2,3,4], func=operator.mul)
```
compares every entry to the maximum => [1,2,5,5,5]
```markdown
accumulate([1,2,5,3,4], func=max)
```
gives interabel - groups by the func => True[1,2], False[3]
```markdown
groupby([1,2,3],key=func_smaller3)
```
same thing - with a lambda operation => True[1,2], False[3]
```markdown
grougpy([1,2,3],key=lambda x: x<3)
```
infinite loop starting at 10 (has to be ended with break sometimes)
```markdown
for i in count(10)
```
infinite cycle through the list (has to be ended with break sometimes)
```markdown
for i in cycle([1,2,3])
```
infinite loop with 1
```markdown
for i in repeat(1)
```
loop with 1 for 4 times
```markdown
for i in repeat(1,4)
```



---
## MODULE - NUMPY - basis for different other modules
[jump to top...](#python)<br><br>
- memory efficient, working in the background used by other modules
<br>- using only the bits which are necessary for each column (1 is stored in python with 24bytes - in numpy with 1byte or lesser)
- shape of array has to be consistent - otherwise it just fall back to regular python objects eg. [[12,11],[13]]<br>
Import numpy module with np abbreviation
```markdown
import numpy as np
```
Using arrays, types and slicing<br>
Define a numpy array (automatically with type int)
```markdown
a = np.array([1,2,3,4])
```
Multiindexing in arrays possible => gives array/[0.,1.,2.])
```markdown
a[[0,2,-1]]
```
Defines a numpy array with datatype float (and not int)
```markdown
np.array([1,2,3,4]),dtype=np.float)
```
Defines a 2d numpy array
```markdown
a = np.array([[1,2,3],[4,5,6],[7,8,9])
```
Returns dimension shape => (3,3)
```markdown
a.shape
```
Returns number of dimensions => 2
```markdown
a.ndim
```
Returns total number of elements => 9
```markdown
a.size
```
Gives / slices the second row => [4,5,6]
```markdown
a[1]
```
Gives / slices the second row and first element => 4
```markdown
a[1,0]
```
Slices the first 2 rows => array([[1,2,3],[4,5,6]])
```markdown
a[0:2]
```
Slices all row with first 2 elements => array([[1,2],[4,5],[7,8]])
```markdown
a[:,:2]
```
Slices first 2 rows and first 2 elements => array([[1,2],[4,5]])
```markdown
a[:2,:2]
```
Slices first 2 rows and last element => array([[3],[6]])
```markdown
a[:2,2:]
```
Changes content of second row => array([[1,2,3],[9,9,9],[7,8,9])
```markdown
a[1] = np.array([9,9,9])
```
Changes content of third row (for all elements) => array([[1,2,3],[4,5,6],[8,8,8])
```markdown
a[2] = 8
```
Builds the sum of all elements => 45
```markdown
a.sum()
```
=> 5.0
```markdown
a.mean()
```
Return standard deviation => 2.58198889774344
```markdown
a.std()
```
Builds sum per columns => array([12,15,18])
```markdown
a.sum(axis=0)
```
Builds sum per rows => array([6,15,24])
```markdown
a.sum(axis=1)
```
Initialize numpy array with 5 zeros => array([0.,0.,0.,0.,0.])
```markdown
np.zeroes(5)
```
Initialize numpy array with 2x3 ones with int32 => array([[0,0,0],[0,0,0]])
```markdown
np.ones((2,3),dtype="int32")
```
Initialize np array with 2x2 with the value 99 => array([[99,99],[99,99]])
```markdown
np.full((2,2,),99)
```
Initialize a square matrix with len 3 => array([[1.,0.,0.],[0.,1.,0.],[0.,0.,1.]])
```markdown
np.identity(3)
```
Separate individual copy of the numpy array (no updates in both arrays)
```markdown
arr_b = arr_a.copy()
```
Define 2d numpy array with 2,4 dimension
```markdown
c = np.array([[1,2,3,4],[5,6,7,8]])
```
Reshape the numpy array to 4,2 dimension => [[1,2],[3,4],[5,6],[7,8]]
```markdown
c.reshape((4,2))
```
Reshape the numpy array to 3d with 2,2,2 dimension => [[[1,2],[3,4]],[5,6],[7,8]]]
```markdown
c.reshape((2,2,2))
```

Vector handling<br>
Build array with this range => array([0,1,2,3])
```markdown
a = np.array(4)
```
Changes +10 to each element => array([10,11,12,13]) (creates new array - no changing a)
```markdown
a + 10
```
Changes *10 to each element => array([0,10,20,30]) (creates new array - no changing a)
```markdown
a * 10
```
Changes the existing array a => array([100,101,102,103])
```markdown
a += 100
```
Defines second array babab6
```markdown
b = np.array([10,10,10,10])
```
Sums the 2 arrays to new array => array([10,11,12,13)
```markdown
a + b
```
Multiplicates the 2 arrays to new array => array([0,10,20,30)
```markdown
a * b
```
Make sinus of all entries
```markdown
np.sin(b)
```
Make cosinus of all entries
```markdown
np.cos(b)
```

Boolean Array Operations<br>
Build array with this range => array([0,1,2,3])
```markdown
a = np.array(4)
```
Selecting items with boolean expressions - returns first and last element => array([0,3])
```markdown
a[True,False,False,True]
```
Use operation on the array => array([False,False,True,True])
```markdown
a >= 2
```
Using operation for slicing => array([2,3])
```markdown
a[a >= 2]
```
Gives back all elements which are greater than the mean => array([2,3])
```markdown
a[a > a.mean()]
```
Gives back all elements which are NOT greater than the mean => array([0,1])
```markdown
a[~(a > a.mean())]
```
Gives back all elements which are equal to 0 OR 1 => array([0,1])
```markdown
a[(a==0) | (a==1)]
```
Gives back all elements which are <=2 and have no rest divided by 2 => array([0,2])
```markdown
a[(a <= 2) & (a % 2 == 0)]
```

Creating random arrays<br>
Random 1d float array with 3 entries => eg. (0.8377, 0.8720, 0,7784)
```markdown
np.random.rand(3)
```
Random 2d array 3 entries => [[0.27,0.91,0.54],[0.68,0.87,0.36],[0.05,0.64,0.16]]
```markdown
np.random.rand(3,3)
```
Random 1d int array 3 entries => [0,8,8]
```markdown
np.random.randint(0,10,3)
```
Random 2d int array 3x4 entries => [[2,6,4,5],[7,6,7,3],[7,0,4,0]]
```markdown
np.random.randint(0,10,(3,4))
```
Random 2d int array 3x3 entries with values from 0 to 99
```markdown
np.random.randint(100, size(3,3))
```
Random 2d int array 3x3 entries with values from -4 to 7
```markdown
np.random.randint(-4,8,size(3,3))
```
Shuffeling a 2d list but only the first axes
```markdown
np.random.shuffle(lst)
```
Can reproduce the same results
```markdown
np.random.seed(1)
```



---
## MODULE - PANDAS - analyzing and working with data
[jump to top...](#python)<br><br>
<br>examples
```markdown
https://gist.github.com/why-not/4582705
```
Import Module
```markdown
import pandas as pd
```
Also importing numpy-module necessary
```markdown
import numpy as np
```
Show more information - count of the shown columns
```markdown
pd.set_option('display.max_columns',11)
```
Show more information - None is using the maximum width of the IDE
```markdown
pd.set_option('display.width', None)
```

SERIES<br>
Define a series
```markdown
s = pd.Series([35,63,81,61,127,65,319])
```
Shows default-index in 1 row / values in 2 row - also the dtype: int64 at the bottom
```markdown
print(s)
```
Name the series (shows the name also when series i printed at the bottom
```markdown
s.name = "G7 population in millions"
```
Shows the dtype of the series => dtype("int64")
```markdown
s.dtype
```
Values of the series => array([35,63,81,61,127,65,319])
```markdown
s.values
```
Slicing element => 35
```markdown
s[0]
```
Shows the index of the series => RangeIndex(start=0, stop=7, step=1)
```markdown
s.index
```
Shows first index-value
```markdown
s.index[0]
```
Change the index of the series from default 0-6 to country-names
```markdown
s.index=["CAN","FRA","GER","ITA","JPN","UK","USA]
```
Accessing now with the new index possible => 81
```markdown
s["GER"]
```
Access with index still possible using iloc => 35
```markdown
s.iloc[0]
```
Access with index still possible using iloc => 319
```markdown
s.iloc[-1]
```
Multiple selecting possible => GER 81 and JPN 127
```markdown
s.["GER","JPN"]
```
Multiple selecting with index using iloc possible => CAN 35 and USA 319
```markdown
s.iloc[0,-1]
```
Multiple selecting with ":" - upper element is included => CAN 35, FRA 63, GER 81
```markdown
s.["CAN":"GER"]
```
Add 10 for the every element in the series => ([45,73,91,71,137,75,329])
```markdown
s + 10
```
Using boolean operation to output every element => GER 81, JPN 127, USA 319
```markdown
s[s > 70]
```
Using boolean operation to output countries > mean => JPN 127, USA 319
```markdown
s[s > s.mean()]
```
~ for not, | for or, & for and
```markdown
logical operator which can be used
```
Changing the value of a series element => CAN 40
```markdown
s["CAN"] = 40
```
Changing the value of the last element => USA 500
```markdown
s.iloc[-1] = 500
```
Changing the value with a specific operation => CAN,FRA,ITA,UK are changed to 99
```markdown
s[s < 70] = 99
```
Define a series with NaN values
```markdown
s = pd.Series([1,np.nan,7]
```
Check for NaN values in the series => False,True,False
```markdown
d.isnull()
```
Check for NOT NaN values in the series => True,False,True
```markdown
s.notnull()
```
Sum of not NaN values in the series => 2
```markdown
s.notnull().sum()
```
Sum of NaN values in the series => 1
```markdown
s.isnull().sum()
```
Outputs all entries which are not NaN
```markdown
s.[s.notnull()]
```
Delete all entries with NaN
```markdown
s.dropna()
```
Replace the NaN-values with 0
```markdown
s.fillna(0)
```
Replace the NaN-values with the meanvalue of the serie
```markdown
s.fillna(s.mean())
```
With forward-fill the NaN-values are replaced with the value before (if the first i gets NaN)
```markdown
s.fillna(method="ffill")
```
With backward-fill the NaN-values are replaced with the value after (if the last i gets NaN)
```markdown
s.fillna(method="bfill")
```
Returns the duplicates (only the first entry for the same is no duplicate - rest gets True)
```markdown
s.duplicated()
```
Returns the duplicates (only the last entry for the same value is no duplicate - rest gets True)
```markdown
s.duplicated(keep="last")
```
Returns the duplicates (when there are more than one value - all get flagged as duplicate with True)
```markdown
s.duplicated(keep=False)
```
Duplicates get dropped (only the first entry remains)
```markdown
s.drop_duplicates()
```
Duplicates get dropped (only the last entry remains)
```markdown
s.drop_duplicates(keep="last")
```
Duplicates get dropped (no entry remains if there are duplicate entries for the value)
```markdown
s.drop_duplicates(keep=False)
```
Sorting by value ascending
```markdown
s.sort_values()
```
Sorting by value descending
```markdown
s.sort_values(ascending=False)
```

<br>DATAFRAMES
<br>are immutable, column is a series, dataframe = combination of multiple series
<br>reading data
<br>possible reader: read_csv,read_excel,read_json,read_html,read_sql
<br>possible writer: to_csv,to_excel,to_json,to_html,to_sql

CSV<br>
Shows all parameters for the reader
```markdown
pf.read_csv?
```
Read csv into dataframe - first line will be col-names of the dataframe
```markdown
df = pd.read_csv("fn.csv")
```
Read csv into dataframe - no headerline (col names will be default numeric)
```markdown
df = pd.read_csv("fn.csv",header=None)
```
")							=> Read csv with sepeartor "=>" instead of the default ";"
```markdown
df = pd.read_csv("fn.csv",sep="
```
Many operations can be directly done when reading the csv-file
```markdown
df = pd.read_csv("fn.csv",
```
=> no header in the csv available
```markdown
header=None
```
=> name the columns
```markdown
names=["Timestamp","Price"],
```
=> define which column will be the index
```markdown
index_col=0,
```
=> read dates as date - and not as string
```markdown
parse_dates=True,
```
=> treat this chars as NaN-values
```markdown
na_values["?","-",""],
```
=> assign specific datatype to the column "Price"
```markdown
dtype={"Price":"float"},
```
=> decimal-point is "," (and not ".")
```markdown
decimal=",",
```
=> read also blank lines (as default they are ignored)
```markdown
skip_blank_lines=False),
```
=> use only the three columns when reading the csv (by position)
```markdown
usecols=[0,1,2],
```
=> use only the three columns when reading the csv (selected by name)
```markdown
usecols=["first","last","age"])
```
Write dataframe to csv
```markdown
df.to_csv("fn2.csv")
```

XLSX<br>
Read xlsx (first worksheet) into dataframe
```markdown
df = pd.read_excel("file.xlsx")
```
Read xlsx (first worksheet) into dataframe - without headers
```markdown
df = pd.read_excel("file.xlsx",header=None)
```
Read xlsx and define the first column as index of the dataframe
```markdown
df = pd.read_excel("file.xlsx",index_col=[0])
```
Read xlsx (worksheet "Prod") into dataframe
```markdown
df = pd.read_excel("file.xlsx",sheet_name="Prod")
```
Read xlsx with the ExcelFile method
```markdown
ef = pd.ExcelFile("file.xlsx")
```
Shows alle worksheet-names as a list => eg. ["Prod","Desc"]
```markdown
ef.sheet_names
```
Read/Parse the worksheet "Prod" in a dataframe
```markdown
df = ef.parse("Prod")
```
Write dataframe to xlsx
```markdown
df.to_excel("file2.xlsx",
```
Write to worksheet "Prod"
```markdown
sheet_name="Prod",
```
Start writing at row 1
```markdown
startrow=1,
```
Start writing at col 2
```markdown
startcol=2)
```
Write dataframe to xlsx with the ExcelWriter method
```markdown
w = pd.ExcelWriter("file2.xlsx")
```
Write dataframe to xlsx worksheet "Prod" with the ExcelWriter method
```markdown
with w: df.to_excel(w,sheet_name="Prod"
```
Write multiple worksheet to xlsx from dataframes
```markdown
with pd.ExcelWriter("file2.xlsx") as writer:
```
Dataframe1 stored in worksheet "Prod"
```markdown
df1.to_excel(w, sheet_name="Prod")
```
Dataframe2 stored in worksheet "Desc"
```markdown
df2.to_excel(w, sheet_name="Desc")
```

SQL<br>
Establish connection to the sql-db
```markdown
conn = sqlite3.connect("data.db")
```
Read data from sql-db into dataframe
```markdown
df = pd.read_sql("SELECT * FROM empl;",conn)
```
Many operations can be directly done when reading the sql-db
```markdown
df = pd.read_sql("SELECT * FROM empl;",conn,
```
=> define which column will be the index
```markdown
index_col="EmplID",
```
=> read this columns as date
```markdown
parse_dates["BirthDate","HireDate"])
```
It is easier to read a complete table using sqlalechmy
```markdown
from sqlalchemy import create_engine
```
Create SQL Alchemy engine
```markdown
engine = create_engine("data.db")
```
Establish connection with SQL Alchemy
```markdown
connection = engine.connect()
```
Read whole table with SQL-Alechmy (many things are auto-done - e.g. Indexing,Parsing)
```markdown
df = pd.read_sql_table("empl",con=connection)
```
Writes dataframe to the sql-db (breaks when table allready exists)
```markdown
df.to_sql("data.db",conn)
```
Writes dataframe to the sql-db (with droping the table before inserting)
```markdown
df.to_sql("data.db",conn,if_exists="replace")
```
Writes dataframe to the sql-db (with inserting new values to existing table)
```markdown
df.to_sql("data.db",conn,if_exists="append")
```

HTML<br>
Read html into dataframe
```markdown
df = pd.read_html(html_string)
```
Assign html-varialbe
```markdown
html_url"https://www.xyz.com"
```
Read html-link to dataframe
```markdown
df = pd.read_html(html_url)
```

<br>EXAMPLE
```markdown
https://www.freecodecamp.org/learn/data-analysis-with-python/data-analysis-with-python-course/pandas-condtitional-selection-and-modifying-dataframes
    Popl	HDI		Continent
CAN	35		0,913	America
FRA	64		0,888	Europe
GER	81		0,916	Europe
ITA 61		0,873	Europe
JPN 127		0,891	Asia
UK  65		0,907	Europe
USA 319		0,915	America
```

<br>Initialize a dataframe with random ints with 5 rows and 2 columns
```markdown
df = pd.DataFrame(np.random.randint(0,5,size=(5, 2)), columns=list('AB'))
```
Show the shape of the dataframe (rows, columns) => (7,3)
```markdown
df.shape
```
Info for columns (index,name,dtype) also count of NaN-values per column
```markdown
df.info()
```
Shows datatype of every column
```markdown
df.dtpyes()
```
Several statistic for the dataframe (median,max,min,std,...)
```markdown
df.describe()
```
Output of the first 5 rows per default
```markdown
df.head()
```
Output of the first 22 rows
```markdown
ead(22)
```
Output of the last 5 rows per default
```markdown
df.tail()
```
Output of the last 22 rows
```markdown
df.tail(22)
```
Output of all column names
```markdown
df.columns
```
Rename the columns
```markdown
df.columns["POPL","hdi","CONT"]
```
Outputs the index
```markdown
df.index
```
Set index to column "name"
```markdown
df.index = df["name"]
```
Assigning new index - replaces the default numeric index
```markdown
df.index = ["CAN","FRA","GER","ITA","JPN","UK","USA"]
```
Outputs the size of the dataframe
```markdown
df.size
```
Resets the index - with inplace it is permanently saved
```markdown
df.reset_index(inplace=True)
```
Define "Popl" as new index - with inplace it is permanently saved
```markdown
df.set_index("Popl", inplace=True)
```
Selecting Rows by index - showing the row with the index = "CAN"
```markdown
df.loc["CAN"]
```
Selecting Rows by position - showing the last row
```markdown
df.iloc[-1]
```
Selecting Columns by title - showing the whole column "Population" for all rows
```markdown
df["Popl"]
```
Output of alle values with their count
```markdown
df["Continent"].value_counts()
```
Output of alle values with their count in percent
```markdown
df["Continent"].value_counts(normalize=True)
```
Showing cols Popl,Continent for all rows
```markdown
df[["Popl","Continent"]]
```
Showing cols Popl,Continent for all rows - values divided by 100
```markdown
df[["Popl","Continent"]] / 100
```
Show the rows from index CAN to ITA
```markdown
df.loc["CAN":"ITA"]
```
Show the rows from index CAN to ITA - only with the column1
```markdown
df.loc["CAN":"ITA","Popl"]
```
Show the rows from index CAN to ITA - only with the column1 + column3
```markdown
df.loc["CAN":"ITA",["Popl","Continent"]]
```
Show the columns col1 to col4 for all rows
```markdown
df.loc[:,"col1":"col4"]
```
Show the columns col1 to col4 for 3 rows from index 0 to 2 (2 included)
```markdown
df.loc[0:2,"col1":"col4"]
```
Show the columns cols 1 and 3 for the rows from index 0 to 2 (2 included)
```markdown
df.loc[0:2,["col1","col3"]]
```
Show the 1st and last row => CAN,USA
```markdown
df.iloc[0,-1]
```
Show 2nd and 3rd row for all cols => FRA,GER / Popl,HDI,Continent
```markdown
df.iloc[1:3]
```
Show 2nd and 3rd row for 2nd col => FRA,GER / HDI
```markdown
df.iloc[1:3,1]
```
Show 2nd and 3rd row for 1st and 3rd column => FRA,GER / Popl,Continent
```markdown
df.iloc[1:3,[0,2]}
```
Show 2nd and 3rd row for the 2nd and 3rd col => FRA,GER / HDI,Continent
```markdown
df.iloc[1:3,1:3]
```
Returns series with boolean True/False for every row (F,F,T,F,T,F,T)
```markdown
df["Popl"] > 70
```
Returns GER,JPN,USA for all cols
```markdown
df.loc[df["Popl"]] > 70
```
Returns GER,JPN,USA for col "Popl"
```markdown
df.loc[df["Popl"] > 70, "Popl"]
```
Returns GER,JPN,USA for cols "Popl" and "Continent"
```markdown
df.loc[df["Popl"] > 70, ["Popl","Continent"]]
```
Output of 2 columns for the column slice
```markdown
df[["Open","Close"]]["2010":"2020"]
```
Output specific rows and slice of columns
```markdown
df[df.index.isin(["2020","2019"])][hist.columns[0:4]]
```
Output specific rows and columns
```markdown
df[df.index.isin(["2020","2019"])][["Open","Close"]]
```
Drops the row CAN
```markdown
df.drop("CAN")
```
Drops the rows CAN,JPN
```markdown
df.drop(["CAN","JPN"])
```
Drops the rows CAN,JPN (2nd method)
```markdown
df.drop(["CAN","JPN"],axis=0)
```
Drops the rows CAN,JPN (3rd method)
```markdown
df.drop(["CAN","JPN"],axis="rows")
```
Drops the cols Popl,Continent
```markdown
df.drop(columns=["Popl","Continent"])
```
Drops the cols Popl,Continent (2nd method)
```markdown
df.drop(["Popl","Continent"],axis=1)
```
Drops the cols Popl,Continent (3rd method)
```markdown
df.drop(["Popl","Continent"],axis="columns")
```
Drops the whole dataframe
```markdown
df.drop(df.index, inplace=True)
```
Define series with same col-names as in the dataframe - with some correction values
```markdown
crisis = pd.Series([-10,-0,3],index=["Popl","HDI"])
```
Comines crisis-series to the df => all values in "Popl" -10 and "HDI" -0,3 in the df
```markdown
df[["Popl","HDI"]] + crisis
```
Define new series for new column in dataframe
```markdown
langs = pd.Series(
```
=> values of new column
```markdown
["FR","DE","IT"],
```
=> existing index in dataframe
```markdown
index=["FRA","GER","ITA"],
```
=> name of the new column
```markdown
name= "lang")
```
Creates new column in the dataframe according to the series "langs" - other rows will get "NaN"
```markdown
df["lang"] = langs
```
Values of all rows in the column "lang" will be changed to "GB"
```markdown
df["lang"] = "GB"
```
Renames column names
```markdown
df.rename(columns={"Popl":"POPL","Continent":"CONT"})
```
Renames index names
```markdown
df.rename(index={"UK":"UnKi","USA":"US"})
```
Creates new column by dividing col "Popl" with col "HDI"
```markdown
df["Popl_HDI"] = df["Popl"] / df["HDI"]
```
Different operations for the column in the dataframe
```markdown
df["Popl"].median().max().min().sum().mean().qunatile()
```
Changes Timestamp-String to Timestamp-Type (eg. read from csv-file before)
```markdown
df["Timestamp"]=pd.to_datetime(df["Timestamp"])
```
Plotting the dataframe using the mathlib-module
```markdown
df.plot()
```
Plot the dataframe
```markdown
df.plot(figsize=(12,6))
```
Plot the dataframe for the specific timeframe
```markdown
df.loc["2017-12-01":"2019-12-01"].plot(figsize=(12,6)))
```
Check for NaN values in the Dataframe => Matrix with True / False
```markdown
df.isnull()
```
Check for NOT NaN values in the Series => Matrix with True / False
```markdown
df.notnull()
```
Sum of NaN values per column
```markdown
df.isnull().sum()
```
Deleting all rows with at least one NaN value in it
```markdown
df.dropna()
```
Deleting all columns with at least one NaN value in it
```markdown
df.dropna(axis=1)
```
Deleting all rows where all columns are NaN
```markdown
df.dropna(how="all")
```
Deleting all rows where at least 3 columns are NOT NaN
```markdown
df.dropna(thresh=3)
```
Replace NaN values with text
```markdown
df.fillna("missing")
```
With forward-fill NaN-values are replaced with the value before (axis=0 means vertical / per column)
```markdown
df.fillna(method="ffill",axis=0)
```
With forward-fill NaN-values are replaced with the value before (axis=0 means horizontal / per row)
```markdown
df.fillna(method="ffill",axis=1)
```
Shows the existing values for the column => eg: "M","F","D","?" (M/F is correct and D/? is wrong)
```markdown
df["Sex"].unique()
```
Shows the count of each existing value in the column => eg. "M" 175, "F" 132, "D" 5, "?", 3 => so 8 wrong entries
```markdown
df["Sex"].value_counts()
```
Change all "D" values in the column to "F"
```markdown
df["Sex"].replace("D","F")
```
Change all "D" to "F" and "N" to "M" in the column
```markdown
df["Sex"].replace({"D":"F","N":"M"})
```
Find all the invalid values in the age-column => eg. greater than 100 is invalid entry
```markdown
df[df["Age"] > 100]
```
Fixing the invalid values for age by dividing it to 100
```markdown
df.loc[df["Age"]>100,"Age"]=df.loc[df["Age"]>100,"Age"]/100
```
Defines new filter
```markdown
filt = (df["col1" == "col1_val1"])
```
Defines new filter with several values
```markdown
filt2 = (df["col1"].isin(["val1","val2","val3"]))
```
Defines new filter NOT with several values
```markdown
filt3 = (~df["col1"].isin(["val1","val2","val3"]))
```
Defines new filter with a > operator
```markdown
filt4 = (df["col1"] > 123)
```
Outputs the result for the above filter
```markdown
df[filt]
```
Outputs the result for the above filter with only col2
```markdown
df[filt]["col2"]
```
Filter the elements for the top 2.5% of the dataset (quantile)
```markdown
df= df[(df['value'] >= df['value'].quantile (0.025))]
```
Filter the elements for the bottom 2.5% of the dataset (quantile)
```markdown
df= df[(df['value'] < df['value'].quantile (0.975))]
```
Check duplicates for all rows (only first entry is not flagged as True)
```markdown
df.duplicated()
```
Check duplicates for all rows (only last entry is not flagged as True)
```markdown
df.duplicated(keep="last")
```
Check duplicates for all rows (every entry is flagged as True)
```markdown
df.duplicated(keep=False)
```
Check duplicates only for subset-col (only first entry is not flagged as True)
```markdown
df.duplicated(subset=["Name"])
```
Check duplicates only for subset-col (only last entry is not flagged as True)
```markdown
df.duplicated(subset=["Name"],keep="last")
```
Check duplicates only for subset-col (every entry is flagged as True)
```markdown
df.duplicated(subset=["Name"],keep=False)
```
Split all the strings in the column at the blank-char "_" => eg. results [1987, M, US, 1]
```markdown
df["Data"].str.split("_")
```
Split all the strings in the column at the blank-char and build seperate new columsn in the dataframe
```markdown
df["Data"].str.split("_",expand=True)
```
Check column if there exists an "U" in the string-values (True / False output as series) - also regex possible
```markdown
df["Data"].str.contains("U")
```
Eliminate the whitespaces at the beginning and end for the string-values
```markdown
df["Data"].str.strip()
```
Replace / Deletes blanks " " in the string-values
```markdown
de["Data"].str.replace(" ","")
```
Function lower is used for the whole dataframe
```markdown
df.apply(lambda x: x.lower())
```
Function lower is used for the first 3 columns
```markdown
df.apply(lambda x: x.lower(), axis="columns")[0:3]
```
Sorting the new index ascending
```markdown
df.sort_index(inplace=True)
```
Sorting the columns in dataframe
```markdown
df.reindex(sorted(df.columns), axis=1)
```
Sorting by column ascending
```markdown
df.sort_values(by="co1")
```
Sorting by column descending
```markdown
df.sort_values(by="co2",ascending=False)
```
Sorting by 2 columns descending - first col1 and then col2
```markdown
df.sort_values(by=["col1","col2"],ascending=False)
```
Sorting a series for one specific col descending
```markdown
df["col1"].sort_value(ascending=False)
```
Change the column titles to uppercase
```markdown
df.columns =) [x.upper() for x in df.columns]
```
Function lower is used for the whole column
```markdown
df["c1"] = df["c1"].apply(lambda x: x.lower())
```
Change the names of the values - all others become NaN
```markdown
df["c1"].map({"val1":"val1new","val2":"val2new"})
```
Change the names of the values - all others are not touched
```markdown
df["c1"].replace({"val1":"val1new","val2":"val2new"})
```
New column at the end
```markdown
df["cnew1"] = df["c1"] + df["c2"]
```
Deleting 2 columns
```markdown
df.drop(columns=["c1","c2"], inplace=True)
```
Add new row (all other cols are defined as NaN for the row)
```markdown
df = df.append({"c1":"val1"},ignore_index=True)
```
Outputs the 5 highest values in the column - only col1
```markdown
df["col1"].nlargest(5)
```
Outputs the 5 highest values in the column - all columns
```markdown
df.nlargest(5,"col1")
```
Outputs the 5 lowest values in the column - all columns
```markdown
df.nsmallest(5,"col1")
```
Grouping according to col1
```markdown
col1_grp = df.groupby("col1")
```
Access to one value from the group
```markdown
col1_grp.get_group("col1_value")
```
Grouping col1 and output median for col2
```markdown
col1_grp["col2"].median()
```
Grouping col1 and output median for col2 only for 3 group-values
```markdown
col1_grp["col2"].median().loc[["A","B","C"]]
```
Filtering all Values with 0
```markdown
non_zero = df[df["col1"]!=0]
```
Add new column with Y/N depending if the value in col "Sales" is > 50
```markdown
df["newcol"]=["Y" if x > 50 else "N" for x in df["Sales"]]
```
Change existing column with Y/N depending if the value in col is > 50
```markdown
df["col"]=["Y" if x > 50 else "N" for x in df["col"]]
```
Add/change column with 0/1 depending of calc of the variables x/y from 2 cols
```markdown
df["c"]=[1 if (x/y>9) else 0 for x,y in zip(df["c1"],df["c2])]
```



---
## MODULE - MATPLOTLIB - working with charts
[jump to top...](#python)<br><br>
<br>Import module as plotter plt
```markdown
import matplotlib.pyplot as plt
```
Plot a line
```markdown
plt.plot(x, x **2 )
```
Plot another line (in the other direction)
```markdown
plt.plot(x, -1 * (x ** 2))
```
Define x values
```markdown
x_values = list(range(1000))
```
Define y values / squares
```markdown
squares = [x**2 for x in x_values]
```
Plot diagram with x- and y-axes
```markdown
plt.plot(x_values, squares)
```
Plot 1st row, 2nd col in the 2nd diagram (any line after that will only access the 2nd diagram)
```markdown
plt.subplot(1,2,2)
```
Sscatter diagram with x- and y-axes and line strenght = 5
```markdown
plt.scatter(x_values, squares, s=5)
```
Title with fontsize = 24
```markdown
plt.title("Title", fontsize=24)
```
X-Axe title with fontsize = 18
```markdown
plt.xlabel("X-Axe", fontsize=18)
```
Y-Axe title with fontsize = 18
```markdown
plt.ylabel("Y-Axe", fontsize=18)
```
Params describtion with fontsize = 10
```markdown
plt.tick_params(axis="both", which="major", labelsize=10)
```
Define scaling of axes
```markdown
plt.axis([0,1100,0,1100000])
```
Colors from one shade to another with different params
```markdown
plt.scatter(x,y,c=squares,cmap=plt.cm.Blues,edgecolor="none", s=10)
```
Expoit the first point larger in green
```markdown
plt.scatter(x[0],y[0],c="green",edgecolor="none", s=100)
```
Expoit the last point larger in red
```markdown
plt.scatter(x[-1],y[-1],c="red",edgecolor="none", s=100)
```
Hide the complete x-axis description
```markdown
plt.axes().get_xaxis().set_visible(False)
```
Hide the complete y-axis description
```markdown
plt.axes().get_yaxis().set_visible(False)
```
Define custom figure size
```markdown
plt.figure(dpi=128, figsize=(10,6))
```
Show diagram
```markdown
plt.show()
```
Save diagram as png-picture-file
```markdown
plt.savefig("example.png",bbox_inches="tight")
```



---
## MODULE - SELENIUM - browser automatization
[jump to top...](#python)<br><br>
chromedriver.exe in Ordner von py-file speichern<br>
Different methods for locating elements
```markdown
https://selenium-python.readthedocs.io/locating-elements.html
```
Import WebDriver für Zugriff auf URL
```markdown
from selenium import webdriver
```
Import Time-Library für Verzögerungen wenn notwendig
```markdown
import time
```
Import Keys to send Key-strokes
```markdown
from selenium.webdriver.common.keys import Keys
```
Driver für Chrome definieren - mit akt. Ordner os.getcwd
```markdown
driver = webdriver.Chrome(os.getcwd() + '/chromedriver')
```
Zugriff auf die URL
```markdown
driver.get("url")
```
Click auf ein ELement (Copy ) - mit Untersuchen - Copy XPath
```markdown
driver.find_element_by_xpath('//*[@id="button"]/input').click()
```
Manchmal notwendig um Verarbeitung abzuwarten
```markdown
time.sleep(1)
```
Feld Name wird mit Inhalt x befüllt
```markdown
driver.find_element_by_xpath('//*[@id="name"]').send_keys("x"])
```
Text wird in Feld eingetragen
```markdown
driver.find_element_by_name("q").send_keys("txt")
```
Text wird in Feld eingetragen und Enter gedrückt
```markdown
driver.find_element_by_name("q").send_keys("txt" + u'\ue007')
```
Feld word nach ID gesucht
```markdown
driver.find_element_by_id("xy-id")
```
Felder werdem nach Class gesucht (als Liste)
```markdown
driver.find_elements_by_class_name("cl")[0]
```
Felder werdem nach Tag gesucht (als Liste)
```markdown
driver.find_elements_by_tag_name("tag")[0]
```
Send single keyboard-elements <> chars (needs import keys)
```markdown
driver.send_keys(Keys.Backspace,Keys.ARROW_LEFT,Keys.ENTER)
```
Send an Return-keystroke (eg. for enter after data entries in fields)
```markdown
driver.send_keys (u'\ue007')
```
Enter wird gedrückt bzw. die Seite abgeschickt
```markdown
field.submit()
```
Driver schließen (sonst schließt sich das Fenster nicht)
```markdown
driver.quit()
```
Titel der HTML-Seite
```markdown
driver.title
```
Back-Function in browser-history
```markdown
driver.back()
```
Forward-Function in browser-history
```markdown
driver.forward()
```
Define an individual cookie
```markdown
cookie = {"name": "token", "value": "23874kljdsjhfaökldjs"}
```
Use Cookie
```markdown
driver.add_cookie(cookie)
```
Outputs a specific cookie
```markdown
driver.get_cookie("token")
```
Outputs all cookies
```markdown
driver.get_cookies())
```
Read current, actual url
```markdown
driver.current_url
```
Swith to a frame-id (eg. a PopUp)
```markdown
driver.switch_to.frame ("frame_id")
```
Read active window name
```markdown
act_window = driver.current_window_handle
```
Switch (back) to active window (eg. after working on the popup-frame or popup-window)
```markdown
driver.switch_to.window(act_window)
```

<br>Use Selenium with chrome windows hidden
```markdown
from selenium.webdriver.chrome.options import Options
options = Options()
options.add_argument('--headless')                                          # Window Hidden (only used this for the final program - not during devleopment / testing!)
if platform == "win32": options.add_argument('--start-maximized')           # Window Started Maximized (for Windows)
elif platform in ["linux","darwin"]: options.add_argument('--kiosk')        # Window Started Maximized (for Linux and Mac)
options.add_experimental_option ('excludeSwitches', ['enable-logging'])     # No error messagegs when exec in cmd
driver = webdriver.Chrome(os.getcwd() + '/chromedriver', options=options)
```

<br>Scroll to the very bottom of a site - eg. Twitter, Facebook, Stocktwits,...
```markdown
lenOfPage = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
match=False
while(match==False):
    lastCount = lenOfPage
    time.sleep(1)
    lenOfPage = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
    if lastCount==lenOfPage:
        match=True
```

<br>When there are problems clicking an element on a page
```markdown
Method1:
element = driver.find_element_by_id('datePickerToggleBtn')
webdriver.ActionChains(driver).move_to_element(element ).click(element ).perform()

Method2:
element = driver.find_element_by_css('div[class*="loadingWhiteBox"]')
driver.execute_script("arguments[0].click();", element)
```

<br>Wait till a specific element is loaded
```markdown
WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.NAME, "agree"))).click()
WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "YDC-Col1")))
```

<br>Take a screenshot when something fails in headless mode
```markdown
try:
    ...
    do the whole selenium work...
    ...
except:
    driver.get_screenshot_as_file("a.jpeg")
```



---
## MODULE - BEAUTIFUL SOAP - webscraping
[jump to top...](#python)<br><br>
<br>Import module for beautiul soap
```markdown
from bs4 import BeautifulSoap
```
Import moduel for fake useragent
```markdown
from fake_useragent import UserAgent
```
Define UserAgent
```markdown
ua = UserAgent()
```
Create random useragent
```markdown
ua.random
```
Read url as page
```markdown
page = requests.get("https://www.ariva.de/dax-30")
```
Read page with html.parser
```markdown
soup = BeautifulSoup (page.content,"html.parser")
```
Read specific invidual id
```markdown
table  = soup.find(id="result_table_0")
```
Read specific class
```markdown
name_box = soup.find("h1", attrs={"class": "99a4824b"})
```
Read all table data cells
```markdown
table.find_all("td"):
```
Read all table rows for specific class
```markdown
soup.find_all("tr", class_="arrow0"):
```
Read all table data cells with id and content
```markdown
for col_id, col_content in enumerate(result.find_all("td")):
```
Read all divs with specific class
```markdown
entries = results.find_all("div", class_="col-xs-6")
```
Find div with id "lj_div"
```markdown
soup.find("div", {"id": "lj_div"})
```
Find (first) p with class "line"
```markdown
soup.find("p", {"class": line}
```
Check if class has specific content
```markdown
if row.get("class") == ["ellipsis", "nobr", "new"]:
```
Read all links from href element
```markdown
for e in soup.find_all("a"): e.get("href"))
```
Read all number from the field "value"
```markdown
for e in soup.find_all("a"): e.get("value"))
```
Outputs text without whitespaces
```markdown
content.text.strip()
```
Read url from the image
```markdown
url_i = rows[0].find('img')['src']
```
Read image as content
```markdown
image = requests.get(f'https:{url_i}').content
```
Formated Output with html indentations
```markdown
results.prettify()
```
Check if specific text in soup text-output
```markdown
if "Kein Zugriff" in soup.text:
```

<br>Read with Selenium when necessary due the specific homepage
```markdown
from bs4 import BeautifulSoup
from selenium import webdriver
link = "https://www.gurufocus.com/stock/" + stock + "/summary"			# define the homepage to be scraped
options = Options()
options.add_argument('--headless')										# webpage will work in the back
options.add_experimental_option ('excludeSwitches', ['enable-logging'])
path = os.path.abspath (os.path.dirname (sys.argv[0]))					# works for alle platforms (Win,MacOs,Linux)
if platform == "win32":
	cd = '/chromedriver.exe'
elif platform == "linux":
	cd = '/chromedriver_linux'
elif platform == "darwin":
	cd = '/chromedriver'
driver = webdriver.Chrome (path + cd, options=options)					# Use chromedriver.exe to read website with the above options
driver.get (link)  														# Read link
time.sleep (2)  														# Wait till the full site is loaded
```

<br>Wait for the specific element to load
```markdown
element = driver.find_element_by_id("analyst-estimate")
driver.execute_script("arguments[0].scrollIntoView();", element)
time.sleep (1)
```
<br>Read page with html.parser and to the further scraping
```markdown
soup = BeautifulSoup(driver.page_source, 'html.parser')
```
Close the chromedriver window
```markdown
driver.quit ()
```

<br>all searches also possible for more elements wiht find_elements_*
```markdown
driver.find_element_by id												# Search for a id in html
driver.find_element_by_name												# Search for name-field (eg. in input-tag)
driver.find_element_by_xpath											# Search by xpath of the element (right mouse blick in Chrome Dev Tools)
driver.find_element_by_link_text										# Search for (full) text within the tags
driver.find_element_by_partial_link_text								# Search for (part) text within the tags
driver.find_element_by_tag_name('h1')									# Search for a tag in html
driver.find_element_by_class_name("cont")								# Search for a specific class name in html
driver.find_element_by_css_selector('p.content')						# Search for tag and selector
```



---
## MODULE - REQUESTS - workings with APIs
[jump to top...](#python)<br><br>
<br>import module requests
```markdown
import requests
```
import module json
```markdown
import json
```
Request api from the generated api-link
```markdown
api_request = requests.get ("apilink.html")
```
Read/parse api-data to a json-loadfil
```markdown
api = json.loads(api_request.content)
```
Read the value for the 1 element and the attribute xyz
```markdown
result = api[0]["xyz"]
```



---
## MODULE - PYQT - making GUIs
[jump to top...](#python)<br><br>
<br>Installation
```markdown
pip install pyqt5
```
Defines Application
```markdown
from PyQt5.QtWidgets import QApplication
```
Defines Label
```markdown
from PyQt5.QtWidgets import QLabel
```
Defines Widget
```markdown
from PyQt5.QtWidgets import QWidget
```
Arranges horizontally from left to right
```markdown
from PyQt5.QtWidgets import QHBoxLayout
```
Arranges vertically from top to bottom
```markdown
from PyQt5.QtWidgets import QVBoxLayout
```
Arranges in grid from on x and y axes
```markdown
from PyQt5.QtWidgets import QGridLayout
```
Field for forms - 1col are titles, 2col are fields,rbs,cb
```markdown
from PyQt5.QtWidgets import QFormLayout
```
Defines PushButton
```markdown
from PyQt5.QtWidgets import QPushButton
```
Module for dialog windows
```markdown
from PyQt5.QtWidgets import QDialog
```
Module for button boxes in dialog windows
```markdown
from PyQt5.QtWidgets import QDialogButtonBox
```
Defines input field with text
```markdown
from PyQt5.QtWidgets import QLineEdit
```
Module for main windows
```markdown
from PyQt5.QtWidgets import QMainWindow
```
Module for status bar
```markdown
from PyQt5.QtWidgets import QStatusBar
```
Module for tool bar
```markdown
from PyQt5.QtWidgets import QToolBar
```
Create an instance of the application
```markdown
app = QApplication(sys.argv)
```
Initialize a window
```markdown
w = QWidget()
```
Title of the windows
```markdown
w.setWindowTitle('Windows Title')
```
Define windows (1:x-coord,2:y-coord,3:width,4:height)
```markdown
w.setGeometry(200, 200, 380, 180)
```
Place / move windows to coodinates 60,15
```markdown
w.move(50, 15)
```
Define label / message in format h1
```markdown
msg = QLabel('<h1>Hello World!</h1>', parent=window)
```
Place / move labe to coordinates 60,15
```markdown
msg.move(50, 15)
```
Show the application GUI - schedules a paint event
```markdown
windows.show()
```
Start the app and close it with sys.exit
```markdown
sys.exit(app.exce_())
```
Defines horzontal box
```markdown
layout_qh = QHBoxLayout()
```
Defines vertical box
```markdown
layout_qv = QVBoxLayout()
```
Defines grid layout
```markdown
layout_qg = QGridLayout()
```
Defines form layout
```markdown
layout_qf = QFormLayout()
```
Defines one or more buttons
```markdown
layout_qh.addWidget(QPushButton('Button1'))
```
Defines one or more buttons
```markdown
layout_qv.addWidget(QPushButton('Button1'))
```
Defines one or more buttons and set it to position 1,0
```markdown
layout_qg.addWidget(QPushButton('Button1'),1,0)
```
Set buttons to position 2,1 and span it 1row/2cols
```markdown
layout_qg.addWidget(QPushButton('Button1'),2,1,1,2)
```
Defines input field
```markdown
layout_qf.addRow("text:", QLineEdit())
```
Sets layout dimensions to window
```markdown
w.setLayout(layout_xy)
```
Defines a class dialog which inherits from QDialog
```markdown
class Dialog(QDialog):
```
Define buttons for a dialog window
```markdown
buttons = QDialogButtonBox()
```
Defines a ok button on a dialog window
```markdown
buttons.setStandardButtons(QDialogButtons.OK)
```
Adds buttons to vertical layout
```markdown
layout_qv.addWidget(buttons)
```
Defines a class Windows which inherits from QMainWindow
```markdown
class Window(QMainWindow):
```



---
## MODULE - TKinter - making GUIs
[jump to top...](#python)<br><br>
<br>Tutorial with deep explanation
```markdown
https://www.youtube.com/watch?v=YXPyB4XeYLA
```
Import tkinter module
```markdown
from tkinter import *
```
Create root window
```markdown
root = Tk()
```
Name of the window in the title
```markdown
root.title("Header Title")
```
Define icon for the windows (left upper corner)
```markdown
root.iconbitmap("pic.ico")
```
Define size of the window
```markdown
root.geometry("400x400")
```
Creating a label widget
```markdown
myLabel = Label(root,text="Hello World!")
```
Showing myLabel on the screen
```markdown
myLabel.pack()
```
Showing myLabel on grid place 0/0 (left upper corner) with 10pixel padding from above
```markdown
myLabel.grid(row=0,column=0,pady=10)
```
Creating a status label widget with border (bd=1), sunken relief and anchor position right (east)
```markdown
status = Label(root,text="St",bd=1,relief=SUNKEN,anchor=E
```
Showing status bar - with using maximum space from left to right (west to east) with sticky
```markdown
status.grid(row=2,column=0,columnspan=3,sticky=W+E)
```
Creating a button widget with a name
```markdown
myButton = Button(root,text="Click Me!")
```
Creating a deactivated, greyed button widget with a name
```markdown
myButton = Button(root,text="Click Me!",state=DISABLED)
```
Creating a button widget with a name and size 50 * 50
```markdown
myButton = Button(root,text="C",padx=50,pady=50)
```
Creating a button which will excute the myfunc-function when its clicked
```markdown
myButton = Button(root,text="T",command=myfunc)
```
Creating a button which will excute the func-function with a numeric parameter
```markdown
myButton = Button(root,text="T",command=lambda: func(nr))
```
Creating a button with background blue and foreground white
```markdown
myButton = Button(root,text="col",bg="blue",fg="white")
```
Create a quit-button on the window
```markdown
QuitButton = Button(root,text="exit",command=root.quit)
```
Creating a entry field - with width 50 and borderwidth 5 - and showing the field
```markdown
myEntry = Entry(root, width=50, borderwidth=5).pack()
```
Showing myEntry as grid in row/col = 0/0 and spanned over 3 columns
```markdown
myEntry.grid(row=0,column=0,columnspan=3)
```
Showing myEntry as grid in row/col = 0/0 and with pading in x/y-axes
```markdown
e.grid(row=0,column=0,padx=10,pady=10)
```
Read content of the entry field
```markdown
myEntry.get()
```
Shows a default value in the entry field
```markdown
myEntry.insert(0,"Default-Text")
```
Insert a number into the entry field
```markdown
myEntry.insert(0, number)
```
Delete content of the entry field
```markdown
myEntry.delete(0,END)
```
Mainloop of the program
```markdown
root.mainloop()
```
Close window "wind"
```markdown
...command=wind.destroy
```

<br>Pics in Tkinter-Windows
```markdown
from PIL import ImageTk,Image								# Additional module Pillow neede (install with <pip install Pillow>
my_img = ImageTk.PhotoImage(Image.open("demo.png"))			# Reads Image wiht Pillow-module (Tkinter can not read png/jpg files)
my_label = Label(image=my_img)								# Creating a Label with the image
my_label.pack()												# Showing the pic
```

<br>Define Frame
```markdown
frame = LabelFrame(root,text="Name_Frame",padx=5,padx=5)	# Creating a frame with padding 5/5 (inside the frame)
frame.pack(padx=10,pady=10)									# Showing the frame with padding 10/10 (outside the frame)
button = Button(frame,text="Name_Button")					# Creating button in the frame (not root window)
button.grid(row=0, column=0)								# Showing the button in the frame as grid (with frames is mixing between pack and grid possible)
```

<br>RadioButtons
```markdown
r = IntVar()												# Define variable for radio button - when string use StringVar()
r.set("2")													# Choose default radio button
Radiobutton(root,text="Opt1",variable=r,value=1).pack()		# Define and show radiobutton 1
Radiobutton(root,text="Opt2",variable=r,value=2).pack()		# Define and show radiobutton 2
r.get()														# Get value from choosen radio button
```

<br>MessageBox
```markdown
messagebox.showinfo("Title of PopUp", "Hello World!")		# Show Messagebox
different boxes available: showinfo, showwarning, showerror, askquestion, askokcancel, askyesno
response = messagebox.askquestion ("Bla", "BlaBla!")		# Show AskQuestion Box and store response
```

<br>Check about response of user in message box
```markdown
if response == 1: Label(root, text= "YES").pack()
elif response == 0: Label(root, text= "NO").pack()
```

<br>More Windows
```markdown
def open()													# Function for opening the 2nd window
	global my_img											# Global definition necessary - otherwise no pic would be drawn
	sec = TopLevel()										# Define 2nd window
	sec.title("2nd Window")									# Title for 2nd window
    img = ImageTk.PhotoImage(Image.open("demo.png"))		# Define image
    Label (top, image=img).pack()							# Show image in 2nd window
btn=Button(root,text="Open 2nd Window",command=open).pack()	# Button for opening 2nd window per click
```

<br>FileDialog
```markdown
root.filename = filedialog.askopenfilename(					# Define filname dialog
    initialdir="/Users/Bla/images",							# Define initial dir for the file dialog
    title="Select file",									# Title of the file dialog
    filetypes=(("png files","*.png"),("all files","*.*")))	# Define filetypes in dialog (first name, second which files, default first entry)
my_label = Label(root, text=root.filename).pack()			# After choosing a file - show the filename + filepath
```

<br>Slider
```markdown
vertical = Scale(root,from_=0,to=200)						# Define vertical slider
vertical.pack()												# Showing vertical slider
horizontal = Scale(root,from_=0,to=200,orient=HORIZONTAL)	# Define horizontal slider
horizontal.pack()											# Showing horizontal slider
```

<br>Checkboxes
```markdown
Checkbutton(root,text="Check1",variable=var).pack(			# Define and Show a checkbox
c.select() or c.deselect()									# Select or Deselect per default the checkbox
```

<br>DropDown
```markdown
options=["Mo","Tu","We","Th","Fr"]							# Define options for dropdown menue
var = StringVar()											# Define variable for dropdown menue
var.set("Mo")												# Set default for dropdown menue
OptionMenu(root,var,*options).pack							# Define dropdown menue
```



---
## MODULE - PYGAME - making games
[jump to top...](#python)<br><br>
<br>Pygame documentation
```markdown
http://pygame.org/docs/
```
Import of the pygame module
```markdown
import pygame as pg
```
Initialize and setup screen
```markdown
pg.init()
```
Define dimension
```markdown
screen_dim = (1200,800)
```
Show screen with the defined dimensions
```markdown
screen = pg.display.set_mode(screen_dim)
```
Define background color
```markdown
bg_color = (230,230,230)
```
Screen filling with defined background color
```markdown
screen.fill(bg_color)
```
Title of the game in the window
```markdown
pg.display.set_caption("My Super Game")
```
Rectangle infos (left,top,width,height - (0,0,1200,800)
```markdown
rect screen.get_rect()
```
Center of the Rectangle as tuple - (600,400)
```markdown
rect.center
```
Size of the Rectangle as tuple - (1200,800)
```markdown
rect-size
```
X-Dim left - (0)
```markdown
rect.left
```
X-Dim right - (1200)
```markdown
rect.right
```
Y-Dim top - (0)
```markdown
rect.top
```
Y-Dim bottom - (800)
```markdown
rect.bottom
```
Middle of X-Dim - (600)
```markdown
rect.centerx
```
Middle of Y-Dim - (400)
```markdown
rect.centery
```
Width of the rectangle - (1200)
```markdown
rect.width
```
Height of the rectangle - (800)
```markdown
rect.height
```
Define new rectangle
```markdown
small_rect = pg.Rect(100,100,10,150)
```
Draw small rectangle in screen
```markdown
pg.draw.rect(screen,(100,100,100,small_rect)
```
Loading an image
```markdown
figure = pg.image.load("ship.png")
```
Getting the rect object from an image
```markdown
figure.get_rect()
```
Positioning an image in the middle of the bottom screen
```markdown
figure_rect.midbottom = screen_rect.midbottom
```
Drawing an image to the screen
```markdown
screen.blit(figure, figure_rect)
```
Check if an event has happend (keystroke, mouseclick)
```markdown
for event in pg.event.get():
```
Check if key is pressed
```markdown
event.type == pg.KEYDOWN:
```
Some action when Right-Key is pressed
```markdown
event.key == pg.K_RIGHT:
```
Some action when Space-Key is pressed
```markdown
event.key == pg.K_SPACE:
```
Check if mousebutton is clicked
```markdown
event.type == pg.MOUSEBUTTONDOWN
```
Findinig the mouse position
```markdown
mouse_pos = pg.mouse.get_pos()
```
Check if mouse-cursor is ofer an object / rectangle
```markdown
button_rect.collidepoint(mouse_pos)
```

Pygame groups<br>
Group class for working with similar objects
```markdown
from pygame.sprite import Sprite,Group
```
Making and filling a group - must inherit from Sprite
```markdown
def Bullet(Sprite):
```
Method from the new group
```markdown
def draw_bullet(self):
```
Method from the new group
```markdown
def update(self):
```
Define group of elements
```markdown
bullet = Group()
```
Define new instance
```markdown
new_bullet = Bullet()
```
Add new instance to group
```markdown
bullets.add(new_bullet)
```
Iterate through group instances and draw
```markdown
from bullet in bullets.sprites(): bullet.draw_bullet()
```
Calls the methode update() on each member of the group
```markdown
bullets.update()
```
Remove instance from group
```markdown
bullets.remove(bullet)
```
Check if single object is overlapping with groupelements
```markdown
prg.sprite.spritecollideany(obj,group)
```
Result-Dict with all overlapping elements of both groups
```markdown
pg.sprite.groupcollide(group1,group2,True,True)
```
Define message
```markdown
msg = "Play again!"
```
Defines message color
```markdown
msg_col = (100,100,100)
```
Defines background color
```markdown
bg_col = (230,230,230)
```
Defines font from system font
```markdown
font = pg.font.SysFont(None,48)
```
Create an image of the message
```markdown
msg_img = f.render(msg,True,msg_col,bg_col)
```
Read rect from message-image
```markdown
msg_img_rect = msg_image.get_rect()
```
Pos the message-image in the middle of the window
```markdown
msg_img_rect.center = screen_rect.center
```
Display the positioned message-image
```markdown
screen.blit(msg_img, msg_img_rect)
```



---
## MODULE - PYTHONCOM - make new formula in excel with python-function
[jump to top...](#python)<br><br>
https://www.youtube.com/watch?v=cYwn8Pu5eRg&feature=emb_logo<br>
Import necessary modules
```markdown
import pythoncom
```
Import client
```markdown
import win32com.client
```
Import server
```markdown
import win32com.server.register
```
Put everything in a class
```markdown
class PythonObjectLibrary:
```
UniqueID for our object to register it with Windows
```markdown
_reg_clsid_ = pythoncom.CreateGuid()
```
Register the object as an EXE
```markdown
_reg_clsctx = pythoncom.CLSCTX_LOCAL_SERVER
```
Register the object as a DLL
```markdown
_reg_clsctx = pythoncom.IMPROC_SERVER
```
Name of the project library
```markdown
_reg_progid_ = "Python.ObjectLibrary"
```
Optional / Description of the library
```markdown
_reg_desc_ = "This is our Python Obj Library"
```
Name the functions - this sees the user in excel
```markdown
_public_methods_ = ["f1","f2,"f3"]
```
Define the function in the class
```markdown
def f1(self, x, y):
```
Return the result of the function (to excel later)
```markdown
return x + y
```
Another function - this time wie a range (more cells in excel)
```markdown
def f2(self, myRange):
```
Create an instance of the range object passed trough
```markdown
rng1 = win32com.client.Dispatch(myRange)
```
Change the object to an numpy-array (or an list)
```markdown
rng1val = np.array(list(rng1.Value))
```
Return the sum of the range (to excel later)
```markdown
return rng1val.sum()
```
Part of the code in the main-section
```markdown
if __name__ == "__main__":
```
Register the library (when the program is started => the Library is registered in Windows)
```markdown
win32com.server.register.UseCommandLine(PythonObjectLibrary)
```

<br>Part in Excel
```markdown
(in the Visual Basic Editor under Development Tools)
# Definition of the f1-function - now the user can use the function "f1" in excel
Function f1(x As Long, y As Long)
    f1 = VBA.CreateObject("Python.ObjectLibrary").f1(x, y)
End Function
# Definition of the f2-function - now the user can use the function "f2" in excel
Function f2(x As Range)
    f2 = VBA.CreateObject("Python.ObjectLibrary").f2(x)
End Function
```



---
## MODULE - FLASK, ZAPPA, AWS - making an API
[jump to top...](#python)<br><br>
<br>create basic api in flask
```markdown
https://nordicapis.com/how-to-create-an-api-from-a-dataset-using-python-and-flask/
```
create basic api in flask, deploy to AWS with zappa and setup on Rapidapi
```markdown
https://pythonforundergradengineers.com/deploy-serverless-web-app-aws-lambda-zappa.html#what-is-zappa
```
create basic api in flask, deploy to AWS with zappa and
```markdown
https://towardsdatascience.com/develop-and-sell-a-python-api-from-start-to-end-tutorial-9a038e433966
```

<br>Import the module
```markdown
import flask
```
Creates a Flask application
```markdown
app = flask.Flask(__name__)
```
Runs the program in debug mode (no reset necessary when changing a line of code)
```markdown
app.config["DEBUG"] = True
```
"/" indicates where the result in the url will output - GET will read data (POST for writing data)
```markdown
@app.route('/', methods=['GET'])
```
Runs the application
```markdown
app.run()
```

<br>Outputs a List with a dict to the server / url
```markdown
@app.route('/api/v1/resources/books/all', methods=['GET'])	# Data will available at: http://127.0.0.1:5000/api/v1/resources/books/all
def api_all():
    return jsonify(books)	    # Converts and returns the list in JSON-Flask-format
app.run()
# results are available under http://127.0.0.1:5000/api/v1/resources/books/all
```

<br>Filtering data
```markdown
@app.route('/api/v1/resources/books', methods=['GET'])
def api_id():
    if 'id' in request.args:					# Check if an ID was provided as part of the URL
        id = int(request.args['id'])			# If ID is provided, assign it to a variable
    else: return "Error: No id field provided"	# If no ID is provided, display an error in the browser.
    for book in books:							# Loop through the data and match results that fit the requested ID
        if book['id'] == id: results.append(book)
    return jsonify(results)						# Use the jsonify function from Flask to convert our list of - Python dictionaries to the JSON format
app.run()
# results are available under http://127.0.0.1:5000/api/v1/resources/books?id=1
```

<br>Check if API is called from the right access-place (like rapidapi.com)
```markdown
(key is provided from the platform - eg. here from rapidapi.com)
    if "e6e45ed0-55e5-11eb-963e-ffe9fcdce080" not in request.headers:
        return "Error: Wrong API-Call - use www.rapidapi.com for calling the API!"
```

<br>Using zappa and deploying to AWS (zappa is only working in a virtual environment)
```markdown
pip install zappa											=> Install module
=> Create file and insert the credentials from AWS (creation see second link above)
create file credentials in "%UserProfile%\.aws
	[default]
	aws_access_key_id = XXXXXXXXXXXXXXXXXXXXXXXXXX
	aws_secret_access_key = XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
virtualenv xyz									# Create an virtual environment
xyz\Scripts\activate							# Activate virtual environment
go back to folder xyz and install all necessary modules with pip install
pip list										# Check if everything is installed in the folder
zappa init (when virutal environement is activated!)		# Create zappa_settings.json File (press return at any prompt)
    "dev": {
		"app_function": "app.app",				# Name of the py-file
		"aws_region": "eu-central-1",			# Nearest aws-region
        "profile_name": "default",				# Same as in aws-credentials at "%UserProfile%/.aws/credentials
        "project_name": "apicheck",
        "runtime": "python3.7",					# Automatic generated
        "s3_bucket": "zappa-gsoln7zyl"			# Automatic generated
    }
pip freeze > requirements.txt					# Create requirements.txt for all installed modules in the virtual environment
zappa deploy dev (when virutal environement is activated!)	# Deploy everything to AWS (when ended with link everything worked fine) (otherwise 502 error - often a module is missing)
	eg. https://xnujiyxsb1.execute-api.eu-central-1.amazonaws.com/dev/api/v1/incstat?ticker=FB
		https://xnujiyxsb1.execute-api.eu-central-1.amazonaws.com/dev/api/v1/summary?ticker=CAT
		https://xnujiyxsb1.execute-api.eu-central-1.amazonaws.com/dev/api/v1/profile?ticker=FB
zappa update dev (when virutal environement is activated!)	# Update deployment on AWS (when something changed in the pyhton-program)
zappa undeploy dev								# Undeploy everything on AWS
zappa status									# Show actual status
zappa tail										# Show actual loggin (in error cases)
```

<br>AWS part
```markdown
see the APIs under AWS Api Geteway => region on the upper right site has to be the same as in the zappa_settings.json file#
check API-access
	select API (under API Gateway and APIs)
	click on second ANY link
	click Test (on the left side)
	select Method Get
	input path example under {proxy} eg. api/v1/incstat?ticker=FB
	click Test Button (at the bottom)
```



---
## MODULE - ICECREAM - print for debugging
[jump to top...](#python)<br><br>
<br>Imort icecream
```markdown
from icecream import ic
```
Show value of the variable in the form: ic| var1: 20
```markdown
ic(var1)
```
Show when command is reached: ic| icecream_example.py:5 in func() at 01:44:20.394 (line / file / time)
```markdown
ic()
```
Set Context Output => also shows line / file / time
```markdown
ic.configureOutput(includeContext=True)
```



---
## PYINSTALLER - generate python programs to executables
[jump to top...](#python)<br><br>
<br>Installation
```markdown
pip install pyinstaller
```
Generate the bundle in a subdirectory called dist.
```markdown
pyinstaller prg.py
```
Generate only one file
```markdown
pyinstaller --onefile prg.py
```
Generate file with icon
```markdown
--icon=app.ico
```
Generating under mac os sometimes only work with this params
```markdown
--hidden-import=pkg_resources.py2_warn
```
Generating under mac os sometimes only work with this params
```markdown
--hidden-import=pkg_resources.py2_warn
```
When some modules are making problems - sometimes this helps
```markdown
--hidden-import=pymssql
```
when there is a depreciating warning from matlib
```markdown
--exclude-module matplotlib
```
Open this file to start the python-program
```markdown
prg.exe
```

<br>Problems with some added python modules (eg. pycountry)
```markdown
https://groups.google.com/g/pyinstaller/c/OYhJdeZ9010/m/32g3-T8XBAAJ
Create hook-file hook-pycountry.py with content:
	from PyInstaller.utils.hooks import copy_metadata, collect_data_files
	datas = copy_metadata("pycountry") + collect_data_files("pycountry")
Compile Program with
	pyinstaller --onefile --exclude-module matplotlib --additional-hooks-dir=. TestPyCountry.py
```

<br>Problems with path when executing from py and exe
```markdown
config_name = 'creds.json'                                    # Define the config file name
```

<br>determine if application is a script file or frozen exe
```markdown
if getattr(sys, 'frozen', False):                             # Get path when starting as executable
    application_path = os.path.dirname(sys.executable)
elif __file__:                                                # Get path when running from IDE as py-file
    application_path = os.path.dirname(__file__)
config_path = os.path.join(application_path, config_name)     # Final Config Path
```
