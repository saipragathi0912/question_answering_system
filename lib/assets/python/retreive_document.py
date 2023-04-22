import wikipedia
import requests
import re
import random
import concurrent.futures
class RetreiveDocument:
    def __init__(self,url='https://en.wikipedia.org/w/api.php') -> None:
        self.url = url

    def search_pages(self, query):
        params = {
            'action': 'query',
            'list': 'search',
            'srsearch': query,
            'format': 'json'
        }
        res = requests.get(self.url, params=params)
        return res.json()
    
    def search_page(self, page_id):
        try:
            res = wikipedia.page(pageid=page_id)
        except wikipedia.DisambiguationError as e:
            s = random.choice(e.options)
            res = wikipedia.page(s)
        return res.content
    
    def search(self, query):
        pages = self.search_pages(query)
        with concurrent.futures.ThreadPoolExecutor() as executor:
            process_list = [executor.submit(self.search_page, page['pageid']) for page in pages['query']['search']]
            docs = [self.post_process(p.result()) for p in process_list]
        return docs

    def post_process(self, doc):
        #pattern = "(^==) [A-Za-z0-9\s]+(==$)|(^===) [A-Za-z0-9\s]+(===$)"
        pattern = '|'.join([
            '== References ==',
            '== Further reading ==',
            '== External links',
            '== See also ==',
            '== Sources ==',
            '== Notes ==',
            '== Further references ==',
            '== Footnotes ==',
            '=== Notes ===',
            '=== Sources ===',
            '=== Citations ===',
        ])
        p = re.compile(pattern)
        indices = [m.start() for m in p.finditer(doc)]
        min_idx = min(*indices, len(doc))
        return doc[:min_idx]