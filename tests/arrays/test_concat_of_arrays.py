from leetcode.arrays.concat_of_array import array_cat


def test_example_1():
    assert array_cat([1, 2, 1]) == [1, 2, 1, 1, 2, 1]


def test_example_2():
    assert array_cat([1]) == [1, 1]
