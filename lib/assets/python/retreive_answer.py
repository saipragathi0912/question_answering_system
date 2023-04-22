import pickle
import operator
from transformers import BertTokenizer,BertForQuestionAnswering,QuestionAnsweringPipeline
class RetreiveAnswer:
    def __init__(self,model,tokenizer) -> None:
        model = BertForQuestionAnswering.from_pretrained(model)
        tokenizer = BertTokenizer.from_pretrained(tokenizer)
        self.qapipeline = QuestionAnsweringPipeline(model = model,tokenizer=tokenizer)

    def answer(self,question,passages):
        answers = []
        for passage in passages:
            try:
                answer = self.qapipeline(question=question, context=passage)
                answer['text'] = passage
                answers.append(answer)
            except KeyError:
                pass
        return answers

    