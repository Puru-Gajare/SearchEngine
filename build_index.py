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

    for root, dirs, files in os.walk("./DEV"):
        for file in files:
            with open(file, "r") as current_file:
                data = json.loads(file.read())
                #posting.process_file(data["content"], indexStorage)
                html_content = data["content"]


                # Extract all text elements from the parsed HTML
                soup = BeautifulSoup(html_content, 'html.parser')
                text = soup.get_text()

                # tokenize html, get list of all tokens
                tokens = tokenize(text)

                # get dictionary that has counts of all tokens
                tokenFrequencies = computeWordFrequencies(tokens)

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

    return indexStorage, urlStorage
