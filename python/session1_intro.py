# session 1 intro
# copying lots of the nice stuff on learn Python the hard way
# http://learnpythonthehardway.org/book/ex17.html
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




