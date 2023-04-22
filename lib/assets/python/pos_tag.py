import nltk
from nltk.tag import StanfordPOSTagger
class PosTag:
    def __init__(self,text) -> None:
        self.st = StanfordPOSTagger('/Users/pragathi/stanford-postagger-full-2020-11-17/models/english-bidirectional-distsim.tagger','/Users/pragathi/stanford-postagger-full-2020-11-17/stanford-postagger.jar',encoding='utf-8')
        self.tags=[]
        self.text = text
    def processed_tags(self):
        self.tags = self.st.tag(self.text.split())
        required_tags = ['NN','NNP','NNPS','JJ','VB','JJR','JJS']
        processed_tag = []
        for i in self.tags:
            if i[1] in required_tags:
                processed_tag.append(i[0])
        return processed_tag

