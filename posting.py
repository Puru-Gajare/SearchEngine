from tokenizer import tokenize
from bs4 import BeautifulSoup


class Posting:
    def __init__(self) -> None:
        self.website_name = ""
        self.token_freq = 0



class ListOfPostings:
    def __init__(self) -> None:
        pass


def process_file( html_content: str, indexStorage ) -> None:
    '''
    takes in html content, tokenizes it, and adds it to storage dictionary

    @return: 
    '''
    
    # Extract all text elements from the parsed HTML
    soup = BeautifulSoup(html_content, 'html.parser')
    text = soup.get_text()

    # tokenize html, get list of all tokens
    tokens = list()   # change after tokenize function gets updated
    tokens = tokenize(text)

    # iterate through tokens
    for token in tokens:
        # if token already exists in storage, add url to it's list and increment frequency count
        # if token does not exist in storage, add it, add url to it's list, and set its frequency count to 0
            
