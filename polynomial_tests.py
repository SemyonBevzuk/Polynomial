import unittest
from polynomial import Polynomial


class TestPolynomialInit(unittest.TestCase):
    def test_empty(self):
        correct_answer = (0, [0])
        p = Polynomial()
        answer = (p.degree(), p.coeffs)
        self.assertEqual(correct_answer, answer)

    def test_with_list(self):
        list_coefficients = [1, 2, 3]
        correct_answer = (2, list_coefficients)
        p = Polynomial(list_coefficients)
        answer = (p.degree(), p.coeffs)
        self.assertEqual(correct_answer, answer)

    def test_with_garbage_list(self):
        list_coefficients = [1, 'abc', 3.4]
        self.assertRaises(ValueError, Polynomial, list_coefficients)

    def test_with_tuple(self):
        tuple_coefficients = (1, 2, 3)
        correct_answer = (2, list(tuple_coefficients))
        p = Polynomial(tuple_coefficients)
        answer = (p.degree(), p.coeffs)
        self.assertEqual(correct_answer, answer)

    def test_with_garbage_tuple(self):
        tuple_coefficients = (1, 'abc', 3.4)
        self.assertRaises(ValueError, Polynomial, tuple_coefficients)

    def test_empty_typle(self):
        tuple_coefficients = ()
        correct_answer = (0, [0])
        p = Polynomial(tuple_coefficients)
        answer = (p.degree(), p.coeffs)
        self.assertEqual(correct_answer, answer)

    def test_empty_list(self):
        list_coefficients = []
        correct_answer = (0, [0])
        p = Polynomial(list_coefficients)
        answer = (p.degree(), p.coeffs)
        self.assertEqual(correct_answer, answer)

    def test_constant(self):
        list_coefficients = [1, ]
        correct_answer = (0, list_coefficients)
        p = Polynomial(list_coefficients)
        answer = (p.degree(), p.coeffs)
        self.assertEqual(correct_answer, answer)

    def test_second_degree(self):
        list_coefficients = [3, 2, 1]
        correct_answer = (2, list_coefficients)
        p = Polynomial(list_coefficients)
        answer = (p.degree(), p.coeffs)
        self.assertEqual(correct_answer, answer)

    def test_list_with_zeros(self):
        list_coefficients = [0, 0, 0]
        correct_answer = (0, [0])
        p = Polynomial(list_coefficients)
        answer = (p.degree(), p.coeffs)
        self.assertEqual(correct_answer, answer)

    def test_list_with_zeros_in_head(self):
        list_coefficients = [0, 0, 0, 1, 0, 0, 1]
        correct_answer = (3, [1, 0, 0, 1])
        p = Polynomial(list_coefficients)
        answer = (p.degree(), p.coeffs)
        self.assertEqual(correct_answer, answer)

    def test_invalid_argument_string(self):
        self.assertRaises(TypeError, Polynomial, 'abc')

    def test_invalid_argument_float(self):
        self.assertRaises(TypeError, Polynomial, 1.1)

    def test_polynomial_equal_coefficients(self):
        list_coefficients = [1, 2, 3]
        p1 = Polynomial(list_coefficients)
        p2 = Polynomial(p1)
        self.assertEqual(p1.coeffs, p2.coeffs)

    def test_polynomial_not_equal_lists_coefficients(self):
        list_coefficients = [3, 2, 1]
        p1 = Polynomial(list_coefficients)
        p2 = Polynomial(p1)
        self.assertIsNot(p1.coeffs, p2.coeffs)


