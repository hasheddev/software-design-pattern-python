import unittest

class CombinationLock:
    def __init__(self, combination):
        self.status = 'LOCKED'
        self.combination = combination
        self.combination_length = len(combination)
        self.input_count = 0
        
    def reset(self):
        self.status = 'LOCKED'
        self.input_count = 0

    def enter_digit(self, digit):
        if self.status == "OPEN":
            return
        elif self.status == "LOCKED":
            self.status = str(digit)
        else:
            self.status += str(digit)
        self.input_count += 1

        if self.input_count == self.combination_length:
            success = self.status == "".join([str(digit) for digit in self.combination])
            self.status = "ERROR" if not success else "OPEN"


class FirstTestSuite(unittest.TestCase):
    def test_success(self):
        cl = CombinationLock([1, 2, 3, 4, 5])
        self.assertEqual('LOCKED', cl.status)
        cl.enter_digit(1)
        self.assertEqual('1', cl.status)
        cl.enter_digit(2)
        self.assertEqual('12', cl.status)
        cl.enter_digit(3)
        self.assertEqual('123', cl.status)
        cl.enter_digit(4)
        self.assertEqual('1234', cl.status)
        cl.enter_digit(5)
        self.assertEqual('OPEN', cl.status)

    def test_failure(self):
        cl = CombinationLock([1, 2, 3])
        self.assertEqual('LOCKED', cl.status)
        cl.enter_digit(1)
        self.assertEqual('1', cl.status)
        cl.enter_digit(2)
        self.assertEqual('12', cl.status)
        cl.enter_digit(5)
        self.assertEqual('ERROR', cl.status)

if __name__ == "__main__":
    unittest.main()