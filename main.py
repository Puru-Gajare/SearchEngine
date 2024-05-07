import os
from bs4 import BeautifulSoup
from collections import defaultdict
from tokenizer import tokenize
import posting
import shelve
import json

if (__name__ == "__main__"):
    indexStorage = shelve.open("index")

    # for each file, create dict where key is the url and value is the hash of the file
    for root, dirs, files in os.walk("./DEV"):
        for file in files:
            with open(file, "r") as current_file:
                data = json.loads(file.read())
                posting.process_file(data["content"], indexStorage)

    



