#!/usr/bin/python3
import string


def ispalindrome(x):
    for i in x:
        if string.punctuation.find(i) != -1 or i == " ":
            x = x.replace(i, "")
    x = x.lower()
    if x == x[::-1]:
        return True
    else:
        return False


str = input(":")
print(ispalindrome(str))
