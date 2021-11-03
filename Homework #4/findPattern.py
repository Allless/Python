def getPattern(word):
    return [[x for x in range(len(word)) if word[x] == letter] for letter in word]

def findAndReplacePattern(words, pattern):
    myPattern = getPattern(pattern)
    return [word for word in words if getPattern(word) == myPattern]
