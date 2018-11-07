###############################################################################
# Project 6
#
# CSV file reading
#   Prompt for files to be opened
#   Read data from files and create lists of data
#   Output data to user in a nice format
#   Ask user if they would like to plot the data
#       If yes, create a bar graph of the data
#       If no, end the program
###############################################################################
from operator import itemgetter  # useful for sorting
import pylab   # for plotting


def open_file():
    '''
    Opens user inputted file
    Returns: File pointer
    '''
    opened = 0
    while opened != 1:
        try:
            filename = input("Enter a file name: ")
            f = open(filename, "r")
            opened = 1
        except IOError:
            print("Error. Please try again.")
            opened = 0
    return f


def find_index(header_lst, s):
    '''
    Finds the index of a given string in the header
    header_lst: List of the entries in the header of the file (list)
    s: String to search for (str)
    Returns: index of string in header list (int)
    '''
    try:
        index = header_lst.index(s)
        return index
    except ValueError:
        return None


def read_2016_file(fp):
    '''
    Reads through and collect data from the 2016 file
    fp: File pointer to the 2016 data file
    Returns: Sorted list of tuples of state name and data (list)
    '''
    datalist = []
    header = fp.readline()
    header_lst = header.split(',')

    for line in fp:
        line_lst = line.strip().split(',')
        state = line_lst[2].strip()

        nat_index = find_index(header_lst, "EST_VC197")
        naturalized_index = find_index(header_lst, "EST_VC201")
        non_citizen_index = find_index(header_lst, "EST_VC211")

        non_citizen = str(line_lst[non_citizen_index].strip())
        naturalized = str(line_lst[naturalized_index].strip())
        nat = str(line_lst[nat_index].strip())

        try:
            non_citizen = int(non_citizen)
            naturalized = int(naturalized)
            nat = int(nat)
        except ValueError:
            non_citizen = 0
            naturalized = 1
            nat = 0

        nat_ratio = (naturalized / (nat + naturalized + non_citizen))
        non_ratio = (non_citizen / (nat + naturalized + non_citizen))
        state_tup = (state, nat, naturalized, nat_ratio, non_citizen,
                     non_ratio)

        datalist.append(state_tup)

    datalist.pop(0)
    datalist = sorted(datalist, key=itemgetter(5))
    return datalist


def read_2000_file(fp2):
    '''
    Reads through and collects data from the 2000 file
    fp2: File pointer to the 2000 data file
    Returns: Tuple of total citizens (int), natural born citizens (int),
    naturalized citizens (int), and non citizens (int)
    '''
    header = fp2.readline()
    header_lst = header.split(',')

    for line in fp2:
        line_lst = line.strip().split(',')

        total_index = find_index(header_lst, "HC01_VC02")
        nat_index = find_index(header_lst, "HC01_VC03")
        naturalized_index = find_index(header_lst, "HC01_VC05")
        non_citizen_index = find_index(header_lst, "HC01_VC06")

        total = str(line_lst[total_index].strip())
        non_citizen = str(line_lst[non_citizen_index].strip())
        naturalized = str(line_lst[naturalized_index].strip())
        nat = str(line_lst[nat_index].strip())

        try:
            total = int(total)
            non_citizen = int(non_citizen)
            naturalized = int(naturalized)
            nat = int(nat)
        except ValueError:
            total = 0
            non_citizen = 0
            naturalized = 0
            nat = 0

        tup = (total, nat, naturalized, non_citizen)

    return tup


def calc_totals(data_sorted):
    '''
    Calculates the sum of all data from 2016
    data_sorted: list of tuples of sorted data (list)
    Returns: Tuple of totals (tuple)
    '''
    nat_total = 0
    naturalized_total = 0
    non_citizen_total = 0

    state, nat, naturalized, nat_ratio, non_citizen, non_ratio \
        = zip(*data_sorted)

    for v in nat:
        nat_total += v
    for v in naturalized:
        naturalized_total += v
    for v in non_citizen:
        non_citizen_total += v

    total = (nat_total + naturalized_total + non_citizen_total)

    return (nat_total, naturalized_total, non_citizen_total, total)


