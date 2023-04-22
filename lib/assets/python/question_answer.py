import nltk
from pos_tag import PosTag
from retreive_document import RetreiveDocument
from retreive_passages import RetreivePassages
from retreive_answer import RetreiveAnswer
from nltk.tag import StanfordPOSTagger
class QuestionAnswerModel:
    def __init__(self,text,model,tokenizer) -> None:
        self.question = text
        self.pos_tag_model = PosTag(text)
        self.retreive_documents = RetreiveDocument()
        self.retreive_passages = RetreivePassages()
        self.retreive_answer = RetreiveAnswer(model,tokenizer)

    def execute_model(self):
        reqd_words = self.pos_tag_model.processed_tags()
        query = ' '.join(reqd_words)
        if len(query) > 0:
            docs = self.retreive_documents.search(query)
            passages = self.retreive_passages.top_passages(docs,query)
            top_answers = self.retreive_answer.answer(self.question,passages)
            return top_answers[0]['text']
        return "Oops!! I don't know the answer for your question :/"
