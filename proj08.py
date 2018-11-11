#!/usr/bin/env python3
###############################################################################
#
#
#
#
#
#
###############################################################################
import pylab
# from operator import itemgetter

REGIONS = {'MENA': 'Middle East and North Africa', 'EUR': 'Europe',
           'AFR': 'Africa', 'NAC': 'North America and Caribbean',
           'SACA': 'South and Central America',
           'WP': 'Western Pacific', 'SEA': 'South East Asia'}


def open_file():
    '''
    Opens user inputted file
    Returns: File pointer
    '''
    opened = 0
    while opened != 1:
        try:
            filename = input("Enter a file name: ")
            f = open(filename, "r", encoding="windows-1252")
            opened = 1
        except IOError:
            print("Error. Please try again.")
            opened = 0
    return f


def create_dictionary(fp):
    '''
        Place Docstring here!
    '''
    datadict = {}

    for line in fp:
        line_list = line.strip().split(',')

        country = line_list[1]
        region = line_list[2]
        age_group = line_list[3]
        gender = line_list[4]
        geographic_area = line_list[5]
        diabetes = int(float(line_list[6]) * 1000)
        population = int(float(line_list[7]) * 1000)

        tup = (gender, geographic_area, diabetes, population)

        datadict[region] = {}
        datadict[region][country] = {}
        datadict[region][country][age_group] - {}
        datadict[region][country][age_group].append(tup)

    return datadict


def get_country_total(data):
    '''
        Place Docstring here!
    '''
    pass


def display_table(data, region):
    '''
        Place Docstring here!
    '''
    pass


def prepare_plot(data):
    '''
        Place Docstring here!
    '''
    pass


def plot_data(plot_type, data, title):
    '''
        This function plots the data.
            1) Bar plot: Plots the diabetes prevalence of various age groups in
                         a specific region.
            2) Pie chart: Plots the diabetes prevalence by gender.

        Parameters:
            plot_type (string): Indicates what plotting function is used.
            data (dict): Contains the dibetes prevalence of all the contries
                         within a specific region.
            title (string): Plot title

        Returns:
            None

    '''

    plot_type = plot_type.upper()

    categories = data.keys()  # Have the list of age groups
    gender = ['FEMALE', 'MALE']  # List of the genders used in this dataset

    if plot_type == 'BAR':

        # List of population with diabetes per age group and gender
        female = [data[x][gender[0]] for x in categories]
        male = [data[x][gender[1]] for x in categories]

        # Make the bar plots
        width = 0.35
        p1 = pylab.bar([x for x in range(len(categories))], female,
                       width=width)
        p2 = pylab.bar([x + width for x in range(len(categories))], male,
                       width=width)
        pylab.legend((p1[0], p2[0]), gender)

        pylab.title(title)
        pylab.xlabel('Age Group')
        pylab.ylabel('Population with Diabetes')

        # Place the tick between both bar plots
        pylab.xticks([x + width/2 for x in range(len(categories))], categories,
                     rotation='vertical')
        pylab.show()
        # optionally save the plot to a file; file extension determines
        # file type
        # pylab.savefig("plot_bar.png")

    elif plot_type == 'PIE':

        # total population with diabetes per gender
        male = sum([data[x][gender[1]] for x in categories])
        female = sum([data[x][gender[0]] for x in categories])

        pylab.title(title)
        pylab.pie([female, male], labels=gender, autopct='%1.1f%%')
        pylab.show()
        # optionally save the plot to a file; file extension determines
        # file type
        # pylab.savefig("plot_pie.png")


def main():

    "\nDiabetes Prevalence Data in 2017"
    MENU = \
        '''
                Region Codes
    MENA: Middle East and North Africa
    EUR: Europe
    AFR: Africa
    NAC: North America and Caribbean
    SACA: South and Central America
    WP: Western Pacific
    SEA: South East Asia
    '''

    "Enter region code ('quit' to terminate): "
    "Do you want to visualize diabetes prevalence by age group and gender\
     (yes/no)?: "
    "Error with the region key! Try another region"
    "Incorrect Input! Try Again!"

    with open_file() as fp:
        data = create_dictionary(fp)
        for region in data:
            for country in region:
                for age_group in country:
                    total = get_country_total(age_group)


if __name__ == "__main__":
    main()
