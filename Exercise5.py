name = 'James F. OBoyle'
age = 25 # not a lie
height = 74 # inches
weight = 200 # lbs
eyes = 'Green'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "He's %d pounds heavy." % weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (
    age, height, weight, age + height + weight)

#question about %r

pounds = 200
kilos = pounds * 0.45359237
print "%r pounds equals %r kilos." % (pounds, kilos)

inches = 25
centimeters = inches * 2.54
print "%r inches equals %r centimeters." % (inches, centimeters)