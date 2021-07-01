"""
This program asks the user for paths to a .txt file and .csv file,
and prints the evaluation, potency, and activity (EPA) levels for the text.
This program also prints the number of adjectives, number of adverbs,
and count of each unique word in the text.
"""

# Created By: Romi Lifshitz

import nltk
nltk.download('brown')
nltk.download('universal_tagset')

"""
Importing the necessary NLTK libraries and modules.
"""
from nltk.tag import StanfordPOSTagger
from nltk.corpus import wordnet
from nltk import pos_tag, word_tokenize
from nltk.corpus import words
from nltk.tokenize import word_tokenize


"""
To identify the part-of-speech of the words retrieved from
Word2vec, we used the conditional frequency feature of the NLTK module
which returns a frequency-ordered list of the possible parts of speech associated
with all of the English words that are found in the Brown Corpus. Our sys-
tem uses the Brown Corpus to generate the frequency-ordered list because
of the fact that the words contained in the Brown Corpus are annotated with
part-of-speech tags.
"""
wordtags = nltk.ConditionalFreqDist((w.lower(), t)
                                    for w, t in nltk.corpus.brown.tagged_words(tagset="universal"))


def findPOS(word):
    """
    This is a function that accepts a word (str) as its parameter and returns the part-of-speech of the word (str).
    The function considers adjectives, adverbs and nouns.
    """
    lisPOS = list(wordtags[word])
    if "ADJ" in lisPOS:
        return "ADJECTIVE"
    if "ADV" in lisPOS:
        return "ADVERB"
    if "NN" in lisPOS:
        return "NOUN"


def readFile(filename):
    """
    This is a function that accepts a path to a .txt file as its parameter, reads in the file text, and returns the
    text (str) filtered to contain only letters and white spaces.
    """
    speechFile = open(filename, "r")
    speech = speechFile.read()
    speechFile.close()
    # Filters speech to contain only letters and white spaces
    speechFiltered = filterSpeech(speech)
    return speechFiltered


def filterSpeech(speech):
    """
    This is a function that accepts a string (i.e. read from a text document) as its parameter and returns the string,
    filtered to contain only letters and white spaces (no other character types).
    """
    speechFiltered = ""
    for char in speech:
        # str.isalpha() returns True if str is a letter
        if char.isalpha() or char == " ":
            speechFiltered += char
    return speechFiltered


def getWords(speechFiltered):
    """
    This is a function that segments the words in a document. It accepts a string (should contain only letters and white
    spaces) and returns a list of the words in the string.
    """
    return speechFiltered.split()



def prepareSemanticDifferential(txtFilePath):
    """
    This is a function that reads in the EPA values from the Osgood wordlist (.csv file) and stores
    the values in a Python dictionary. It accepts a path to the .csv file (str) as its parameter and
    returns a list of dictionaries, where each dictionary contains the word and its EPA values.
    """
    fileIn = open(txtFilePath, 'r')
    allData = []
    line = fileIn.readline()
    while line != "":
        line = fileIn.readline().strip()
        if line != "":
            values = line.split(',')
            wordData = {}
            wordData['word'] = str(values[0])
            wordData['evaluation'] = float(values[1])
            wordData['activity'] = float(values[2])
            wordData['potency'] = float(values[3])
            # The dictionary entries of allData are formatted:
            # {'potency':value,'activity':value,'evaluation':value,'word':value}
            allData.append(wordData)
    fileIn.close()
    return allData


def calculateSD(txtFilePath, csvFilePath):
    """
    This is a function that calculates the evaluation, activity, and potency levels of a text document (.txt file),
    considering only adverbs and adjectives within the .txt file. It takes in a path to a .txt file (str) and a path to a
    .csv file (str) as its parameters and prints the EPA levels of the text.
    """
    speechFiltered = readFile(txtFilePath)  # speechFiltered contain only letters and whitespaces
    speechWords = getWords(speechFiltered)
    allData = prepareSemanticDifferential(csvFilePath)  # allData is a list of dictionaries

    evaluationSum = 0
    activitySum = 0
    potencySum = 0

    # Determine POS of each speechWord in speechWords. If speechWord is an adjective or adverb, add its EPA values
    # (extracted from corresponding wordEPA dictionary in allData) to the running EPA sums.
    for speechWord in speechWords:
        pos = findPOS(speechWord)
        if pos == "ADJECTIVE" or pos == "ADVERB":
            # Find dictionary in allData corresponding to current speechWord and add its
            # EPA values to the running EPA sums.
            for wordEPA in allData:
                if wordEPA['word'] == speechWord:
                    evaluationSum += wordEPA['evaluation']
                    activitySum += wordEPA['activity']
                    potencySum += wordEPA['potency']
    print("Evaluation Score: " + str(round(evaluationSum, 2)))
    print("Activity Score: " + str(round(activitySum, 2)))
    print("Potency Score: " + str(round(potencySum, 2)))


