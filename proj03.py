#!/usr/bin/python3
import string


# Input choice
answer = input("Would you like to (D)ecrypt, (E)ncrypt or (Q)uit? ")


# Error check answer
while answer.upper() not in "D,E,Q":

    answer = input("Would you like to (D)ecrypt, (E)ncrypt or (Q)uit? ")


# Main loop
while answer.upper() != 'Q':

    # Encrypt Section
    if answer.upper() == 'E':

        # Initialize encryption strings
        encryptor = string.ascii_lowercase
        alpha = string.ascii_lowercase
        substitute = ""
        affine = ""
        decrypt = ""
        norepeat = ""

        # Input encryption keyword
        keyword = input("Please enter a keyword: ")

        # Error check for length and letters
        while not keyword.isalpha() or len(keyword) > 26:

            print("There is an error in the keyword. It must be all letters an"
                  "d a maximum length of 26")

            keyword = input("Please enter a keyword: ")

        # Remove keyword duplicate letters
        for i in keyword:

            found = False

            for z in norepeat:

                if z == i:

                    found = True
                    break

            if not found:

                norepeat += i.lower()

        # Remove letters from alphabet
        for let in norepeat:
            encryptor = encryptor.replace(let.lower(), "")

        # Add keyword to alphabet - letters
        encryptor = (norepeat.lower() + encryptor.lower())

        # Input message to be encrypted
        code = input("Enter your message: ")

        # Encrypt message with substitution
        for i in code.lower():

            if i.isalpha() is False:
                substitute += i

            else:
                substitute += encryptor[alpha.find(i)]

        # Encrypt message with affine
        for i in substitute:

            if i.isalpha() is False:
                affine += i

            else:
                affine += encryptor[((5 * encryptor.find(i)) + 8) % 26]

        print("your encoded message:  " + affine.lower())

    # Decrypt Section
    if answer.upper() == 'D':

        # Initialize encryption strings
        encryptor = string.ascii_lowercase
        alpha = string.ascii_lowercase
        decrypt = ""
        norepeat = ""

        # Input encryption keyword
        keyword = input("Please enter a keyword: ")

        # Error check for length and letters
        while not keyword.isalpha() or len(keyword) > 26:

            print("There is an error in the keyword. It must be all letters an"
                  "d a maximum length of 26")
            keyword = input("Please enter a keyword: ")

        # Remove keyword duplicate letters
        for i in keyword:

            found = False

            for z in norepeat:

                if z == i:

                    found = True
                    break

            if not found:

                norepeat += i

        # Remove letters from alphabet
        for let in norepeat:
            encryptor = encryptor.replace(let.lower(), "")

        # Add keyword to alphabet - letters
        encryptor = (norepeat + encryptor)

        # Input message to be encrypted
        code = input("Enter your message: ")

        for i in code:
            if i == " ":
                decrypt += " "
            elif i.isalpha() is True:
                decrypt += alpha[(((encryptor.find(i) - 8) * 21) % 26)]
        print("your decoded message:  " + decrypt)

    answer = input("Would you like to (D)ecrypt, (E)ncrypt or (Q)uit? ")

print("See you again soon!")
