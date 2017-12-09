from calculations import numbers_sum


def test_numbers_sum():
    assert numbers_sum(10, 40) == 52
    assert numbers_sum(1, 4) == 7


test_numbers_sum()