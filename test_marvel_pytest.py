import pytest

from marvel import (convert_csv_to_dict,
                    most_popular_characters,
                    max_and_min_years_new_characters,
                    percentage_female,
                    good_vs_bad)


def test_convert_csv_to_dict():
    data = list(convert_csv_to_dict())
    assert len(data) == 16376


def test_most_popular_characters():
    expected_no_arg_or_arg_5 = ['Spider-Man',
                                'Captain America',
                                'Wolverine',
                                'Iron Man',
                                'Thor']
    expected_arg_3 = expected_no_arg_or_arg_5[:3]
    most_popular_characters() == expected_no_arg_or_arg_5
    most_popular_characters(5) == expected_no_arg_or_arg_5
    most_popular_characters(3) == expected_arg_3


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

    males = good_vs_bad('MALE')  # case should not matter
    assert males.get('Bad Characters') == 55
    assert males.get('Good Characters') == 30
    assert males.get('Neutral Characters') == 15

    females = good_vs_bad('female')
    assert females.get('Bad Characters') == 31
    assert females.get('Good Characters') == 49
    assert females.get('Neutral Characters') == 20
