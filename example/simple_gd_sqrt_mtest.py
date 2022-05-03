import simple_gd_sqrt as sqrt_test


# Test calculate_Y
assert sqrt_test.calculate_Y(x=3) == 9
assert sqrt_test.calculate_Y(x=-3) == 9


# Test update_X
updated_X = sqrt_test.update_X(y_expected=9, y_current=4, x=2, step_size=0.0001)
assert updated_X == 2 + 2 * 2 * 0.0001
updated_X = sqrt_test.update_X(y_expected=9, y_current=16, x=4, step_size=0.0001)
assert updated_X == 4 - 2 * 4 * 0.0001


# Test solve
y_current = sqrt_test.solve(x=10, y_expected=9, limit=0.01, step_size=0.0001)
assert abs(y_current - 3) < 0.01
y_current = sqrt_test.solve(x=1, y_expected=9, limit=0.01, step_size=0.0001)
assert abs(y_current - 3) < 0.01