# /usr/bin/env python3 

# Ryan Higgins
#Calculate Square root of number

#create function 
def sqrt(x):
    """
    Calculate Sqaure Root for the argument
    """

  #If Statement
  #Check if x is positive
    if x < 0:
     print("Error: Negative Value")
    return -1

  #Initital Guess for Square Root
  #Create Variable for z
    z = x / 2.0

    #Continually Improve the guess
    while abs (x - (z*z)) >  0.00000000000001:
      z = z - (((z * z) - x) / (2 * z))


    return z
#Every line to here is indented means that these are all belong to function.
myval = -63.0
print("The sqaure root of ", myval, "is", sqrt(myval))