class TestPolynomialStr(unittest.TestCase):
    def test_positive_full_polynomial_degree_3(self):
        correct_answer = '4x^3 + 3x^2 + 2x + 1'
        p = Polynomial([4, 3, 2, 1])
        answer = str(p)
        self.assertEqual(correct_answer, answer)

    def test_negative_full_polynomial_degree_3(self):
        correct_answer = '- 4x^3 - 3x^2 - 2x - 1'
        p = Polynomial([-4, -3, -2, -1])
        answer = str(p)
        self.assertEqual(correct_answer, answer)

    def test_mixed_full_polynomial_degree_3(self):
        correct_answer = '- 4x^3 + 3x^2 + x - 1'
        p = Polynomial([-4, 3, 1, -1])
        answer = str(p)
        self.assertEqual(correct_answer, answer)

    def test_mixed_not_full_polynomial_degree_3(self):
        correct_answer = '- x^3 - 2x + 1'
        p = Polynomial([-1, 0, -2, 1])
        answer = str(p)
        self.assertEqual(correct_answer, answer)

    def test_negative_full_polynomial_degree_0(self):
        correct_answer = '- 10'
        p = Polynomial([-10])
        answer = str(p)
        self.assertEqual(correct_answer, answer)

    def test_mixed_not_full_polynomial_degree_1(self):
        correct_answer = '- 10x'
        p = Polynomial([-10, 0])
        answer = str(p)
        self.assertEqual(correct_answer, answer)

    def test_empty_polynomial(self):
        correct_answer = '0'
        p = Polynomial()
        answer = str(p)
        self.assertEqual(correct_answer, answer)


class TestPolynomialRepr(unittest.TestCase):
    def test_positive_full_polynomial_degree_3(self):
        correct_answer = 'Polynomial([4, 3, 2, 1])'
        p = Polynomial([4, 3, 2, 1])
        answer = repr(p)
        self.assertEqual(correct_answer, answer)


class TestPolynomialCall(unittest.TestCase):
    def test_call_int_polynomial_degree_3(self):
        correct_answer = 4
        p = Polynomial([1, 1, 1, 1])
        answer = p(1)
        self.assertEqual(correct_answer, answer)

    def test_call_int_polynomial_degree_0(self):
        correct_answer = 10
        p = Polynomial([10])
        answer = p(1)
        self.assertEqual(correct_answer, answer)

    def test_call_float_polynomial_degree_1(self):
        correct_answer = 6.0
        p = Polynomial([2, 1])
        answer = p(2.5)
        self.assertEqual(correct_answer, answer)

    def test_invalid_argument(self):
        p = Polynomial([1, 2, 3])
        self.assertRaises(TypeError, p, 'abc')


class TestPolynomialIter(unittest.TestCase):
    def test_full_polynomial_degree_3(self):
        correct_answer = '4 3 2 1 '
        p = Polynomial([4, 3, 2, 1])
        answer = ''
        for a in p:
            answer += '{} '.format(a)
        self.assertEqual(correct_answer, answer)

    def test_not_full_polynomial_degree_3(self):
        correct_answer = '4 0 0 1 '
        p = Polynomial([4, 0, 0, 1])
        answer = ''
        for a in p:
            answer += '{} '.format(a)
        self.assertEqual(correct_answer, answer)


class TestPolynomialGetitem(unittest.TestCase):
    def test_get_existing_element(self):
        correct_answer = 3
        p = Polynomial([4, 3, 2, 1])
        answer = p[2]
        self.assertEqual(correct_answer, answer)

    def test_get_not_existing_element(self):
        correct_answer = 0
        p = Polynomial([4, 3, 2, 1])
        answer = p[10]
        self.assertEqual(correct_answer, answer)

    def test_invalid_argument_less_0(self):
        p = Polynomial([1, 2, 3])
        self.assertRaises(ValueError, p.__getitem__, -1)

    def test_invalid_argument(self):
        p = Polynomial([1, 2, 3])
        self.assertRaises(TypeError, p.__getitem__, 'abc')


