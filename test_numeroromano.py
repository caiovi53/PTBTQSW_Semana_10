import unittest

from numeroromano import converte


class TestConverteNumeroRomano(unittest.TestCase):
    def test_i(self):
        self.assertEqual(converte("I"), 1)

    def test_v(self):
        self.assertEqual(converte("V"), 5)

    def test_ii(self):
        self.assertEqual(converte("II"), 2)

    def test_xxii(self):
        self.assertEqual(converte("XXII"), 22)

    def test_ix(self):
        self.assertEqual(converte("IX"), 9)

    def test_xxiv(self):
        self.assertEqual(converte("XXIV"), 24)

    def test_m(self):
        self.assertEqual(converte("M"), 1000)


if __name__ == "__main__":
    unittest.main()
