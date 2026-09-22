import time
import random
import requests

class Rest:
    '''
    Class containing REST functions common to the whole project
    '''
    # Constants declaration
    #API headers
    HEADERS = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:124.0) Gecko/20100101 Firefox/124.0",
        "Accept": "application/json",
        "Accept-Language": "en-US,en;q=0.9",
    }

    def __init__(self, API_URL: str):
        self.API_URL = API_URL
        

    def rest_get (self, body: str) -> list:
                    
        '''
        Makes a REST GET call
        '''
        time.sleep(random.uniform(1.5, 3.0))

        params = {'q': body, 'format': 'json'}
        response = requests.get(self.API_URL, params=params, timeout=10, headers=self.HEADERS)
        print(f"REST GET call executed:\n{response}")
        
        return response
    
    def rest_find(self, body: list, phrase: str):
        '''
        Searches a phrase in the rest response
        '''
        response = body.json() ['Heading'].lower()
        assert phrase.lower() == response

    def rest_response_code(self, body: list, code: int):
        '''
        Validates response status code
        '''
        assert body.status_code == code