class TestPolynomialSetitem(unittest.TestCase):
    def test_set_element_less_degree(self):
        correct_p = Polynomial([4, 2, 1])
        p = Polynomial([3, 2, 1])
        p[2] = 4
        self.assertEqual(correct_p, p)

    def test_set_element_more_degree(self):
        correct_p = Polynomial([4, 3, 2, 1])
        p = Polynomial([3, 2, 1])
        p[3] = 4
        self.assertEqual(correct_p, p)

    def test_set_element_more_more_degree(self):
        correct_p = Polynomial([6, 0, 0, 3, 2, 1])
        p = Polynomial([3, 2, 1])
        p[5] = 6
        self.assertEqual(correct_p, p)

    def test_set_zero_element_in_max_degree(self):
        correct_p = Polynomial([3, 2, 1])
        p = Polynomial([6, 0, 0, 3, 2, 1])
        p[5] = 0
        self.assertEqual(correct_p, p)

    def test_invalid_argument_less_0(self):
        p = Polynomial([1, 2, 3])
        self.assertRaises(ValueError, p.__setitem__, -1, 4)

    def test_invalid_argument_degree_not_int(self):
        p = Polynomial([1, 2, 3])
        self.assertRaises(TypeError, p.__setitem__, 0.1, 4)

    def test_invalid_argument_value_not_int(self):
        p = Polynomial([1, 2, 3])
        self.assertRaises(TypeError, p.__setitem__, 3, 0.1)


class TestPolynomialGetattr(unittest.TestCase):
    def test_correct_attribute(self):
        list_coefficients = [4, 3, 2, 1]
        p = Polynomial(list_coefficients)
        self.assertEqual(list_coefficients, p.coeffs)
        AttributeError

    def test_incorrect_attribute(self):
        p = Polynomial([4, 3, 2, 1])
        self.assertRaises(AttributeError, p.__getattr__, 'abc')


class TestPolynomialSetattr(unittest.TestCase):
    def test_correct_all(self):
        list_coefficients = [4, 3, 2, 1]
        p = Polynomial()
        p.coeffs = list_coefficients
        self.assertEqual(list_coefficients, p.coeffs)

    def test_incorrect_attribute(self):
        p = Polynomial([4, 3, 2, 1])
        self.assertRaises(AttributeError, p.__setattr__, 'not_coeffs', [1, 2, 3])

    def test_incorrect_type(self):
        p = Polynomial([4, 3, 2, 1])
        self.assertRaises(TypeError, p.__setattr__, 'coeffs', 123)

    def test_incorrect_value(self):
        p = Polynomial([4, 3, 2, 1])
        self.assertRaises(ValueError, p.__setattr__, 'coeffs', [4, 'abc', []])


class TestPolynomialEq(unittest.TestCase):
    def test_equal_polynomial(self):
        list_coefficients = [4, 3, 2, 1]
        p1 = Polynomial(list_coefficients)
        p2 = Polynomial(list_coefficients)
        self.assertTrue(p1 == p2)

    def test_not_equal_polynomial(self):
        p1 = Polynomial([1, 2, 3, 4])
        p2 = Polynomial([4, 3, 2, 1])
        self.assertFalse(p1 == p2)

    def test_not_equal_polynomial_with_different_length(self):
        p1 = Polynomial([1, 2, 3, 4])
        p2 = Polynomial([3, 2, 1])
        self.assertFalse(p1 == p2)

    def test_invalid_argument(self):
        p = Polynomial([1, 2, 3])
        self.assertRaises(TypeError, p.__eq__, 'abc')


class TestPolynomialNe(unittest.TestCase):
    def test_equal_polynomial(self):
        list_coefficients = [4, 3, 2, 1]
        p1 = Polynomial(list_coefficients)
        p2 = Polynomial(list_coefficients)
        self.assertFalse(p1 != p2)

    def test_not_equal_polynomial(self):
        p1 = Polynomial([1, 2, 3, 4])
        p2 = Polynomial([4, 3, 2, 1])
        self.assertTrue(p1 != p2)

    def test_not_equal_polynomial_with_different_length(self):
        p1 = Polynomial([1, 2, 3, 4])
        p2 = Polynomial([3, 2, 1])
        self.assertTrue(p2 != p1)


