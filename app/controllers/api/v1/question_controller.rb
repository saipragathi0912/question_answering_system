class Api::V1::QuestionController < ApplicationController
    protect_from_forgery with: :null_session
    def ask_question
        question = question_params['question']
        puts "Question"
        puts question
        @response = `python3 lib/assets/python/main.py "#{question}"`
        render json: { answer: @response}
    end

    private 

    def question_params
        params.permit(:question)
    end
end