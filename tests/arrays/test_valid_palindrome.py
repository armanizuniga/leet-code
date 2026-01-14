from leetcode.arrays.valid_palindrome import valid_pali


def test_example_1():
    assert valid_pali("racecar") is True

def test_example_2():
    assert valid_pali("") is True

def test_example_3():
    assert valid_pali("armani") is False