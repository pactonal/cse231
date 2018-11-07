###############################################################################
# Project 7 | csv file reading
# Gets file as input
# Processes file data and displays it
# Asks user to plot data
#   If yes, plot
#   If no, exit
###############################################################################
import pylab   # needed for plotting

STATUS = ['Approved', 'Denied', 'Settled']


def open_file():
    '''
    Opens user inputted file
    Returns: File pointer
    '''
    opened = 0
    num = 0
    while opened != 1:
        if num < 1:
            try:
                filename = input("Please enter a file name: ")
                f = open(filename, "r")
                opened = 1
            except IOError:
                filename = input(
                        "File not found. Please enter a valid file name: ")
                num += 1
        else:
            try:
                filename = input(
                        "File not found. Please enter a valid file name: ")
                f = open(filename, "r")
                opened = 1
            except IOError:
                pass
    return f


def read_file(fp):
    '''
    Reads through and collect data from the 2016 file
    fp: File pointer to the 2016 data file
    Returns: Sorted list of tuples of state name and data (list)
    '''
    datalist = []

    for line in fp:
        line_lst = line.strip().split(",")
        year = line_lst[1].strip()
        airport = line_lst[4].strip()
        claim = line_lst[9].strip('$ ')
        for let in claim:
            if let == ";":
                claim = claim.replace(let, "")
        try:
            claim = float(claim)
        except ValueError:
            claim = -1
        status = line_lst[10].strip()
        settleAmount = line_lst[11].strip('$ ')
        for let in settleAmount:
            if let == ";":
                settleAmount = settleAmount.replace(let, "")
        try:
            settleAmount = float(settleAmount)
        except ValueError:
            settleAmount = -1
        tup = (year, airport, claim, status, settleAmount)

        if '' not in tup and tup[4] != -1 and tup[2] != -1:
            datalist.append(tup)
    return datalist


def process(data):
    '''
    Reads through data list and extracts data
    data: input data from read_file function (list)
    Returns: list of processed data (list)
    '''
    total = [0, 0, 0, 0, 0, 0, 0, 0]
    settled = [0, 0, 0, 0, 0, 0, 0, 0]
    denied = [0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(0, 8):
        for tup in data:
            name = tup[0]
            name = name[-2:]
            if name == ("0" + str(2 + i)) and (
                    tup[3] == "Approved" or tup[3] == "Settled"):
                settled[i] += 1
                total[i] += 1

    for i in range(0, 8):
        for tup in data:
            name = tup[0]
            name = name[-2:]
            if name == ("0" + str(2 + i)) and tup[3] == "Denied":
                denied[i] += 1
                total[i] += 1

    max_claim = 0
    num = 0
    vnum = 0
    ctotal = 0
    for i in range(0, 8):
        for tup in data:
            name = tup[0]
            name = name[-2:]
            if name == ("0" + str(2 + i)) and tup[3] in STATUS:
                num += 1
            if tup[3] != STATUS[1] and tup[3] in STATUS and tup[4] != 0 and (
                        name == ("0" + str(2 + i))):
                    ctotal += tup[4]
                    vnum += 1
            if tup[2] > max_claim:
                max_claim = tup[2]
                max_port = tup[1]
    average = ctotal / vnum

    ltup = (total, settled, denied, num, average, max_claim, max_port)

    return ltup


def display_data(tup):
    '''
    prints processed data in a nice format
    tup: input processed data (tuple)
    '''
    total = tup[0]
    settled = tup[1]
    denied = tup[2]
    print("TSA Claims Data: 2002 - 2009\n")
    print("N = {:,}".format(tup[3]))
    print("{:<8s}{:>8s}{:>8s}{:>8s}{:>8s}{:>8s}{:>8s}{:>8s}{:>8s}".format(
        " ", '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009'))
    print("{:<8s}{:>8,}{:>8,}{:>8,}{:>8,}{:>8,}{:>8,}{:>8,}{:>8,}".format(
        "Total", total[0], total[1], total[2], total[3], total[4], total[5],
        total[6], total[7]))
    print("{:<8s}{:>8,}{:>8,}{:>8,}{:>8,}{:>8,}{:>8,}{:>8,}{:>8,}".format(
        "Settled", settled[0], settled[1], settled[2], settled[3], settled[4],
        settled[5], settled[6], settled[7]))
    print("{:<8s}{:>8,}{:>8,}{:>8,}{:>8,}{:>8,}{:>8,}{:>8,}{:>8,}\n".format(
        "Denied", denied[0], denied[1], denied[2], denied[3], denied[4],
        denied[5], denied[6], denied[7]))
    print("Average settlement: ${:,.2f}".format(tup[4]))
    print("The maximum claim was ${:,.2f} at {} ".format(tup[5], tup[6]) +
          "Airport")


def plot_data(accepted_data, settled_data, denied_data):
    '''Plot the three lists as bar graphs.'''

    X = pylab.arange(8)   # create 8 items to hold the data for graphing
    # assign each list's values to the 8 items to be graphed, include a color
    # and a label
    pylab.bar(X, accepted_data, color='b', width=0.25, label="total")
    pylab.bar(X + 0.25, settled_data, color='g', width=0.25, label="settled")
    pylab.bar(X + 0.50, denied_data, color='r', width=0.25, label="denied")

    # label the y axis
    pylab.ylabel('Number of cases')
    # label each bar of the x axis
    pylab.xticks(X + 0.25 / 2, (
        "2002", "2003", "2004", "2005", "2006", "2007", "2008", "2009"))
    # create a legend
    pylab.legend(loc='best')
    # draw the plot
    pylab.show()
    # optionally save the plot to a file; file extension determines file type
    # pylab.savefig("plot.png")


def main():
    '''
    Opens file and processes and displays it.  Asks user if they want to plot
    '''
    with open_file() as tsa:
        next(tsa)
        tuplist = read_file(tsa)
        procdata = process(tuplist)

        display_data(procdata)

        p = input("Plot data (yes/no): ")
        if p == "yes":
            plot_data(procdata[0], procdata[1], procdata[2])


if __name__ == "__main__":
    main()
