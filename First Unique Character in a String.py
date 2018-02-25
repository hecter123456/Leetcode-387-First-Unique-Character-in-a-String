import unittest
import operator

class unitest(unittest.TestCase):
    def testNone(self):
        Input = ""
        Output = -1
        self.assertEqual(Solution().firstUniqChar(Input),Output)
    def testSample(self):
        Input = "loveleetcode"
        Output = 2
        self.assertEqual(Solution().firstUniqChar(Input),Output)

class Solution():
    def firstUniqChar(self, s):
        dic = {}
        for i in range(len(s)):
            char = s[i]
            if char in dic:
                dic[char] = -1
            else:
                dic[char] = i
        dic = sorted(dic.items(), key=lambda x: x[1])
        for key in dic:
            if key[1] != -1:
                return key[1]
        return -1

if __name__ == '__main__':
    unittest.main()
