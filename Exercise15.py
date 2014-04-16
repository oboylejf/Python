#imports argument variable from system
from sys import argv
#reports back the filename is whatever the arg variable is
script, filename = argv
#open the .txt file
txt = open(filename)

print "Here's your file %r:" % filename
print txt.read()

print "Type the filename again:"
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()