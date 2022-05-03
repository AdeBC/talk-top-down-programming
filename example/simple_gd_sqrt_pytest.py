import unittest
import simple_gd_sqrt as sqrt_test


class TestgdSQRT(unittest.TestCase):

    def test_solve(self):
        y_current = sqrt_test.solve(x=10, y_expected=9, limit=0.01, steps=10**6, step_size=0.0001)
        self.assertTrue(abs(y_current - 3) < 0.01)
        y_current = sqrt_test.solve(x=1, y_expected=9, limit=0.01, steps=10**6, step_size=0.0001)
        self.assertTrue(abs(y_current - 3) < 0.01)

    def test_calculate_Y(self):
        self.assertEqual(sqrt_test.calculate_Y(x=3), 9)
        self.assertEqual(sqrt_test.calculate_Y(x=-3), 9)

    def test_update_X(self):
        updated_X = sqrt_test.update_X(y_expected=9, y_current=4, x=2, step_size=0.0001)
        self.assertEqual(updated_X, 2 + 2 * 2 * 0.0001)
        updated_X = sqrt_test.update_X(y_expected=9, y_current=16, x=4, step_size=0.0001)
        self.assertEqual(updated_X, 4 - 2 * 4 * 0.0001)

if __name__ == '__main__':
    unittest.main()

