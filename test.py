import unittest
from martian_sort import martian_sort
import random

tests = (
    ((['oq', 'fk', 'al', 'wr', 'id', 'cv', 'ar', 'aa', 'fp', 'xd'], [0, 1]), ['aa', 'al', 'ar', 'cv', 'fk', 'fp', 'id', 'oq', 'wr', 'xd']),
    (
        (
            ['bet', 'big', 'bit', 'rag', 'bar', 'bat', 'rat', 'beg', 'bag'],
            [0, 2, 1]
        ),
        ['bag', 'beg', 'big', 'bar', 'bat', 'bet', 'bit', 'rag', 'rat']
    ),
    (
        (
            ['bet', 'big', 'bit', 'rag', 'bar', 'bat', 'rat', 'beg', 'bag'],
            [0, 1, 2]
        ),
        ['bag', 'bar', 'bat', 'beg', 'bet', 'big', 'bit', 'rag', 'rat']
    ),
    (
        (
            ['bet', 'big', 'bit', 'rag', 'bar', 'bat', 'rat', 'beg', 'bag'],
            [2, 1, 0]
        ),
        ['bag', 'rag', 'beg', 'big', 'bar', 'bat', 'rat', 'bet', 'bit']
    ),
    ((['wpeim', 'caqyo', 'qpoqh', 'lwmbp', 'cdzbz', 'swlen', 'ealml', 'pxxee', 'ybriw', 'tgqhp', 'neybg', 'qpbee', 'bhosf', 'scbxx', 'wliqe', 'lqfuf', 'zdapi', 'hoxci', 'wykvf', 'ifqlr', 'ioght', 'agryq', 'sdmki', 'jvxcr', 'ywowc', 'xczls', 'nbned', 'yvlzn', 'wnxfc', 'jixak'], [3, 2, 4, 1, 0]), ['jixak', 'lwmbp', 'neybg', 'cdzbz', 'hoxci', 'jvxcr', 'qpbee', 'swlen', 'nbned', 'pxxee', 'wnxfc', 'ioght', 'tgqhp', 'wpeim', 'ybriw', 'sdmki', 'ifqlr', 'xczls', 'ealml', 'zdapi', 'wliqe', 'qpoqh', 'bhosf', 'lqfuf', 'wykvf', 'ywowc', 'scbxx', 'caqyo', 'agryq', 'yvlzn']),
)


def check(test):
    args, staff_sol = test
    student_sol = martian_sort(*args)
    print(staff_sol)
    print(student_sol)
    return staff_sol == student_sol


class TestCases(unittest.TestCase):
    def test_01(self):
        self.assertTrue(check(tests[0]))

    def test_02(self):
        self.assertTrue(check(tests[1]))

    def test_03(self):
        self.assertTrue(check(tests[2]))

    def test_04(self):
        self.assertTrue(check(tests[3]))

    def test_05(self):
        self.assertTrue(check(tests[4]))


if __name__ == "__main__":
    res = unittest.main(verbosity=3, exit=False)
