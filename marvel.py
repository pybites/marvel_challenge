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
    with open(data) as csvfile:
        for row in csv.DictReader(csvfile):
            name = re.sub(r'(.*?)\(.*', r'\1', row['name']).strip()
            # could do:
            # yield row
            # but namedtuple is more elgant
            # tried to make pytest work with both
            yield Character(pid=row['page_id'],
                            name=name,
                            sid=row['ID'],
                            align=row['ALIGN'],
                            sex=row['SEX'],
                            appearances=row['APPEARANCES'],
                            year=row['Year'])


data = list(convert_csv_to_dict())


def most_popular_characters(n=5):
    '''get the most popular character by number of appearances
       accept an argument of n (int) of most popular characters
       to return (leave default of 5)'''
    common = sorted([d for d in data if d.appearances.isdigit()],
                    key=lambda x: int(x.appearances),
                    reverse=True)
    return [c.name for c in common[:n]]


def max_and_min_years_new_characters():
    '''Get the year with most and least new characters introduced respectively,
       use either the 'FIRST APPEARANCE' or 'Year' column in the csv data, or
       the 'year' attribute of the namedtuple, return a tuple of
       (max_year, min_year)'''
    max_ = Counter(d.year for d in data if d.year).most_common(1)[0][0]
    min_ = Counter(d.year for d in data if d.year).most_common()[-1][0]
    return (max_, min_)


def percentage_female():
    '''Get the percentage of female characters, only look at male and female,
       ignore the rest, return a percentage rounded to 2 digits'''
    sexes = Counter(d.sex for d in data)
    sex_female = sexes['Female Characters']
    sex_male = sexes['Male Characters']
    female_perc = sex_female / (sex_female + sex_male) * 100
    return round(female_perc, 2)


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
    sex = sex.lower()
    if sex not in 'male female'.split():
        raise ValueError('not a valid sex')

    sex = sex.title() + ' Characters'
    cnt = Counter(d.align for d in data if d.align and d.sex == sex)
    total = sum(cnt.values())
    cnt2 = {}
    for k, v in cnt.items():
        cnt2[k] = round(v/total*100)
    return cnt2


if __name__ == '__main__':
    most_popular_characters()
    max_and_min_years_new_characters()
    percentage_female()
    good_vs_bad('female')
    good_vs_bad('male')
