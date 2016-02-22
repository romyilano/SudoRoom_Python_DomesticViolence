
# Analyzing Domestic Violence Data Sets with Python

# Overview
This is a basic tutorial on python using the command line.
Held at [SudoRoom](https://sudoroom.org) late afternoons / Spring 2016. 

![SudoRoom Late Afternoons](graphics/Workshops.png)

## Level

Python newbie teaching other python newbies. 

Note: I am _not_ a teacher! This is an independent workshop, _not_ a class and _not_ a bootcamp.  =D I'm a creator just like you. 

This is very self-guided, dependent on you taking initiative, from the perspective of people who eventually want to learn in order to build things. The focus is on you learning how to ask the right questions.

## Benefits

* You will get more comfortable using the command line, which opens many opportunities to learn other useful things in coding
* You can make a basic "networked" app
* You can avoid doing clerical gruntwork and using horrible Excel Macros

This was originally created for Women Who Code East Bay but this session is open to all genders! Trans, male, female... 

_Women dominate clerical, lower-paid clerical jobs like entry level accounting and secretarial work or lower-level marketing positions. They live their lives in Excel sheets. Enabling them to learn basic coding and taking advantage of their intelligence and potential will help make the world a better place._

# Important Links

* [OpenData Oakland - CrimeWatch Map in the past 90 days](https://data.oaklandnet.com/Public-Safety/CrimeWatch-Maps-Past-90-Days/ym6k-rx7a)
* [Learn Python the Hard Way](http://learnpythonthehardway.org/book/) _we'll be using learn the hard way as a reference point. In my experience his teaching style is what works best for self-driven people out to build stuff_
* [Learn Command line the hard way](http://cli.learncodethehardway.org/book/)
* [Team Treehouse @ SF Public Library](https://teamtreehouse.com/gateways/san_francisco_public_library/signup) San Francisco Public Library card users have free access to the Team Treehouse Python lessons

# Sessions

## Step 1 - Setup

* Get set up on your computer - Railsbridge is excellent, great people, great installation advice (Railsbridge Installation Guide)[http://docs.railsbridge.org/installfest/choose_your_operating_system]
* Be comfortable with the command line - [Learn Command line the hard way](http://cli.learncodethehardway.org/book/) _IMHO the more comfortable you get with the command line the better off you'll be in the short and long run_
* Understand how to use git 
* Complete [Learn Python the Hard Way](http://learnpythonthehardway.org/book/) up until [Lesson 20](http://learnpythonthehardway.org/book/ex20.html) - 


write your first script in the python folder:

```
from sys import argv 
script, filename = argv

in_file = open(filename)
indata = in_file.read()

print("Here's your file %r:" % filename)

print("The sample csv is %d bytes long" % len(indata))
input(" Return to continue >")

print("Now I'm going to print out all the data - it's very long!")
input(" Return to continue >")
print(indata)
input(" Return to continue >")

print("Closing the file")
in_file.close()
```

Run the script, we'll be using the sample.csv which is the spreadsheet of crimes in the Oakland area in the past 90 days

```
python python/session1_intro.py csv/sample.csv
```

### Self-directed Learning Steps

* Make 2 or 3 variations of this script
* Redo the Learn to Code the hard way lessons
* Download other csv files and read them

## Step 2 - CSV
	
* Open up the sample.csv file inside the csv folder - this is a spreadsheet of crimes in the Oakland area in the past 90 days  (downloaded from [OpenData Oakland - CrimeWatch Map in the past 90 days](https://data.oaklandnet.com/Public-Safety/CrimeWatch-Maps-Past-90-Days/ym6k-rx7a))
* We'll work together to use the python csv module to filter out which area had domestic violence
* We'll create a command line script so you can make simple copies and get user input

## Step 3 - CSV Analysis
* Creation of python script with command line input to analyze data in csv

## Step 4 - Python + JSON
## Step 5 - Web Interface

	
## Public Data for Oakland

For tutorials and students we can practice on the Oakland Open Data sets. [https://data.oaklandnet.com](https://data.oaklandnet.com)

* Teach people how to find the sample JSON Endpoint
* Teach people how to get a secret token, etc and add it to their project
* Help people put this in a web console interview




