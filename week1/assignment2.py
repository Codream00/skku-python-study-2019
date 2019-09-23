#set의 교집합 기능을 이용했습니다.
def find_common_char1(word1,word2):
    intersection = list(set(word1)&set(word2))
    return intersection

#각 단어의 문자를 한번씩 읽어서 공통부분을 뽑을 수 있게 했습니다.
def find_common_char2(word1,word2):
    setOfWord1 = []
    common = []
    
    for c in word1:
        if c not in setOfWord1:
            setOfWord1.append(c)

    for c in word2:
        if c not in common and c in setOfWord1:
            common.append(c)
            
    return common

if __name__ == "__main__":
    word1 = input()
    word2 = input()
    print(find_common_char1(word1,word2))
    print(find_common_char2(word1,word2))
    
