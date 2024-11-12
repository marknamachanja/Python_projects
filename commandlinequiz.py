#import the "random" module to generate random questions
import random

#Define a dictionary to store the quiz questions and answers
quiz_questions = {
    "What is the capital of France?": "Paris",
    "Who is the current Prime Minister of the United Kingdom?": "David Cameron",
    "What is the name of the longest river in the world?": "Nile",
    "What is the largest island in the world?": "Greenland",
    "Who is the author of the book 'To Kill a Mockingbird'?": "Harper Lee"
}

#Define a function to ask a question and check the answer
def ask_questions(question, answer):
    #ask the user the question
    user_answer = input(question + " ")
    
    #check if the user's answer matches the correct answer
    if user_answer.lower() == answer.lower():
        print("Correct!")
        return 1
    else:
        print("Incorrect! The right answer is " + answer)
        return 0

#Define a function to play the quiz
def play_quiz():
    #initialize the score to zero
    score = 0

    #shuffle the quiz questions to randomize the order
    questions = list(quiz_questions.items())
    random.shuffle(questions)

    #ask each question and update the score
    for question, answer in questions:
        score += ask_questions(question, answer)
        
    #display the final score
    print("Quiz complete!!\nYour final score is " +str(score)+"/"+ str(len(questions)))

#define a main part to start the quiz
def main():
    print("Welcome to the quiz!")
    play_quiz()

if __name__ == "__main__":
    main()