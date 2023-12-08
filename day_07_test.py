from day_07 import hand_to_score


def test_1():
    test_str = "JQ9QK"
    res = hand_to_score(test_str)

    assert str(res)[0] == "4"


def test_2():
    test_str = "JJQ4Q" # 5 wronf
    res = hand_to_score(test_str)

    assert str(res)[0] == "6"