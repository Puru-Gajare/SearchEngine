from tokenizer import tokenize
from bs4 import BeautifulSoup
import os
from bs4 import BeautifulSoup
from collections import defaultdict
from tokenizer import *
import posting
import shelve
import json
from posting import Posting
from posting import ListOfPostings
from nltk.stem import PorterStemmer
from nltk.stem import SnowballStemmer
from nltk.tokenize import word_tokenize
from nltk.tokenize import RegexpTokenizer




def buildIndex() -> None:
    '''
    iterate through every file and build out an inverse index represented
    through a dictionary

    @return: 
    '''

    # dictionary with key of token and value of list of postings
    indexStorage = dict()

    # dictionary that stores which url each docID represents
    # key: doc ID  =>   value: url
    urlStorage = dict()

    # currentDocID (will get incremented as we iterate through each file)
    docID = 1

    # used to count number of documents so we can load off files to disk periodically
    docCount = 0

    for root, dirs, files in os.walk("./DEV"):
        for file in files:
            fileToOpen = os.path.join(root, file)       # get actual path of file

            with open(fileToOpen, "r", errors='ignore') as current_file:
                try:
                    data = json.loads(current_file.read())
                    #posting.process_file(data["content"], indexStorage)
                    html_content = data["content"]


                    # Extract all text elements from the parsed HTML
                    soup = BeautifulSoup(html_content, 'html.parser')
                    text = soup.get_text()

                    # tokenize html, get list of all tokens
                    #tokens = tokenize(text)
                    #tokens =  word_tokenize(text)
                    tokenizer = RegexpTokenizer(r'\w+')
                    tokens = tokenizer.tokenize(text)


                    # Use porter stemmer to standardize all words
                    # ex: turns [likely, liking] => [like, like]
                    stemmer = SnowballStemmer(language='english')
                    stemmed_tokens = [stemmer.stem(token) for token in tokens]


                    # get dictionary that has counts of all tokens
                    tokenFrequencies = computeWordFrequencies(stemmed_tokens)

                    # iterate through tokens
                    for token in tokenFrequencies.keys():
                        # if token not in indexStorage then add it as a key with value being empty ListOfPostings
                        if token not in indexStorage:
                            indexStorage[token] = ListOfPostings()

                        # Create new posting object with specified id and frequency
                        currentPosting = Posting(docID, tokenFrequencies[token])      

                        # append new Posting object to indexStorage[token]
                        indexStorage[token].addPosting(currentPosting)

                    # set docID to point to new url 
                    urlStorage[docID] = file          # file is the correct url right?
                    
                    # increment docID
                    docID += 1
                    docCount += 1

                    # if number of documents has reached threshold, output to disk, clear dictionary, and reset docCount
                    if docCount == 100000:
                        outputToFile(indexStorage)
                        docCount = 0

                    
                except json.decoder.JSONDecodeError as e:
                    continue

    return indexStorage, urlStorage


def outputToFile(indexStorage) -> None:
    '''
    loads off files from indexStorage in order to meet constraint
    '''

    # ouput to file in correct format
    with open('dev_index.txt', 'w') as file:
        for key in indexStorage:
            file.write(key + " : "  + indexStorage[key].getStringOfPostings() + '\n\n')

    # clear dictionary to free up memory
    indexStorage.clear()

