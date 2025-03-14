import random 

questions = [
    {"question": "What is the smallest ocean?", "answer": "Arctic"},
    {"question": "What ocean are sharks mostly found in?", "answer": "Atlantic"},
    {"question": "What is the most famous marine plant?", "answer": "Seaweed"},
    {"question": "Do sharks have more fins or teeth?", "answer": "Teeth"},
    {"question": "What is the deepest part of the ocean called?", "answer": "Challenger Deep"},
    {"question": "Do sharks have bones?", "answer": "No"}, 
    {"question": "Do sharks only eat meat?", "answer": "No"}  
]

def ask_question(): 
    index = random.randint(0, len(questions) - 1) 
    question = questions[index]
    print(question["question"])
    answer = input("Your answer: ") 

    if answer == question["answer"]:
        return True
    else:
        return False
    
if ask_question():
    print("Correct!")
else:
    print("Incorrect!") 