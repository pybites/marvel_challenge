from collections import Counter, namedtuple
import csv
import re
from math import floor

DATA = 'marvel-wikia-data.csv'

Character = namedtuple('Character', 'pid name sid align sex appearances year')


def convert_csv_to_dict(data=DATA):
    '''write a function to parse marvel-wikia-data.csv, see
       https://docs.python.org/3.7/library/csv.html#csv.DictReader
       should return a list of OrderedDicts or a list of Character
       namedtuples (see Character namedtuple above')'''
    dict1 = []
    with open(DATA, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        headers = next(reader)
        for row in reader:
            aux = {}
            for index, key in enumerate(headers):
                aux[key] = row[index]
            dict1.append(aux)
    return dict1

data = list(convert_csv_to_dict())


def sanitize_list(names):
    rlist = []
    for name in names:
        for idx, character in enumerate(name):
            if character == '(':
                rlist.append(name[:idx-1])
                break
    return rlist

def most_popular_characters(n=5):
    '''get the most popular character by number of appearances
       accept an argument of n (int) of most popular characters
       to return (leave default of 5)'''
    list1 = [ a.get('name') for a in sorted(data, key=lambda x: int(x.get('APPEARANCES') or '-1'), reverse=True)[:n]]
    return sanitize_list(list1)


def max_and_min_years_new_characters():
    '''Get the year with most and least new characters introduced respectively,
       use either the 'FIRST APPEARANCE' or 'Year' column in the csv data, or
       the 'year' attribute of the namedtuple, return a tuple of
       (max_year, min_year)'''
    dict1 = {}
    for character in data:
        year = character.get('Year')
        if not year:
            continue
        num = dict1.get(year, 0) + 1
        dict1[year] = num
    return (max(dict1, key=dict1.get), min(dict1, key=dict1.get))


def percentage_female():
    '''Get the percentage of female characters, only look at male and female
       for total, ignore the rest, return a percentage rounded to 2 digits'''
    females = len([a for a in data if a.get('SEX') == 'Female Characters'])
    males = len([a for a in data if a.get('SEX') == 'Male Characters'])
    return round(100 * (females/(females+males)),2)


def good_vs_bad(sex):
    '''Return a dictionary of bad vs good vs neutral characters.
       This function receives an arg 'sex' and should be validated
       to only receive 'male' or 'female' as valid inputs (should
       be case insensitive, so could also pass it MALE)

       The expected result should be a the following dict. The values are
       rounded (int) percentages (values made up here):

       expected = {'Bad Characters': 33,
                   'Good Characters': 33,
                   'Neutral Characters': 33})
    '''
    d1 = {
        'male': 'Male Characters',
        'female': 'Female Characters',
    }
    gender_filter = ''
    valid = ['male', 'female']
    if sex.lower() not in valid:
        raise ValueError
    else:
        gender_filter = d1.get(sex.lower())
    good = len([a for a in data if a.get('ALIGN') == 'Good Characters' and a.get('SEX') == gender_filter])
    bad = len([a for a in data if a.get('ALIGN') == 'Bad Characters' and a.get('SEX') == gender_filter])
    neutral = len([a for a in data if a.get('ALIGN') == 'Neutral Characters' and a.get('SEX') == gender_filter])
    total = float(good + bad + neutral)
    return {
        'Bad Characters': round((bad/total) * 100),
        'Good Characters': round((good/total) * 100),
        'Neutral Characters': round((neutral/total) * 100)
    }



def pene():
    import csv
    with open('eggs.csv', newlipne='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in spamreader:
            print(', '.join(row))

if __name__ == '__main__':
    print(most_popular_characters())
    print(percentage_female(), '%')
    print(good_vs_bad('female'))
    print(good_vs_bad('male'))
    print(max_and_min_years_new_characters())
