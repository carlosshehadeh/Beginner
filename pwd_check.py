"""Name : Carlos shehadeh
   id : 201901601
   instructor :
   Section : cmps 200 lab section b2"""

#program that takes in a string from the commad line and returns wether it is a good password or not depending on the conditions stated in the question.

""" divided the program into multiple sub divisions, working one each condition alone with a function for each one and then returning the conditions,
to put them in a bigger function to check them all at once using boolean statement"""
import sys

password = str(sys.argv[1])

#for the lenght condition
def lenght(password) :
    for i in range (len(password)) :
        if (len( password )) >= 8 :
            return True
        else :
            return False

#print (lenght(password))
#now for the 0-9 digit condition.

digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]

def pwd_digit(password) :
    for i in range(len(password)) :
        if password[i] in digits :
            return True
    return False


#print (pwd_digit(password))

#for the lowercase condition
def lowercase(password) :
    for i in range(len(password)) :
        if password[i].islower() :
            return True
    return False

#print (lowercase(password))

#for the uppercase condition

def uppercase(password) :
    for i in range (len(password)) :
        if password[i].isupper() :
            return True
    return False

#print (uppercase(password))

#for the non-alphanummeric character condition

notalpha = [ "#", "@", "-", ".", "$", "*", "(", ")", "+", ";", "~", ":", "'", "/", "%", "_", "?","=", ",","&", "!"]

def nonalpha(password) :
    for i in range(len(password)) :
        if password[i] in notalpha :
            return True
    return False

#print (nonalpha(password))

#now for the function that combines all of them
def goodpass(password) :
    if lenght(password) and pwd_digit(password) and lowercase(password) and uppercase(password) and nonalpha(password) == True :
        print ("Good")
    else :
        print ("Not Good")
goodpass(password)