def make_lists_for_plot(native_2000, naturalized_2000, non_citizen_2000,
                        native_2016, naturalized_2016, non_citizen_2016):
    '''
    Rearranges lists to be plotted
    native_2000: total native born citizens in 2000 (int)
    naturalized_2000: total naturalized citizens in 2000 (int)
    non_citizen_2000: total non citizens in 2000 (int)
    native_2016: total native born citizens in 2016 (int)
    naturalized_2016: total naturalized citizens in 2016 (int)
    non_citizen_2016: total non citizens in 2016 (int)
    Returns: Tuple of lists of matching data (tuple)
    '''
    l1 = [native_2000, native_2016]
    l2 = [naturalized_2000, naturalized_2016]
    l3 = [non_citizen_2000, non_citizen_2016]
    tup = (l1, l2, l3)
    return tup


def plot_data(native_list, naturalized_list, non_citizen_list):
    '''Plot the three lists as bar graphs.'''

    X = pylab.arange(2)   # create 2 containers to hold the data for graphing
    # assign each list's values to the 3 items to be graphed, include a color
    # and a label
    pylab.bar(X, native_list, color='b', width=0.25, label="native")
    pylab.bar(X + 0.25, naturalized_list, color='g', width=0.25,
              label="naturalized")
    pylab.bar(X + 0.50, non_citizen_list, color='r', width=0.25,
              label="non-citizen")

    pylab.title("US Population")
    # label the y axis
    pylab.ylabel('Population (hundred millions)')
    # label each bar of the x axis
    pylab.xticks(X + 0.25 / 2, ("2000", "2016"))
    # create a legend
    pylab.legend(loc='best')
    # draw the plot
    pylab.show()
    # optionally save the plot to a file; file extension determines file type
    # pylab.savefig("plot.png")


def print_format(tup):
    '''
    Creates print formatting for data
    tup: tuple of data to be printed (tup)
    Returns: Formatted string (str)
    '''
    form = "{:<20s}{:>15,}{:>17,}{:>22.1%}{:>16,}{:>22.1%}".format(
            tup[0], tup[1], tup[2], tup[3], tup[4], tup[5])
    return form


def main():
    '''
    Controls output to user
    '''

    fp2016 = open_file()  # Opens 2016 file, stores file pointer in fp2016
    fp2000 = open_file()  # Opens 2000 file, stores file pointer in fp2000

    data2016 = read_2016_file(fp2016)  # stores sorted 2016 data in data2016
    data2000 = read_2000_file(fp2000)  # stores 2000 data in data2000

    print("{:^112s}\n".format("2016 Population: Native, Naturalized," +
          " Non-Citizen"))  # Prints out table title

    print("{:<20s}{:>15s}{:>17s}{:>22s}{:>16s}{:>22s}".format(
        "State", "Native", "Naturalized", "Percent Naturalized",
        "Non-Citizen", "Percent Non-Citizen"))  # Prints out table headings

    # Every tuple in data2016 is outputted to the user with formatting
    for tup in data2016:
        print(print_format(tup))

    # Print divider at bottom of table
    print("-" * 112)

    calc2016 = calc_totals(data2016)  # Calculate total of all 2016 data

    # Creates a tuple for the total of 2016 data
    total2016 = ("Total 2016", calc2016[0], calc2016[1],
                 (calc2016[1] / calc2016[3]), calc2016[2],
                 (calc2016[2] / calc2016[3]))
    # Prints 2016 totals with formatting
    print(print_format(total2016))

    # Creates a tuple for the total of 2000 data
    total2000 = ("Total 2000", data2000[1], data2000[2],
                 (data2000[2] / data2000[0]), data2000[3],
                 (data2000[3] / data2000[0]))
    # Prints 2000 totals with formatting
    print(print_format(total2000))

    # User inputs whether they want to plot the data or not
    plot = input("Do you want to plot? ")

    if plot.lower() == "yes":
        plot_tup = make_lists_for_plot(data2000[1], data2000[2], data2000[3],
                                       calc2016[0], calc2016[1], calc2016[2])
        # Make list for plotting and plot the data
        plot_data(plot_tup[0], plot_tup[1], plot_tup[2])

    fp2016.close()  # Close 2016 file
    fp2000.close()  # Close 2000 file


if __name__ == "__main__":
    main()
