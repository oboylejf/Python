tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."
#multiple ways to use new line in 9
fat_cat = '''
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
'''

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat


print "\"%s \"yes I am" % backslash_cat
print "\"%r \" \nyes I am" % backslash_cat

while True:
    for i in ["/","-","|","\\","|"]:
        print "%s" % i,