import os
from bs4 import BeautifulSoup
from collections import defaultdict
from tokenizer import tokenize
import posting
import shelve
import json
from build_index import buildIndex

if (__name__ == "__main__"):


    # build inverted index, urls
    indexStorage, urlStorage = buildIndex()

    # print # of urls, # of tokens
    print(len(urlStorage))
    print(len(indexStorage))


    # output rest of urls to file
    # with open('dev_index.txt', 'w') as file:
    #     for key in indexStorage:
    #         file.write(key + " : "  + indexStorage[key].getStringOfPostings() + '\n\n')

    
















