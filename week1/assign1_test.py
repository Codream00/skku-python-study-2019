import unittest
import assignment1 as hw1


class Assign1Tests(unittest.TestCase): 
    #python의 내장함수 reversed를 써서 만든 것과 비교
    def test_func1(self):
        word = "abcdefghijklmn"
        rWord = ''.join(reversed(word))
        self.assertEqual(rWord, hw1.reverse1(word))
        
    def test_func2(self):
        word = "abcdefghijklmn"
        rWord = ''.join(reversed(word))
        self.assertEqual(rWord, hw1.reverse2(word))


# unittest 실행
if __name__ == '__main__':  
    unittest.main()
