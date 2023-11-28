# with built-in functions for secrets module, we can generate sequence of randam chars.
import secrets
# string module provides string constants, that we can use for password generation.
import string

alphabets = string.ascii_letters
numbers = string.digits
specialchars = string.punctuation

secertText = alphabets + numbers + specialchars

passwordLen = 10

secertPassword = ''
for count in range(passwordLen):
    secertPassword += ''.join(secrets.choice(secertText))

print("Your secret password is :  " +secertPassword)

# To make password more secure, we can add some constraints to it. Like min 2 special chars and 2 numbers e.t.c.,
while True:
    secertPassword = ''
    for count in range(passwordLen):
        secertPassword += ''.join(secrets.choice(secertText))

    if(sum(c in specialchars for c in secertPassword) >= 2 and
       sum(c in numbers for c in secertPassword) >= 2):
        break

print("The secret password which is more secure:   "  +secertPassword)
