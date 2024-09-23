from random import *

password=input("enter your password:")

AL=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B'
    'C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','_','-','&']

guess=""

while(guess!=password):
    guess=""
    for i in range(0,len(password)):
        gussed_password=AL[randint(0,53)]
        guess= str(gussed_password) + str(guess)
        print(guess)

print("password cracked !",guess)