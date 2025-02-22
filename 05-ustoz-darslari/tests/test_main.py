# import pytest
# from src.main import func, Login, find_sum
#
#
# def test_main():
#     assert 1 == 1
#
#
# def test_func():
#     assert func(2) == 3
#
#
# def test_class_it():
#     assert Login.logic_param == 10
#
#
# def test_sum_success():
#     x, y = 1, 2
#     result = 3
#     assert find_sum(x, y) == result
#
#
# def test_sum_fail():
#     y = 2
#     x = '1'
#     pytest.raises(TypeError, find_sum, x, y)
#
#
# def test_sum_negative_numbers():
#     a = -1
#     b = 2/3
#     result = a + b
#     assert find_sum(a, b) == result
#     # pytest.raises(TypeError, find_sum, a, b)
#
#
# def test_sum_with_list():
#     a = 0
#     b = [3, 5]
#     pytest.raises(TypeError, find_sum, a, b)
#
#
# def test_sum_large_numbers():
#     assert find_sum(1000000, 2000000) == 3000000
#
#
# @pytest.mark.parametrize(
#     "num1, num2, expected",
#     [
#         (1,1,2),
#         # (1, '1', TypeError)
#     ]
# )
# def test_find_sum(num1, num2, expected):
#     assert find_sum(num1, num2) == expected
