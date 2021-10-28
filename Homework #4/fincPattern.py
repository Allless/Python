def getPattern(words, pattern):
    newPattern = [[x for x in range(len(pattern)) if pattern[x] == letter] for letter in set(pattern)]
    return [word for word in words if [[x for x in range(len(word)) if word[x] == letter] for letter in set(word)] == newPattern]