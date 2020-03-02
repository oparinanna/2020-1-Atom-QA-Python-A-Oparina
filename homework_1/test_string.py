import pytest

class TestString:
    def test_sum_of_strings(self):
        a = 'abc'
        b = 'def'
        assert a + b == 'abcdef'

    def test_string_length(self):
        a = 'testing'
        assert len(a) == 7

    def test_string_comparison(self):
        a = 'aaa'
        b = 'aaa'
        assert a == b

    def test_str_and_int_comparison(self):
        a = '111'
        b = 111
        with pytest.raises(AssertionError):
            assert a == b

@pytest.mark.parametrize('i', ['qwe', 'ert', 'ewq'])
def test_count_element(i):
    assert i.count('e') == 1
