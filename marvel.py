from collections import Counter, namedtuple
import csv
import re

DATA = 'marvel-wikia-data.csv'

Character = namedtuple('Character', 'pid name sid align sex appearances year')


def convert_csv_to_dict(data=DATA):
    '''write a function to parse marvel-wikia-data.csv into a dict
       https://docs.python.org/3.7/library/csv.html#csv.DictReader
       should return a list of OrderedDicts or a list of Character
       namedtuples (see 'Character' above')'''
    pass


data = list(convert_csv_to_dict())


def most_popular_characters(n=5):
    '''get the most popular character by number of appearances
       accept an argument of n = number of most popular characters
       to return'''
    pass


def max_and_min_years_new_characters():
    '''Get the year with most and least new characters introduced respectively,
       return a tuple of (max_year, min_year)'''
    pass


def percentage_female():
    '''Get the percentage of female characters, only look at male and female,
       ignore the rest, return a percentage rounded to 2 digits'''
    pass


def good_vs_bad(sex):
    '''Return a dictionary of bad vs good vs neutral characters.
       This function receives an arg 'sex' and should be validated
       to only receive 'male' or 'female' as valid inputs (should
       be case insensitive, so could also pass it MALE)

       The expected result should be a dict with these keys and
       values percentages, rounded integers (values made up here):

       expected = {'Bad Characters': 33,
                   'Good Characters': 33,
                   'Neutral Characters': 33})
    '''
    pass


if __name__ == '__main__':
    most_popular_characters()
    max_and_min_years_new_characters()
    percentage_female()
    good_vs_bad('female')
    good_vs_bad('male')
