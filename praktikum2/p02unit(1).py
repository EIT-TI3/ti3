# (c) KJR

import unittest
import p02YannicBreitig as p02


class Prak02Unit(unittest.TestCase):

    def testAufgabe1(self):
        print("\nTest zu Aufgabe 1")
        area = p02.create_area((1, 5))
        self.assertIsNone(area)
        area = p02.create_area((5, 1))
        self.assertIsNone(area)
        area = p02.create_area((11, 2))
        self.assertIsNone(area)
        area = p02.create_area((2, 11))
        self.assertIsNone(area)
        m = 6
        n = 8
        area = p02.create_area((m, n))
        self.assertIsNotNone(area)
        self.assertIsInstance(area, list)
        self.assertEqual(len(area), m)
        self.assertEqual(len(area[0]), n)
        self.assertFalse(id(area[0]) == id(area[1]))

    def testAufgabe2(self):
        print("\nTest zu Aufgabe 2")
        m = 7
        n = 8
        area = p02.create_area((m, n))
        p02.fill_area(area, (1, 2), True, 5)
        self.assertTrue(all([e == 'X' for e in area[1][2:7]]))
        p02.fill_area(area, (3, 4), False, 3)
        self.assertTrue(all([area[2][4] == ' ',
                             area[3][4] == 'X',
                             area[4][4] == 'X',
                             area[5][4] == 'X',
                             area[6][4] == ' ']))

    def testAufgabe4(self):
        print("\nTest zu Aufgabe 4")
        m = 7
        n = 8
        area = p02.create_area((m, n))
        p02.fill_area(area, (1, 2), True, 5)
        p02.fill_area(area, (3, 4), False, 3)

        #  Horizontal
        self.assertFalse(p02.check_area(area, (-1, 2), True, 4))
        self.assertFalse(p02.check_area(area, (2, 8), True, 4))
        self.assertFalse(p02.check_area(area, (2, -1), True, 4))
        self.assertFalse(p02.check_area(area, (2, 5), True, 4))
        self.assertFalse(p02.check_area(area, (3, 3), True, 3))
        self.assertFalse(p02.check_area(area, (5, 3), True, 3))
        self.assertFalse(p02.check_area(area, (1, 0), True, 3))
        self.assertTrue(p02.check_area(area, (1, 0), True, 2))
        self.assertTrue(p02.check_area(area, (0, 0), True, 8))
        self.assertTrue(p02.check_area(area, (2, 0), True, 8))
        self.assertTrue(p02.check_area(area, (6, 0), True, 8))
        self.assertTrue(p02.check_area(area, (3, 5), True, 3))
        self.assertTrue(p02.check_area(area, (4, 0), True, 4))
        self.assertTrue(p02.check_area(area, (5, 5), True, 3))

        # Proficheck Horizontal
        self.assertFalse(p02.check_area(area, (1, 0), True, 2, profi_check=True))
        self.assertFalse(p02.check_area(area, (0, 0), True, 8, profi_check=True))
        self.assertFalse(p02.check_area(area, (2, 0), True, 8, profi_check=True))
        self.assertFalse(p02.check_area(area, (6, 0), True, 8, profi_check=True))
        self.assertTrue(p02.check_area(area, (3, 6), True, 2, profi_check=True))
        self.assertTrue(p02.check_area(area, (4, 0), True, 3, profi_check=True))
        self.assertTrue(p02.check_area(area, (5, 0), True, 3, profi_check=True))
        self.assertTrue(p02.check_area(area, (3, 0), True, 3, profi_check=True))

        # Vertikal
        self.assertFalse(p02.check_area(area, (-1, 2), False, 4))
        self.assertFalse(p02.check_area(area, (0, 4), False, 4))
        self.assertFalse(p02.check_area(area, (0, -1), False, 4))
        self.assertFalse(p02.check_area(area, (0, 8), False, 4))
        self.assertFalse(p02.check_area(area, (0, 2), False, 3))
        self.assertFalse(p02.check_area(area, (0, 6), False, 3))
        self.assertFalse(p02.check_area(area, (5, 4), False, 2))
        self.assertTrue(p02.check_area(area, (0, 0), False, 7))
        self.assertTrue(p02.check_area(area, (0, 1), False, 7))
        self.assertTrue(p02.check_area(area, (0, 7), False, 7))
        self.assertTrue(p02.check_area(area, (2, 2), False, 5))
        self.assertTrue(p02.check_area(area, (2, 3), False, 5))
        self.assertTrue(p02.check_area(area, (2, 5), False, 5))
        self.assertTrue(p02.check_area(area, (2, 6), False, 5))

        # Proficheck Vertikal
        self.assertFalse(p02.check_area(area, (2, 3), False, 5, profi_check=True))
        self.assertFalse(p02.check_area(area, (2, 5), False, 5, profi_check=True))
        self.assertFalse(p02.check_area(area, (0, 1), False, 7, profi_check=True))
        self.assertFalse(p02.check_area(area, (0, 7), False, 7, profi_check=True))
        self.assertTrue(p02.check_area(area, (3, 2), False, 4, profi_check=True))
        self.assertTrue(p02.check_area(area, (0, 0), False, 7, profi_check=True))
        self.assertTrue(p02.check_area(area, (3, 6), False, 4, profi_check=True))

    def count_X(self, area):
        counter = sum([l.count('X') for l in area])
        return counter

    def testAufgabe5(self):
        print("\nTest zu Aufgabe 5")
        m = 7
        n = 8
        area = p02.create_area((m, n))
        p02.generate_boat(area, 5)
        p02.generate_boat(area, 4)
        p02.generate_boat(area, 3)
        p02.generate_boat(area, 2)
        self.assertEqual(self.count_X(area), 14)

    def testAufgabe6(self):
        print("\nTest zu Aufgabe 6")
        m = 7
        n = 8
        area = p02.create_area((m, n))
        boat_spec = {2: 3, 3: 2, 4: 1}
        p02.generate_boat(area, boat_spec)
        self.assertEqual(self.count_X(area), 16)


if __name__ == "__main__":
    unittest.main()
