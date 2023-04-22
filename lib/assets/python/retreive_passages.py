from rank_bm25 import BM25Okapi
class RetreivePassages:
    def __init__(self) -> None:
        self.docs = []

    def get_all_passages(self):
        temp = list()
        for doc in self.docs:
            temp.append(doc.split("\n"))
        self.passages = temp
        return [j for i in temp for j in i]
    
    def top_passages(self,docs,query):
        self.docs = docs
        all_passages = self.get_all_passages()
        tokenized_corpus = [passage.split(" ") for passage in all_passages]
        bm25 = BM25Okapi(tokenized_corpus)
        tokenized_query = query.split(" ")
        doc_scores = bm25.get_scores(tokenized_query)
        self.relevant_passages = bm25.get_top_n(tokenized_query, self.get_all_passages(), n=2)
        return self.relevant_passages



