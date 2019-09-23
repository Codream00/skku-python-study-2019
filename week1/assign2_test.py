import unittest
import assignment2 as hw2


class Assign2Tests(unittest.TestCase):

    #공통 문자가 word1과 word2에 모두 속하는지 확인합니다.
    def test_func1(self):
        result = True
        word1 = "abcde"
        word2 = "knaknb"
        common = hw2.find_common_char1(word1,word2)

        for c in common:
            if((c in word1 and c in word2)==False):
                result = False

        self.assertTrue(result)

    def test_func2(self):
        result = True
        word1 = "abcde"
        word2 = "knaknb"
        common = hw2.find_common_char2(word1,word2)

        for c in common:
            if((c in word1 and c in word2)==False):
                result = False

        self.assertTrue(result)
        
if __name__ == '__main__':  
    unittest.main()
