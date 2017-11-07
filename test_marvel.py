from collections import namedtuple
import pytest

from marvel import (convert_csv_to_dict,
                    most_popular_characters,
                    max_and_min_years_new_characters,
                    percentage_female,
                    good_vs_bad)

def _to_dict(nt):
    return type(nt) == namedtuple and nt._asdict or nt


def test_convert_csv_to_dict():
    data = list(convert_csv_to_dict())
    assert len(data) == 16376

    first_row = list(data[0].values())
    assert '1678' in first_row
    assert 'Spider-Man' in first_row

    last_row = list(data[-1].values())
    assert 'Yologarch' in last_row
    assert 'Bad Characters' in last_row

    # number of first appearances should match
    year = 'year' if 'year' in data[0].keys() else 'Year'
    expected_count = 15561
    actual_count = sum(bool(_to_dict(d)[year]) and 1 for d in data)
    assert expected_count == actual_count


def test_most_popular_characters():
    # test call arg
    len(most_popular_characters()) == 5
    len(most_popular_characters(3)) == 3

    expected = ['Spider-Man',
                'Captain America',
                'Wolverine',
                'Iron Man',
                'Thor']
    # order does not matter, should include these
    for exp in expected:
        assert exp in most_popular_characters()


def test_max_and_min_years_new_characters():
    max_, min_ = max_and_min_years_new_characters()
    assert int(max_) == 1993
    assert int(min_) == 1958


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
