#Behold!...... a basic velocity calculator
#v = d/t
import math

answer = str(input("press d for kilometers and e for meters: "))

if answer == 'e':
# d is distance... 
    d = float(input("Enter distance you are going / have gone just numbers as a whole or decimal in KM: "))

# t is time...
    t = float(input("How many minutes did it take you: "))

# v is velocity 
    v = d/t 

    print('Your velocity is ', v, "per minute")
else:

# there is much more to it, this is just extremely basic calculation based on some very traditional physics concepts. 
    print("********** MORE TO BE ADDED **************")
