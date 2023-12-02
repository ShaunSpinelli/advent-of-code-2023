from day_01 import get_first_last_number


def test_1():
    test_str = "1abc2"
    res = get_first_last_number(test_str)

    assert res == 12


def test_2():
    test_str = "pqr3stu8vwx"
    res = get_first_last_number(test_str)

    assert res == 38


def test_3():
    test_str = "a1b2c3d4e5f"
    res = get_first_last_number(test_str)

    assert res == 15


def test_4():
    test_str = "treb7uchet"
    res = get_first_last_number(test_str)

    assert res == 77


def test_5():
    test_str = "treb7utwo1ninechet"
    res = get_first_last_number(test_str)

    assert res == 79


def test_6():
    test_str = "eightwothree"
    res = get_first_last_number(test_str)

    assert res == 83


def test_7():
    test_str = "abcone2threexyz"
    res = get_first_last_number(test_str)

    assert res == 13


def test_8():
    test_str = "xtwone3four"
    res = get_first_last_number(test_str)

    assert res == 24


def test_9():
    test_str = "4nineeightseven2"
    res = get_first_last_number(test_str)

    assert res == 42


def test_10():
    test_str = "zoneight234"
    res = get_first_last_number(test_str)

    assert res == 14


def test_11():
    test_str = "7pqrstsixteen"
    res = get_first_last_number(test_str)

    assert res == 76


def test_12():
    test_str = "sevenine"
    res = get_first_last_number(test_str)

    assert res == 79


def test_13():
    test_str = "eighthree"
    res = get_first_last_number(test_str)

    assert res == 83
