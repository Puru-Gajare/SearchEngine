from collections import defaultdict

# Runtime Complexity: O(N) where n is # of characters in file
# since as n grows, the amount of time our program will take in
# the worst-case will grow linearly, as we are iterating through
# each character in the file one time
def tokenize(inputString):
    '''
    returns a list of all alphanumeric words in the inputted text file
    '''

    result = []
    currentWord = ""

    i = 0
    while i < len(inputString):
        char = inputString[i]             # get character from file

        if not char:            # if character doesn't exist, break loop
            break

        # if current character is alphanumeric, then add
        if char.isalnum() and ord(char) <= 127:
            currentWord += char.lower()

        # if current character is not alphanumeric, reset
        else:
            if currentWord != "":
                result.append(currentWord)
            currentWord = ""

        i += 1

    # add last word if it exists
    if currentWord != "":
        result.append(currentWord)

    return result


def compute_word_frequencies(tokens) -> defaultdict:
    frequencies = defaultdict(int)
    for token in tokens:
        frequencies[token] += 1
    return frequencies