#단어를 뒤에서부터 읽은 리스트를 새로 만들어 문자열로 변환했습니다.
def reverse1(word):
    rWord = [word[len(word)-1-i] for i in range(len(word))]
    rWord = ''.join(rWord)
    return rWord

#파이썬의 extended slices를 이용해 반환했습니다.
def reverse2(word):
    return word[::-1]

if __name__ == "__main__":
    word = input()
    print(reverse1(word))
    print(reverse2(word))