def countAdjectives(txtFilePath):
    """
    This is a function that counts the number of adjectives in a .txt file. The function accepts a path to a
    .txt file (str) as its parameter and returns the adjective count (int) of the .txt file.
    """
    speechFiltered = readFile(txtFilePath)
    speechWords = getWords(speechFiltered)

    numAdjectives = 0
    # Determine POS of each speechWord in speechWords. If speechWord is an adjective, increase numAdjectives by one.
    for speechWord in speechWords:
        pos = findPOS(speechWord)
        if pos == "ADJECTIVE":
            numAdjectives += 1
    return numAdjectives


def countAdverbs(txtFilePath):
    """
    This is a function that counts the number of adverbs in a .txt file. The function accepts a path to a
    .txt file (str) as its parameter and returns the adverb count (int) of the .txt file.
    """
    speechFiltered = readFile(txtFilePath)
    speechWords = getWords(speechFiltered)

    numAdverbs = 0
    # Determine POS of each speechWord in speechWords. If speechWord is an adverb, increase numAdverbs by one.
    for speechWord in speechWords:
        pos = findPOS(speechWord)
        if pos == "ADVERB":
            numAdverbs += 1
    return numAdverbs


def getUniqueWords(txtFilePath):
    """
    This is a function that creates a list of the unique words in a .txt file. The function accepts a path to a
    .txt file (str) as its parameter and returns the subset of unique words (list) in the .txt file.
    """
    speechFiltered = readFile(txtFilePath)
    speechWords = getWords(speechFiltered)

    uniqueWords = []
    for word in speechWords:
        word = word.lower()  # ensures that getUniqueWords() is case in-sensitive
        if word not in uniqueWords:
            uniqueWords.append(word)
    uniqueWords.sort()  # sort elements of uniqueWords in alphabetical order
    return uniqueWords


def countWords(txtFilePath):
    """
    This is a function that counts the number of times each unique word is used in a .txt file (case in-sensitive).
    The function accepts a path to a .txt file (str) as its parameter and returns a dictionary where each key is a
    unique word in the .txt file and each value is the number of occurrences of that word in the .txt file.
    """
    speechFiltered = readFile(txtFilePath)
    speechWords = getWords(speechFiltered)

    uniqueWords = getUniqueWords(txtFilePath)  # Generate list of unique words in .txt document

    dictWordOccurrences = {}
    # Create key-value pair in dictWordOccurrences for each uniqueWord in uniqueWords
    # (key=uniqueWord, value=occurrence count for word).
    for uniqueWord in uniqueWords:
        dictWordOccurrences.update({uniqueWord: 0})
        # Add 1 to dictWordOccurrences[uniqueWord] at each occurrence of uniqueWord in speechWords.
        for speechWord in speechWords:
            speechWord = speechWord.lower()
            if speechWord == uniqueWord:
                dictWordOccurrences[uniqueWord] += 1
    return dictWordOccurrences


def main():
    """
    The top-level function: gets the paths (str) to the .txt file and .csv file from the user (via input() function) and
    prints the overall evaluation, potency, and activity (EPA) levels for the .txt file (considering only adjectives and
    adverbs). This function also prints the adjective count, adverb count, and unique word count of the .txt file.
    """
    print("Hello, this is a program that calculates the EPA values, adjective count, adverb count, "
          "and unique word count for a .txt file.")
    txtFilePath = input("To begin, please input the path of the .txt file you would like to calculate EPA values for:\n")
    csvFilePath = input("Thank you. Now, please input the path to the OsgoodOriginal.csv file:\n")

    # PART A: Calculate and print the overall EPA values for the .txt file (at txtFilePath)
    calculateSD(txtFilePath, csvFilePath)

    # PART B: Count and print the number of adjectives, adverbs, and unique words in the .txt file (at txtFilePath)
    adjectives = countAdjectives(txtFilePath)
    adverbs = countAdverbs(txtFilePath)
    uniqueCount = countWords(txtFilePath)
    print("Adjective Count: " + str(adjectives))
    print("Adverb Count: " + str(adverbs))
    print("Unique Word Count: " + str(uniqueCount))

main()