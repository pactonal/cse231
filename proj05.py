#!/usr/bin/python3
'''Put overall header comments here.'''
import string


def open_file():
    '''Insert function DocString here.'''
    opened = 0
    while opened != 1:
        try:
            filename = input("Enter a file name: \n")
            f = open(filename, "r")
            opened = 1
        except IOError:
            print("Error. Please try again.")
            opened = 0
    return f


def print_headers():
    '''Insert function DocString here.'''
    print('{:^49s}'.format("Maximum Population Change by Continent\n"))
    print("{:<26s}{:>9s}{:>10s}".format("Continent", "Years", "Delta"))


def calc_delta(line, col):
    '''Insert function DocString here.'''
    change = 0

    old = line[(17+6*(col - 1)):(22+6*(col - 1))]
    new = line[(17+6*(col)):(22+6*(col))]

    for i in " ":
        old = old.replace(i, "")
        new = new.replace(i, "")

    for i in string.punctuation:
        old = old.replace(i, "")
        new = new.replace(i, "")

    old = int(old)
    new = int(new)
    change = ((new - old) / old)

    return change


def format_display_line(continent, year, delta):
    '''Insert function DocString here.'''
    yearstring = (str(year - 50) + "-" + str(year))

    delta *= 100
    delta = round(delta)

    displayline = "{:<26s}{:>9s}{:>9d}%".format(continent, yearstring, delta)

    return displayline


def main():
    '''Insert function DocString here.'''
    with open_file() as data:
        print_headers()
        next(data)
        next(data)

        maxofall = 0

        for line in data:
            maxdelta = 0
            maxyear = 0

            continent = line[0:15].strip()

            for column in range(6):
                delta = calc_delta(line, column - 1)

                if delta > maxofall:
                    maxcontinent = continent
                    maxofall = delta
                    maxofallyear = (1750 + 50 * (column + 1))
                if delta > maxdelta:
                    maxdelta = delta
                    maxyear = (1750 + 50 * (column + 1))

            print(format_display_line(continent, maxyear, maxdelta))

        print("Maximum of all continents:")
        print(format_display_line(maxcontinent, maxofallyear, maxofall))

        return 0


if __name__ == "__main__":
    main()
