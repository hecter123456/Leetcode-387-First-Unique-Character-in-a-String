import unittest

class unitest(unittest.TestCase):
    def testNone(self):
        Input = ""
        Output = -1
        self.assertEqual(Solution().firstUniqChar(Input),Output)

class Solution():
    def firstUniqChar(self, s):
        if s == "":
            return -1

if __name__ == '__main__':
    unittest.main()
