import pytest

class TestSet():
    def test_set_length(self):
        a = {1, 2, 'a', 'b', 1}
        assert len(a) == 4

    def test_add_item(self):
        a = {2, 1, 4}
        a.add(3)
        assert (3 in a) == True

    def test_delete_item(self):
        b = {11}
        b.remove(11)
        assert b == set()

    def test_union_of_sets(self):
        a = {1, 2, 3}
        b = {1, 4, 5}
        assert a.union(b) == {1, 2, 3, 4, 5}

@pytest.mark.parametrize('x', [{'a', 'b', 'c'}])
@pytest.mark.parametrize('y', [{'a', 'b', 'c'}, {'b', 'c', 'a'}, {'c', 'a', 'b'}])
def test_set_comparison(x, y):
    assert x == y
