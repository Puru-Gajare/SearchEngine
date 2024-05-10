import os
from bs4 import BeautifulSoup
from collections import defaultdict
from tokenizer import tokenize
import posting
import shelve
import json
from build_index import buildIndex

if (__name__ == "__main__"):

    # create dictionary that stores info
    indexStorage, urlStorage = buildIndex()

    



