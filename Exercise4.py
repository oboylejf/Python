#define cars
cars = 100
#define space in a car
space_in_a_car = 4
#define drivers
drivers = 30
#define passangers
passengers = 90
#define cars not driven
cars_not_driven = cars - drivers
#define cars driven
cars_driven = drivers
#define carpool capactity
carpool_capacity = cars_driven * space_in_a_car
#define avg passangers per car
average_passengers_per_car = passengers / cars_driven


print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."
print "hey %s there" % "you"