class TestPolynomialNeg(unittest.TestCase):
    def test_created_new_polynomial(self):
        p1 = Polynomial([4, -3, -2, 1])
        p2 = -p1
        self.assertIsNot(p1.coeffs, p2.coeffs)

    def test_coefficients_changed_correctly(self):
        p1 = Polynomial([4, -3, -2, 1])
        p2 = -p1
        self.assertEqual([-4, 3, 2, -1], p2.coeffs)


class TestPolynomialPos(unittest.TestCase):
    def test_not_created_new_polynomial(self):
        p1 = Polynomial([4, -3, -2, 1])
        p2 = +p1
        self.assertIs(p1.coeffs, p2.coeffs)

    def test_coefficients_changed_correctly(self):
        p1 = Polynomial([4, -3, -2, 1])
        p2 = +p1
        self.assertEqual([4, -3, -2, 1], p2.coeffs)


class TestPolynomialZipTwoPolynomial(unittest.TestCase):
    def test_polynomial_equal_length(self):
        p1 = Polynomial([-1, 2, -3, 4])
        p2 = Polynomial([4, -3, 2, -1])
        correct_answer = '(-1, 4) (2, -3) (-3, 2) (4, -1) '
        answer = ''
        for elem in Polynomial.zip_two_polynomial(p1, p2):
            answer += '{} '.format(elem)
        self.assertEqual(correct_answer, answer)

    def test_polynomial_not_equal_length_1(self):
        p1 = Polynomial([1, 2, 3, 4])
        p2 = Polynomial([2, 1])
        correct_answer = '(1, 0) (2, 0) (3, 2) (4, 1) '
        answer = ''
        for elem in Polynomial.zip_two_polynomial(p1, p2):
            answer += '{} '.format(elem)
        self.assertEqual(correct_answer, answer)

    def test_polynomial_not_equal_length_2(self):
        p1 = Polynomial([2, 1])
        p2 = Polynomial([1, 2, 3, 4])
        correct_answer = '(1, 0) (2, 0) (3, 2) (4, 1) '
        answer = ''
        for elem in Polynomial.zip_two_polynomial(p1, p2):
            answer += '{} '.format(elem)
        self.assertEqual(correct_answer, answer)


class TestPolynomialAdd(unittest.TestCase):
    def test_equal_polynomial(self):
        correct_answer = Polynomial([2, 2, 2, 2])
        p1 = Polynomial([1, 1, 1, 1])
        p2 = Polynomial([1, 1, 1, 1])
        answer = p1 + p2
        self.assertEqual(correct_answer, answer)

    def test_not_equal_polynomial(self):
        correct_answer = Polynomial([1, 1, 2, 2])
        p1 = Polynomial([1, 1, 1, 1])
        p2 = Polynomial([1, 1])
        answer = p1 + p2
        self.assertEqual(correct_answer, answer)

    def test_sum_equal_zero(self):
        correct_answer = Polynomial([0])
        p1 = Polynomial([-1, -1])
        p2 = Polynomial([1, 1])
        answer = p1 + p2
        self.assertEqual(correct_answer, answer)

    def test_const(self):
        correct_answer = Polynomial([1, 2])
        p1 = Polynomial([1, 1])
        answer = p1 + 1
        self.assertEqual(correct_answer, answer)

    def test_invalid_argument(self):
        p = Polynomial([1, 2, 3])
        self.assertRaises(TypeError, p.__add__, 'abc')


class TestPolynomialRadd(unittest.TestCase):
    def test_const(self):
        correct_answer = Polynomial([1, 2])
        p1 = Polynomial([1, 1])
        answer = 1 + p1
        self.assertEqual(correct_answer, answer)

    def test_invalid_argument(self):
        p = Polynomial([1, 2, 3])
        self.assertRaises(TypeError, p.__radd__, 'abc')


