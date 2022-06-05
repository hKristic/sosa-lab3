import unittest
from dodatak_A import OperationsManager
import math

class TestDodatak_A(unittest.TestCase):
    def test_perform_division(self):
        ops_manager = OperationsManager(5, 0)
        with self.assertRaises(ZeroDivisionError):
            rez = ops_manager.perform_division()

    def test_square_binomial(self):
        ops_manager = OperationsManager(3, 2)
        rez = ops_manager.square_binomial()
        true_rez = ops_manager.a ** 2 + 2 * ops_manager.a * ops_manager.b + ops_manager.b ** 2
        self.assertEqual(rez, true_rez)

    def test_pythagorean_rule(self):
        ops_manager = OperationsManager(3, 4)
        rez = ops_manager.pythagorean_rule()
        true_rez = ops_manager.a ** 2 + ops_manager.b ** 2
        self.assertEqual(rez, true_rez)

    def test_factorial_sum(self):
        ops_manager = OperationsManager(-3, -4)
        with self.assertRaises(Exception):
            ops_manager.factorial_sum()

    def test_circle_area(self):
        ops_manager = OperationsManager(-3, 5)
        rez = ops_manager.circle_area()
        self.assertEquals(rez, 0)


if __name__ == '__main__':
    unittest.main()

