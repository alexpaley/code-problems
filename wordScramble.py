#The program should accept a string as input, and then return a list of words
#that can be created using the submitted letters.
#
#Example: Input: "dog", Output: ["god", "do", "go"]

def wordScramble(string):

    #Open/read wordList.txt for English dictionary
    wordList = open("./wordList.txt")

    #Remove new-line characters from end of lines
    dictionary = list(line.rstrip('\n') for line in wordList)

    #Store dictionary and all anagrams in hashtables for O(1) lookup
    dictionary_hash = {}
    anagram_hash    = {}

    for line in dictionary:
        dictionary_hash[line] = True

    def makeWord(word, remaining):
        anagram_hash[word] = word

        for i in range(remaining.__len__()):
            makeWord(word + remaining[i], remaining[0:i] + remaining[(i+1):])

    makeWord('', string)

    for word in anagram_hash:
        if anagram_hash[word] in dictionary_hash.keys():
            print word

wordScramble('dog')
