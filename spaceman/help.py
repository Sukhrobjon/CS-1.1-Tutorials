'''
def checkWord(char, word):
    for c in word:
        if c == char:
            return True
    return False

print(checkWord('c', 'hello there'))
print(checkWord('l', 'hello there'))

def indexOfChar(char, word):
        indices = []
        for index, character in enumerate(word):
            if character == char:
                indices.append(index)
        return indices

 

print(indexOfChar('o', 'hello'))
'''


def board(word):
    underScore = []
    i = 0
    while i < len(word):
        underScore.append('__')
        i += 1
    print(' '.join(underScore))
    return underScore


underScore = ['__', '__', '__', '__', '__', '__']
print(underScore)
underScore.pop(0)
underScore.insert(0, 'q')
print(underScore)
