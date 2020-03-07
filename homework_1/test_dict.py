import pytest

class TestDict():
    def test_item_existence(self):
        d = {1 : 'a', 2 : 'b'}
        assert d[1] == 'a'

    def test_clear_dict(self):
        d = {1 : 'a', 2 : 'b'}
        d.clear()
        assert d == dict()

    def test_update_key_value(self):
        d = {1 : 'a', 2 : 'b'}
        d.update({1 : 'f'})
        assert d[1] == 'f'

    def test_delete_key(self):
        d = {1 : 'a', 2 : 'b'}
        d.pop(1)
        assert (1 in d) == False

@pytest.mark.parametrize('x,y', [(1, 1), (2, '2'), (3, ''), ('4', 4)])
def test_add_item(x, y):
    d = {}
    d[x] = y
    assert d.get(x) == y
