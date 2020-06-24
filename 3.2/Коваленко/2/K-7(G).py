import re

def isPrime(numb):
    if numb % 2 == 0:
        return numb == 2
    d = 3
    while d * d <= numb and numb % d != 0:
        d += 2
    return d * d > numb

def isPalindrom(numb):
    return numb == numb[::-1]

def isDegree(numb):
    while(numb != 1):
        if numb % 2 == 1:
            return False
        numb /= 2
    return True

def check_pin(pinCode):
    rezult = re.split(r'-', pinCode)
    if isPrime(int(rezult[0])) and isPalindrom(rezult[1]) and isDegree(int(rezult[2])):
        return True
    return False

print(check_pin('7-101-4'))