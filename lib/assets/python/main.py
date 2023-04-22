from question_answer import QuestionAnswerModel
import sys
model_checkpoint = "bert-large-uncased-whole-word-masking-finetuned-squad"
input = sys.argv[1]
if __name__ == '__main__':
    qa_model = QuestionAnswerModel(input,model_checkpoint,model_checkpoint)
    response = qa_model.execute_model()
    print(response)