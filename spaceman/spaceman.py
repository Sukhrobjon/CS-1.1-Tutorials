# 1. print greeting->done
# 2. print underscores equal to the number of letters of the word->done
# 3. Array check function and replace the underscore with found letters->

print('Lets play hangman game!')

def board(word):
    underScore = []
    i = 0
    while i < len(word):
        underScore.append('__')
        i += 1
    print(' '.join(underScore))
    return underScore

    
def checkWord(char, word):
    for c in word:
        if c == char:
            return True
    return False


def indexOfChar(char, word):
    indices = []
    for index, character in enumerate(word):
        if character == char:
            indices.insert(index, char)
            print(indices)
    
    return indices


# board("666666")
# game
word = "television"
counter = 0
while counter < 7:
    char = input("enter a char: ")
    board(word)
    if checkWord(char, word):
        print("found")
    else:
        print('not found')
    counter += 1  
