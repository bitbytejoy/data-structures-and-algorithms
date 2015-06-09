import unittest

def sum_list(numbers_list):
    if len(numbers_list) == 0:
        return 0
    return numbers_list[0] + sum_list(numbers_list[1:])

class ListSumTest(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(0, sum_list([]))
    def test_one_element_list(self):
        self.assertEqual(1, sum_list([1]))
    def test_multiple_elements_list(self):
        self.assertEqual(10, sum_list([1, 2, 3, 4]))

def int_to_base(integer, base):
    if integer < 0:
        raise NegativeNumberError()
    if base < 2 or base > 16:
        raise UnsupportedBaseError()
    if integer < base:
        return "0123456789ABCDEF"[integer % base]
    return int_to_base(integer//base, base) + "0123456789ABCDEF"[integer % base]

class NegativeNumberError(Exception):
    pass

class UnsupportedBaseError(Exception):
    pass

class IntToBaseTest(unittest.TestCase):
    def test_unsupported_base(self):
        with self.assertRaises(UnsupportedBaseError):
            int_to_base(1, 1)
        with self.assertRaises(UnsupportedBaseError):
            int_to_base(1, 17)
        with self.assertRaises(UnsupportedBaseError):
            int_to_base(1, 20)
        with self.assertRaises(UnsupportedBaseError):
            int_to_base(1, -5)
    def test_number_negative(self):
        with self.assertRaises(NegativeNumberError):
            int_to_base(-1, 2)
    def test_number_zero(self):
        self.assertEqual("0", int_to_base(0, 2))
        self.assertEqual("0", int_to_base(0, 8))
        self.assertEqual("0", int_to_base(0, 16))
    def test_number_one(self):
        self.assertEqual("1", int_to_base(1, 2))
        self.assertEqual("1", int_to_base(1, 8))
        self.assertEqual("1", int_to_base(1, 16))
    def test_number_two(self):
        self.assertEqual("10", int_to_base(2, 2))
        self.assertEqual("2", int_to_base(2, 8))
        self.assertEqual("2", int_to_base(2, 16))
    def test_number_three(self):
        self.assertEqual("11", int_to_base(3, 2))
        self.assertEqual("3", int_to_base(3, 8))
        self.assertEqual("3", int_to_base(3, 16))
    def test_number_four(self):
        self.assertEqual("100", int_to_base(4, 2))
        self.assertEqual("4", int_to_base(4, 8))
        self.assertEqual("4", int_to_base(4, 16))
    def test_number_eight(self):
        self.assertEqual("1000", int_to_base(8, 2))
        self.assertEqual("10", int_to_base(8, 8))
        self.assertEqual("8", int_to_base(8, 16))
    def test_number_sixteen(self):
        self.assertEqual("10000", int_to_base(16, 2))
        self.assertEqual("20", int_to_base(16, 8))
        self.assertEqual("10", int_to_base(16, 16))
    def test_number_twenty(self):
        self.assertEqual("10100", int_to_base(20, 2))
        self.assertEqual("24", int_to_base(20, 8))
        self.assertEqual("14", int_to_base(20, 16))

if __name__ == "__main__":
    unittest.main()
