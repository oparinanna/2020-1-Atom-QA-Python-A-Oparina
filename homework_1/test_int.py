import pytest

class TestInt:

    def test_division_by_zero(self):
        with pytest.raises(ZeroDivisionError):
            assert 1 / 0

    def test_subtraction_of_numbers(self):
        assert 5 - 1 == 4

    def test_multiplication_by_zero(self):
        assert 5 * 0 == 0

    def test_sum_of_numbers(self):
        assert 8 + 0 == 0 + 8

@pytest.mark.parametrize('x,y', [(5, 0), (0, -5), (-5, -5)])
def test_comparison_of_numbers(x, y):
    assert x >= y
