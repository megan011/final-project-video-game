import random 

class Questionnaire:
    def __init__(self):
        self.questions = [
            "What is the smallest ocean?",
            "What ocean are sharks mostly found in?",
            "What is the most famous marine plant?",
            "Do sharks have more fins or teeth?",
            "What is the deepest part of the ocean called?",
            "Do sharks have bones?",
            "Do sharks only eat meat?"
        ]
        self.answers = [
            "Arctic",
            "Atlantic",
            "Seaweed",
            "Teeth",
            "Challenger Deep",
            "No",
            "No"
        ]

    def ask_question(self) -> bool: 
        index = random.randint(0, len(self.questions) - 1) 
        question = self.questions[index]
        print(question)

        answer = input("Your answer: ") 
        if answer.casefold() == self.answers[index]:
            return True
        else:
            return False
