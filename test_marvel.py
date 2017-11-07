import pytest

from marvel import (convert_csv_to_dict,
                    most_popular_characters,
                    max_and_min_years_new_characters,
                    percentage_female,
                    good_vs_bad)


def test_convert_csv_to_dict():
    data = list(convert_csv_to_dict())
    assert len(data) == 16376

    expected_id = '1678'
    # could be a namedtuple or OrderedDict
    if hasattr(data[0], 'pid'):
        assert data[0].pid == expected_id
    else:
        assert expected_id in data[0].values()
    expected_name = 'Yologarch'

    # same: account for different data structures
    if hasattr(data[-1], 'name'):
        assert data[-1].name == expected_name
    else:
        assert expected_name in data[-1].values()

    # number of first appearances should match
    expected_count = 15561
    if hasattr(data[0], 'pid'):
        sum(bool(d.year) and 1 for d in data) == expected_count
    else:
        sum(bool(d['Year']) and 1 for d in data) == expected_count


def test_most_popular_characters():
    # test call arg
    len(most_popular_characters()) == 5
    len(most_popular_characters(3)) == 3

    expected = ['Louise Grant',
                'Grand Vizier',
                'Pyreus Kril',
                'Acroyear',
                'Yuriko Oyama']
    # order does not matter, should include these
    for exp in expected:
        assert exp in most_popular_characters()


def test_max_and_min_years_new_characters():
    assert max_and_min_years_new_characters() == ('1993', '1958')


def test_percentage_female():
    assert percentage_female() == 24.79


def test_good_vs_bad():
    # test call arg
    with pytest.raises(ValueError):
        assert good_vs_bad('')
    with pytest.raises(ValueError):
        assert good_vs_bad('wrong_val')

    males = good_vs_bad('MALE')  # case does not matter
    assert males.get('Bad Characters') == 55
    assert males.get('Good Characters') == 30
    assert males.get('Neutral Characters') == 15

    females = good_vs_bad('female')
    assert females.get('Bad Characters') == 31
    assert females.get('Good Characters') == 49
    assert females.get('Neutral Characters') == 20
