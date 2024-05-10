import os
from bs4 import BeautifulSoup
from collections import defaultdict
from tokenizer import tokenize
import posting
import shelve
import json
from build_index import buildIndex

from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk.tokenize import TreebankWordTokenizer
from nltk.stem import SnowballStemmer
from nltk.tokenize import RegexpTokenizer







if (__name__ == "__main__"):


    indexStorage, urlStorage = buildIndex()

    print(len(urlStorage))
    print(len(indexStorage))





    # with open('dev_index.txt', 'w') as file:
    #     for key in indexStorage:
    #         file.write(key + " : "  + indexStorage[key].getStringOfPostings() + '\n\n')


    # text = "Hello everyone. Welcome to GeeksforGeeks."

    # # Tokenize the sentence
    # tokens =  word_tokenize(text)

    # # Print the tokens
    # print(tokens)

    # stemmer = SnowballStemmer(language='english')
    # stemmed_tokens = [stemmer.stem(token) for token in tokens]

    # print(stemmed_tokens)





    # copy this over to build_index once finished
    # count = 0
    # for root, dirs, files in os.walk("./DEV"):
    #     for file in files:
    #         fileToOpen = os.path.join(root, file)       # get actual path of file
    #         count += 1
    #         #print(file)
    #         # with open(fileToOpen, "r", errors='ignore') as current_file:

    #         #     try:
    #         #         data = json.loads(current_file.read())
    #         #         #posting.process_file(data["content"], indexStorage)
    #         #         html_content = data["content"]

    #         #         print(html_content)


    #         #         # Extract all text elements from the parsed HTML
    #         #         soup = BeautifulSoup(html_content, 'html.parser')
    #         #         text = soup.get_text()
    #         #         #print(text)
    #         #     except json.decoder.JSONDecodeError as e:
    #         #         print("Error decoding JSON:", e)

    # print(count)


    



