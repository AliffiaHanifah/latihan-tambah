
from main import tambah


class TestSum():

    def test_zero(self):
        assert tambah(0,0) == 0

    def test_one(self):
        assert tambah(1, 1) == 2

    def test_two(self):
        assert tambah(2, 1) == 3
    
    def test_three(self):
        assert tambah(3, 5) == 8

    def test_four(self):
        assert tambah(4, 5) == 9

    def test_decimal(self):
        assert tambah(1.0, 2.0) == 3