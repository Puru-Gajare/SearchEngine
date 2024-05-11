from tokenizer import *
from bs4 import BeautifulSoup
import shelve


class Posting:
    def __init__(self, website_name, hash, token_freq) -> None:
        self.website_name = website_name
        self.hash = hash
        self.token_freq = token_freq
        


class ListOfPostings:
    def __init__(self) -> None:
        self.listOfUrlIds = list()

    def addURL(self, docID: str, frequency: int):
        if len(self.listOfUrlsIds) == 0:
            self.listOfUrlsIds.append(docID)
            return
        
        # find index to insert at
        index = 0
        for id in self.listOfUrlsIds:
            if id > docID:
                break
            
            index += 1

        self.listOfUrlIds.insert(index, docID)

def process_file( html_content: str, indexStorage: shelve.Shelf, docID: int ) -> None:
    '''
    takes in html content, tokenizes it, and adds it to storage dictionary

    @return: 
    '''
    
    # Extract all text elements from the parsed HTML
    soup = BeautifulSoup(html_content, 'html.parser')
    text = soup.get_text()

    # tokenize html, get list of all tokens
    tokens = list()   # change after tokenize function gets updated

    tokens = list(set(tokenize(text)))   # eliminates duplicates
    frequencies = compute_word_frequencies(tokens)


    # iterate through tokens
    for token, frequency in frequencies.items:
        # if token already exists in storage, add url to it's list and increment frequency count
        if token in indexStorage:
            indexStorage[token].addURL(docID, frequency)
        else:
            indexStorage[token] = ListOfPostings()
            indexStorage[token].addURL(docID, frequency)
        # if token does not exist in storage, add it, add url to it's list, and set its frequency count to 0
            
