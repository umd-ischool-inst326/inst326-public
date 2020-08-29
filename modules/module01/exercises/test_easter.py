""" Test the calculation of Gregorian Easter. """

# Replace "exercise1" below with the name of your script (without the .py).
from exercise1 import easter_date


def test_easter_date():
    assert easter_date(2021) == "April 4"
    assert easter_date(2022) == "April 17"
    assert easter_date(2024) == "March 31"
    assert easter_date(2029) == "April 1"
    assert easter_date(1943) == "April 25"
    assert easter_date(1818) == "March 22"
    assert easter_date(2019) == "April 21"
    assert easter_date(1715) == "April 21"
    assert easter_date(1992) == "April 19"
    assert easter_date(2011) == "April 24"
    assert easter_date(1981) == "April 19"
    assert easter_date(2049) == "April 18"