class TestPolynomialSub(unittest.TestCase):
    def test_equal_polynomial(self):
        correct_answer = Polynomial([2, -2, -2, 2])
        p1 = Polynomial([3, -3, -3, 3])
        p2 = Polynomial([1, -1, -1, 1])
        answer = p1 - p2
        self.assertEqual(correct_answer, answer)

    def test_not_equal_polynomial(self):
        correct_answer = Polynomial([1, 1, 1, 0])
        p1 = Polynomial([1, 1, 2, 1])
        p2 = Polynomial([1, 1])
        answer = p1 - p2
        self.assertEqual(correct_answer, answer)

    def test_sub_equal_zero(self):
        correct_answer = Polynomial([0])
        p1 = Polynomial([1, 1])
        p2 = Polynomial([1, 1])
        answer = p1 - p2
        self.assertEqual(correct_answer, answer)

    def test_const(self):
        correct_answer = Polynomial([1, 0])
        p1 = Polynomial([1, 1])
        answer = p1 - 1
        self.assertEqual(correct_answer, answer)

    def test_invalid_argument(self):
        p = Polynomial([1, 2, 3])
        self.assertRaises(TypeError, p.__sub__, 2.3)


class TestPolynomialRsub(unittest.TestCase):
    def test_const(self):
        correct_answer = Polynomial([1, 0])
        p1 = Polynomial([1, 1])
        answer = 1 - p1
        self.assertEqual(correct_answer, answer)

    def test_invalid_argument(self):
        p = Polynomial([1, 2, 3])
        self.assertRaises(TypeError, p.__rsub__, {})


class TestPolynomialMul(unittest.TestCase):
    def test_equal_polynomial(self):
        correct_answer = Polynomial([1, 2, 1])
        p1 = Polynomial([1, 1])
        p2 = Polynomial([1, 1])
        answer = p1 * p2
        self.assertEqual(correct_answer, answer)

    def test_polynomial(self):
        correct_answer = Polynomial([-1, 6, -11, 12])
        p1 = Polynomial([1, -2, 3])
        p2 = Polynomial([-1, 4])
        answer = p1 * p2
        self.assertEqual(correct_answer, answer)

    def test_zeroing_polynomial(self):
        correct_answer = Polynomial([1, 0, 2, 0, 0, 0])
        p1 = Polynomial([1, 0, 0, 0])
        p2 = Polynomial([1, 0, 2])
        answer = p1 * p2
        self.assertEqual(correct_answer, answer)

    def test_empty_polynomial(self):
        correct_answer = Polynomial([0])
        p1 = Polynomial()
        p2 = Polynomial([-1, 6, -11, 12])
        answer = p1 * p2
        self.assertEqual(correct_answer, answer)

    def test_const_zero(self):
        correct_answer = Polynomial([0])
        p1 = Polynomial([1, 1])
        answer = p1 * 0
        self.assertEqual(correct_answer, answer)

    def test_const(self):
        correct_answer = Polynomial([3, 0, 6])
        p1 = Polynomial([1, 0, 2])
        answer = p1 * 3
        self.assertEqual(correct_answer, answer)

    def test_invalid_argument(self):
        p = Polynomial([1, 2, 3])
        self.assertRaises(TypeError, p.__mul__, 2.3)


class TestPolynomialRmul(unittest.TestCase):
    def test_const_zero(self):
        correct_answer = Polynomial([0])
        p1 = Polynomial([1, 1])
        answer = 0 * p1
        self.assertEqual(correct_answer, answer)

    def test_const(self):
        correct_answer = Polynomial([3, 0, 6])
        p1 = Polynomial([1, 0, 2])
        answer = 3 * p1
        self.assertEqual(correct_answer, answer)

    def test_invalid_argument(self):
        p = Polynomial([1, 2, 3])
        self.assertRaises(TypeError, p.__rmul__, 'abc')


if __name__ == '__main__':
    unittest.main()
