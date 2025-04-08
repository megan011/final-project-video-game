import time
from question import Questionnaire


def print_dramatic_text(text: str, delay=0.1):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

if __name__ == '__main__':

    questionnaire = Questionnaire()
    
    print('---Welcome to Shark Chase!---')
    print_dramatic_text('In order to make it back to land, answer the following questions correctly.')

    correct = questionnaire.ask_question()
    if correct:
        print_dramatic_text('Correct!')
    else:
        print_dramatic_text('Incorrect ... you\'ve been eaten by the shark!')

    response = input('Would you like to add a custom question? (y/n)')
    if response.casefold() == 'y':
        q = input('Please enter your question:')
        a = input('Please enter your answer:')

        result = questionnaire.add_question(q, a)
        if result:
            print('Your question has been successfully added!')
        else:
            print('Your question already exists!')

    num_correct = 0

    while num_correct < 3:
        correct = questionnaire.ask_question()
        if correct: 
            num_correct += 1 
            print_dramatic_text('Correct!')
        else:
            print_dramatic_text('Incorrect! You\'ve been eaten by the shark!')

        if num_correct >= 3: 
            print_dramatic_text('Congratulations! You made it to land safely!')
         