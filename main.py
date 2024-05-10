import os
from bs4 import BeautifulSoup
from collections import defaultdict
from tokenizer import tokenize
import posting
import shelve
import json
from build_index import buildIndex


if (__name__ == "__main__"):



    # copy this over to build_index once finished

    # for root, dirs, files in os.walk("./ANALYST"):
        
    #     for file in files:
            
    #         fileToOpen = os.path.join(root, file)     # get actual path of file
            

    #         with open(fileToOpen, "r", errors='ignore') as current_file:

    #             try:
    #                 data = json.loads(current_file.read())
    #                 #posting.process_file(data["content"], indexStorage)
    #                 html_content = data["content"]


    #                 # Extract all text elements from the parsed HTML
    #                 soup = BeautifulSoup(html_content, 'html.parser')
    #                 text = soup.get_text()
    #                 #print(text)
    #             except json.decoder.JSONDecodeError as e:
    #                 print("Error decoding JSON:", e)


    



