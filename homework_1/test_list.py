import pytest

class TestList():
    def test_sum_lists(self):
        a = [1, 2, 3]
        b = [4]
        assert a + b == [1, 2, 3, 4]

    def test_list_length(self):
        assert len(['a'] * 6) == 6

    def test_delete_element(self):
        a = [1, 2, 3, 4, 5, 6]
        a.pop(2)
        assert a[2] != 3

    def test_add_element(self):
        a = []
        a.append(1)
        assert a != []

@pytest.mark.parametrize('x,y', [([1], [1]), ([1, 1], [1, 1]), (['a', 'b'], ['b', 'a']), ([1, '1'], ['1', 1])])
def test_reverse_list(x, y):
    assert x == y[::-1]
