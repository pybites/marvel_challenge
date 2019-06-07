from collections import Counter, namedtuple
import csv
import re

DATA = 'marvel-wikia-data.csv'

Character = namedtuple('Character', 'pid name sid align sex appearances year')


def convert_csv_to_dict(data=DATA):
    '''write a function to parse marvel-wikia-data.csv, see
       https://docs.python.org/3.7/library/csv.html#csv.DictReader
       should return a list of OrderedDicts or a list of Character
       namedtuples (see Character namedtuple above')'''
    lst = []
    with open(data, "r") as infile:
        reader = csv.DictReader(infile)
        for row in reader:
            c = Character(  row['page_id'], 
                            row['name'], 
                            row['ID'], 
                            row['ALIGN'], 
                            row['SEX'],
                            row['APPEARANCES'],
                            row['Year']
                        )
            lst.append(c)
    return lst


data = list(convert_csv_to_dict())


def most_popular_characters(n=5):
    '''get the most popular character by number of appearances
       accept an argument of n (int) of most popular characters
       to return (leave default of 5)'''
    res =   list(sorted(
                            [x for x in data], key=lambda x: int(x.appearances) \
                            if x.appearances != "" else 0, reverse=True
                        )
                )[:n]

    pattern = re.compile("(.*)\s\(")
    characters = [pattern.search(x.name).group(1) for x in res]
    return characters
    


def max_and_min_years_new_characters():
    '''Get the year with most and least new characters introduced respectively,
       use either the 'FIRST APPEARANCE' or 'Year' column in the csv data, or
       the 'year' attribute of the namedtuple, return a tuple of
       (max_year, min_year)'''
    res = Counter([x.year for x in data if x.year != ""])
    most_common = res.most_common()
    return most_common()[0][0], most_common()[-1][0]



def percentage_female():
    '''Get the percentage of female characters, only look at male and female
       for total, ignore the rest, return a percentage rounded to 2 digits'''
    # print(len(data))
    # print(len([x for x in data if x.sex == "Female Characters"])/ len(data))
    return round(   (len([x for x in data if x.sex == "Female Characters"])/ \
                    len([x for x in data if x.sex == "Female Characters" or \
                    x.sex == "Male Characters"]))*100,2)


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
    if sex.lower() not in ['male', 'female']:
        raise ValueError

    expected = {    'Bad Characters': 0,
                    'Good Characters': 0,
                    'Neutral Characters': 0
                }
    res = [x for x in data if x.sex == sex.capitalize() + " Characters" and x.align != ""]
    t = len(res)
    c = Counter([x.align for x in res])
    for item in c.most_common():
        expected[item[0]] = int(round(item[1]/t,2)*100)
    return expected



if __name__ == '__main__':
    most_popular_characters()
    max_and_min_years_new_characters()
    percentage_female()
    good_vs_bad('female')
    good_vs_bad('male')
