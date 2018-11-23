#!/usr/bin/env python3
###############################################################################
# Project 9
#
#
#
#
###############################################################################
import csv
import string
import pylab
# from operator import itemgetter


def open_file(message):
    '''
    Opens user inputted file
    Returns: File pointer
    '''
    opened = 0
    num = 0
    while opened != 1:
        if num < 1:
            try:
                filename = input(message)
                f = open(filename, "r")
                opened = 1
            except IOError:
                filename = input(
                        "File is not found! Try again! ")
                num += 1
        else:
            try:
                filename = input(
                        "File is not found! Try again! ")
                f = open(filename, "r")
                opened = 1
            except IOError:
                pass
    return f


def read_stopwords(fp):
    '''
        Reads stopwords from file
        fp: file pointer to stopwords.txt
        returns: list of stopwords (list)
    '''
    lst = set()  # create empty set
    for word in fp:  # iterate through all words
        word = word.strip().lower()
        lst.add(word)  # add word to list

    return lst


def validate_word(word, stopwords):
    '''
        Checks if inputted word is in the stopwords
        word: word from song lyrics
        stopwords: list of stopwords
        returns: True or False if word is valid (bool)
    '''
    word = word.strip(string.punctuation)
    word = word.strip(string.digits)
    word = word.strip(string.whitespace)  # remove unwanted chars
    word = word.lower()
    for let in word:
        if let in string.punctuation:
            return False
    if word in stopwords or word in string.digits and word == '':
        return False
    else:
        return True


def process_lyrics(lyrics, stopwords):
    '''
        Processes lyrics and filters words not in stopwords
        lyrics: Song lyrics from data file
        stopwords: list of stopwords
        returns: set of lyrics not in stopwords (set)
    '''
    lyrics = lyrics.split(" ")

    proclyrics = set()  # create an empty set

    for word in lyrics:
        word = word.strip(string.whitespace + string.punctuation).lower()
        if validate_word(word, stopwords):
            proclyrics.add(word)  # add word to set

    return proclyrics


def read_data(fp, stopwords):
    '''
        Reads through all data and creates nested dict of data
        fp: File pointer to data file
        stopwords: list of stopwords
        returns: dictionary of singers, songs and lyrics (dict)
    '''
    datadict = {}
    reader = csv.reader(fp)
    next(reader)
    for row in reader:  # iterate though all rows
        artist = row[0]
        song = row[1]
        lyrics = row[2]
        lyrics = process_lyrics(lyrics, stopwords)

        if artist not in datadict.keys():
            datadict[artist] = {}
        if song not in datadict[artist].keys():
            datadict[artist][song] = lyrics  # create dict of dict

    return datadict


def update_dictionary(data_dict, singer, song, words):
    '''
        Updates dictionary with inputted parameters
        data_dict: dictionary of data
        singer: singer name (str)
        song: song name (str)
        words: set of words (set)
    '''
    if singer not in data_dict:
        data_dict[singer] = {}  # create dict for singers
    if song not in data_dict[singer]:
        data_dict[singer][song] = words  # create dict of dict


def calculate_average_word_count(data_dict):
    '''
        Calculates average words per song
        data_dict: dictionary of data from read_data
        returns: dictionary of singers and respective average word count (dict)
    '''
    datadict = {}
    for singer in data_dict:
        numwords = 0
        numsongs = len(data_dict[singer].keys())
        for song in data_dict[singer]:  # iterate through all songs
            numwords += len(data_dict[singer][song])  # increment words
        avg = numwords / numsongs  # calc average
        if singer not in datadict:
            datadict[singer] = avg

    return datadict


def find_singers_vocab(data_dict):
    '''
        Finds unique words that singer uses
        data_dict: data from read_data function
        returns: dictionary of singer and unique words (dict)
    '''
    datadict = {}
    for singer in data_dict:
        vocab = set()
        for song in data_dict[singer]:
            for word in data_dict[singer][song]:  # iterate through all words
                vocab.add(word)                   # in song
        if singer not in datadict:
            datadict[singer] = vocab

    return datadict


def display_singers(combined_list):
    '''
        Displays data
        combined_list: list of singer, average words, vocab, and total songs
    '''
    pass
    print("{:^80s}".format("Singers by Average Word Count (TOP - 10)"))
    print("{:<20s}{:>20s}{:>20s}{:>20s}".format("Singer", "Average Word Count",
                                                "Vocabulary Size",
                                                "Number of Songs"))
    print('-' * 80)
    print("{:<20s}{:>20f}{:>20d}{:>20f}".format(combined_list[0],
                                                combined_list[1],
                                                combined_list[2],
                                                combined_list[3]))


def vocab_average_plot(num_songs, vocab_counts):
    """
    Plot vocab. size vs number of songs graph
    num_songs: number of songs belong to singers (list)
    vocab_counts: vocabulary size of singers (list)
    """
    pylab.scatter(num_songs, vocab_counts)
    pylab.ylabel('Vocabulary Size')
    pylab.xlabel('Number of Songs')
    pylab.title('Vocabulary Size vs Number of Songs')
    pylab.show()


def search_songs(data_dict, words):
    '''
        Searches for inputted words in songs
        data_dict: data from read_data function
        words: inputted list of words to search
        returns: list of artist and songs with inputted words in them (list)
    '''
    songlist = []
    for singer in data_dict:
        for song in data_dict[singer]:
            match = 0
            for word in words:
                if word in data_dict[singer][song]:
                    match += 1
            if match == len(words):
                tup = (singer, song)
                songlist.append(tup)
    return songlist


def main():
    '''
        Controls user input and output
    '''
    fp1 = open_file('Enter a filename for the stopwords: ')
    fp = open_file('Enter a filename for the song data: ')
    stopwords = read_stopwords(fp1)
    data = read_data(fp, stopwords)
    average = calculate_average_word_count(data)
    vocab = find_singers_vocab(data)
    combined_list = []
    for singer in average:
        tup = (singer, average[singer], len(data[singer]), len(vocab[singer]))
        combined_list.append(tup)
    for tup in combined_list:
        display_singers(tup)
    # 'Do you want to plot (yes/no)?: '

#    RULES = """1-) Words should not have any digit or punctuation
# 2-) Word list should not include any stop-word"""

    # "Search Lyrics by Words"
    # "Input a set of words (space separated), press enter to exit: "
    # 'Error in words!'
    # "There are {} songs containing the given words!"
    # "{:<20s} {:<s}"


if __name__ == '__main__':
    main()
