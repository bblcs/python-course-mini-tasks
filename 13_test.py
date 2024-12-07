import pytest
from foreign import foreign_matrix_power


def test_matrix_power_identity():
    m = [[1.0, 0.0], [0.0, 1.0]]
    result = foreign_matrix_power(m, 3)
    expected = [[1.0, 0.0], [0.0, 1.0]]
    assert result == expected


def test_matrix_power_zero():
    m = [[0.0, 0.0], [0.0, 0.0]]
    result = foreign_matrix_power(m, 3)
    expected = [[0.0, 0.0], [0.0, 0.0]]
    assert result == expected


def test_matrix_power_simple():
    m = [[1.0, 2.0], [3.0, 4.0]]
    result = foreign_matrix_power(m, 1)
    expected = [[1.0, 2.0], [3.0, 4.0]]
    assert result == expected


def test_matrix_power_square():
    m = [[1.0, 2.0], [3.0, 4.0]]
    result = foreign_matrix_power(m, 2)
    expected = [[7.0, 10.0], [15.0, 22.0]]
    assert result == expected


def test_matrix_power_cube():
    m = [[1.0, 2.0], [3.0, 4.0]]
    result = foreign_matrix_power(m, 3)
    expected = [[37.0, 54.0], [81.0, 118.0]]
    assert result == expected


def test_matrix_power_large_power():
    m = [[1.0, 1.0], [0.0, 1.0]]
    result = foreign_matrix_power(m, 5)
    expected = [[1.0, 5.0], [0.0, 1.0]]  # (A + B)^5 = A^5 + 5A^4B + ...
    assert result == expected


def test_invalid_input():
    with pytest.raises(TypeError):
        foreign_matrix_power("not a matrix", 2)

    with pytest.raises(TypeError):
        foreign_matrix_power([[1.0, 2.0], [3.0, 4.0]], "not a number")


if __name__ == "__main__":
    pytest.main()
