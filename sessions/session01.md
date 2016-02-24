
# [Analyzing Domestic Violence Data Sets with Python](../README.md)


# Session 1 - Intro
 Session 1 - Preparations

* Get set up on your computer - Railsbridge is excellent, great people, great installation advice (Railsbridge Installation Guide)[http://docs.railsbridge.org/installfest/choose_your_operating_system]
* Be comfortable with the command line - [Learn Command line the hard way](http://cli.learncodethehardway.org/book/) _IMHO the more comfortable you get with the command line the better off you'll be in the short and long run_
* Understand how to use git 
* Complete [Learn Python the Hard Way](http://learnpythonthehardway.org/book/) up until [Lesson 20](http://learnpythonthehardway.org/book/ex20.html) - 

### Session 1 - the Doing part

Open up the terminal on your computer.

* _Don't know the terminal and command line? [Go here](http://cli.learncodethehardway.org/book/)_

```
mkdir SudoLesson
cd SudoLesson
```

Now use git to clone the [github repo](https://github.com/romyilano/SudoRoom_Python_DomesticViolence) for this workshop 

```
git clone https://github.com/romyilano/SudoRoom_Python_DomesticViolence
```

* _Don't know how to use git from the command line?_ review cloning and the basics [the simple guide](http://rogerdudler.github.io/git-guide/)

```
cd SudoRoom_Python_DomesticViolence
```

write your first script in the python folder, name it ```intro_python.py```

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
python python/intro_python.py csv/sample.csv
```

### Self-directed Learning Steps

* Make 2 or 3 variations of this script
* Redo the Learn to Code the hard way lessons
* Download other csv files and read them