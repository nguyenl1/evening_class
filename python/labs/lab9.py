# # # Version 1 

# conv = float(input ("Enter your measurement in feet "))

# meters = 0.3048

# output = (conv * meters)

# two = ("%.2f" % output) # %f treats value as a decimal, .2 two digits 

# print (f"{two} meters! ")

# # Version 2/3

# meters 
# feet = 0.3048
# miles = 1609.34 
# meters = 1 
# kilo = 1000
# yard = 0.9144
# inch = 0.0254 

# units = float(input("Enter your units. "))
# distance = input("Enter your measurement in feet, miles, meters, kilo, yard, or inch. ")

# if distance == "feet":
#     calc = units * feet
#     two = ("%.2f" % calc)
#     print (f"That's {two} meters!")
# elif distance == "miles":
#     calc = units * miles
#     two = ("%.2f" % calc)
#     print (f"That's {two} meters!")
# elif distance == "meters":
#     calc = units * meters
#     two = ("%.2f" % calc)
#     print (f"That's {two} meters!")
# elif distance == "kilo":
#     calc = units * kilo
#     two = ("%.2f" % calc)
#     print (f"That's {two} meters!")
# elif distance == "yard":
#     calc = units * yard
#     two = ("%.2f" % calc)
#     print (f"That's {two} meters!")
# elif distance == "inch":
#     calc = units * inch
#     two = ("%.2f" % calc)
#     print (f"That's {two} meters!")

#Version 4

meters = { 
'feet' : 0.3048, # 1 m is 3.28084 ft 
'miles' : 1609.34, # 1 m is 0.000621371 mi 
'meters' : 1, 
'kilo' : 1000, # 1 m is 0.001 kilo
'yard' : 0.9144, # 1 m is 1.09361 yard
'inch' : 0.0254 # 1 m is 39.3701 inch
} #dictionary

#meter = name of dictionary, .get = returns the value of the key
distance = float(input("Enter your distance. "))
from_units = meters.get(input("Enter your measurement in feet, miles, meters, kilo, yard, or inch. "))
to_units = meters.get(input("Enter your measurement you would like to convert to in feet, miles, meters, kilo, yard, or inch. "))


measure = (distance * from_units) / to_units
print(measure)


# if from_un25 
    79its == 'feet' and to_units == 'miles':
#     con = (distance * feet)/miles
#     print (f"That's {con} miles! ")


justin solution

define up top
define a function that takes in a distance, and a unit and returns the distance converted into the specified unit.

func(dist,unit)
if unit == m 
distance * conversaion_factor for m 
elif unit == filterdistance * conversaion factor for ft
.
.
.
.

define a function that converts the given distance (specified in meters) into the target units

define another function that standardizes the units using meters, 
converts specified units to the target units by way of conversion to meters filterdistance

def main()
    ask for the distance
    convert the distance to a float
    loop, while True
    ask the user for the units to convert fro, 
    ask the user for the units to convert to
    convert the distance to meters 
    use the distance converted to meters to then convert into the target unit
    then they display
    ask if user wants to go again
    if y go again
    if n break 
