# Follow https://numpy.org/devdocs/user/quickstart.html
import numpy as np
from numpy.testing import assert_array_equal, assert_array_almost_equal


def test_one_dimension_array():
    np_array = np.arange(15)
    assert_array_equal(np_array, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])

    np_array = np.arange(10, 30, 5)
    assert_array_equal(np_array, [10, 15, 20, 25])


def test_one_dimension_float_array():
    np_array = np.arange(0, 2, 0.3)
    assert_array_almost_equal(np_array, [0., 0.3, 0.6, 0.9, 1.2, 1.5, 1.8], decimal=2)

    np_array = np.linspace(0, 2, 9)
    assert_array_almost_equal(np_array, [0., 0.25, 0.5, 0.75, 1., 1.25, 1.5, 1.75, 2.], decimal=2)


def test_two_dimension_array():
    size = 8
    np_array = np.arange(size).reshape(4, 2)
    expected_array = [[0, 1], [2, 3], [4, 5], [6, 7]]
    assert_array_equal(np_array, expected_array)

    np_array = np.arange(size).reshape(2, 4)
    expected_array = [[0, 1, 2, 3], [4, 5, 6, 7]]
    assert_array_equal(np_array, expected_array)

    assert np_array.shape == (2, 4)
    assert np_array.ndim == 2
    assert np_array.dtype.name == "int64"
    assert np_array.size == size


def test_basic_operations():
    a = np.array([20, 30, 40, 50])
    b = np.arange(4)
    c = a - b
    assert_array_equal(c, [20, 29, 38, 47])
    c = a + b
    assert_array_equal(c, [20, 31, 42, 53])
    c = a < 35
    assert_array_equal(c, [True, True, False, False])
    a += 2
    assert_array_equal(a, [22, 32, 42, 52])


def test_array_multiplication():
    a = np.array([[1, 1],
                  [0, 1]])
    b = np.array([[2, 0],
                  [3, 4]])
    c = a * b
    assert_array_equal(c, [[2, 0], [0, 4]])

    # [[1*2 + 1*3 = 5, 1*0 + 1*4 = 4],
    #  [0*2 + 1*3 = 3, 0*0 + 1*4 = 4]]
    c = a @ b
    assert_array_equal(c, [[5, 4], [3, 4]])
    c = a.dot(b)
    assert_array_equal(c, [[5, 4], [3, 4]])

    a = np.ones((2, 3), dtype=np.int_)
    a *= 3
    assert_array_equal(a, [[3, 3, 3], [3, 3, 3]])


def test_aggregations():
    # [[0, 1, 2, 3], [4, 5, 6, 7]]
    np_array = np.arange(8).reshape(2, 4)
    assert np_array.sum() == 28
    assert np_array.min() == 0
    assert np_array.max() == 7

    assert_array_equal(np_array.sum(axis=0), [4, 6, 8, 10])
    assert_array_equal(np_array.min(axis=0), [0, 1, 2, 3])
    assert_array_equal(np_array.max(axis=0), [4, 5, 6, 7])

    assert_array_equal(np_array.sum(axis=1), [6, 22])
    assert_array_equal(np_array.min(axis=1), [0, 4])
    assert_array_equal(np_array.max(axis=1), [3, 7])


def test_indexes():
    # [0, 1, 2, 3, 4, 5, 6, 7]
    a = np.arange(8)
    b = a[2:5]
    assert_array_equal(b, [2, 3, 4])

    a[:6:2] = 10
    assert_array_equal(a, [10, 1, 10, 3, 10, 5, 6, 7])
    assert_array_equal(a[::-1], [7, 6, 5, 10, 3, 10, 1, 10])

    # [[0, 1, 2, 3], [4, 5, 6, 7]]
    a = np.arange(8).reshape(2, 4)
    assert a[1, 1] == 5
    assert_array_equal(a[:, 1], [1, 5])
    assert_array_equal(a[1, :], [4, 5, 6, 7])
    assert_array_equal(a[-1], [4, 5, 6, 7])

    for row in a:
        assert len(row) == 4

    for element in a.flat:
        assert isinstance(element, np.int64)
