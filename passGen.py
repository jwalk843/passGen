#!/usr/bin/python3

import string
import base64
from random import *

# function defined
def passGen():
    chars = string.ascii_letters + string.digits
    password = "".join(choice(chars) for x in range((25)))
    print("Password: "+password)
print("Generating random passwords for you now")
for i in range(10):
    passGen()
#    f = open("passwords.txt", "w")
 #   for i in range(25):
  #      f.write(password+"\n")
    #print("Password is: "+password)
