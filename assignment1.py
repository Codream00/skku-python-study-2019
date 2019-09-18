word = input()
word2 = [word[len(word)-1-i] for i in range(len(word))]
word2 = ''.join(word2)
print(word2)
