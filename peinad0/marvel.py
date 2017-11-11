from collections import Counter, namedtuple
import csv
import re
from math import floor

DATA = 'marvel-wikia-data.csv'


Character = namedtuple('Character', 'page,name,urlslug,id,align,eye,hair,sex,gsm,alive,appearences,first_appearence,year')
FEMALE = 'Female Characters'
MALE = 'Male Characters'

def convert_csv_to_dict(data=DATA):
    characters = []
    reader = csv.reader(open(data, newline=''), delimiter=',', quotechar='"')
    headers = next(reader)
    for character in map(Character._make, reader):
        characters.append(character)
    return characters

"""
def convert_csv_to_dict(data=DATA):
    '''write a function to parse marvel-wikia-data.csv, see
       https://docs.python.org/3.7/library/csv.html#csv.DictReader
       should return a list of OrderedDicts or a list of Character
       namedtuples (see Character namedtuple above')'''
    dict1 = []
    with open(data, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        headers = next(reader)
        for row in reader:
            aux = {}
            for index, key in enumerate(headers):
                aux[key] = row[index]
            dict1.append(aux)
    return dict1
"""
data = list(convert_csv_to_dict())


def remove_parenthesis_content(names):
    rlist = []
    for name in names:
        rlist.append(name[:name.find('(') - 1])
    return rlist

def most_popular_characters(n=5):
    '''get the most popular character by number of appearances
       accept an argument of n (int) of most popular characters
       to return (leave default of 5)'''
    list1 = [ a.name for a in sorted(data, key=lambda x: int(x.appearences or '0'), reverse=True)[:n]]
    return remove_parenthesis_content(list1)


def max_and_min_years_new_characters():
    '''Get the year with most and least new characters introduced respectively,
       use either the 'FIRST APPEARANCE' or 'Year' column in the csv data, or
       the 'year' attribute of the namedtuple, return a tuple of
       (max_year, min_year)'''
    dict1 = {}
    for character in data:
        year = character.year
        if not year:
            continue
        num = dict1.get(year, 0) + 1
        dict1[year] = num
    return (max(dict1, key=dict1.get), min(dict1, key=dict1.get))


def percentage_female():
    '''Get the percentage of female characters, only look at male and female
       for total, ignore the rest, return a percentage rounded to 2 digits'''
    females = len([a for a in data if a.sex == FEMALE])
    males = len([a for a in data if a.sex == MALE])
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
        'male': MALE,
        'female': FEMALE,
    }
    GOOD ='Good Characters'
    BAD ='Bad Characters'
    NEUTRAL ='Neutral Characters'
    gender_filter = ''
    valid = ['male', 'female']
    if sex.lower() not in valid:
        raise ValueError
    else:
        gender_filter = d1.get(sex.lower())
    good = len([a for a in data if a.align == GOOD and a.sex == gender_filter])
    bad = len([a for a in data if a.align == BAD and a.sex == gender_filter])
    neutral = len([a for a in data if a.align == NEUTRAL and a.sex == gender_filter])
    total = float(good + bad + neutral)
    return {
        BAD: round((bad/total) * 100),
        GOOD: round((good/total) * 100),
        NEUTRAL: round((neutral/total) * 100)
    }

if __name__ == '__main__':
    most_popular_characters()
    percentage_female()
    good_vs_bad('female')
    good_vs_bad('male')
    max_and_min_years_new_characters()
