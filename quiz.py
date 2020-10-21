import datetime
import random

from questions import Add, Multiply


class Quiz:
    questions = []
    answers = []
    
    def __init__(self):
        question_types = (Add, Multiply)
        how_many_questions = int(input("How many questions?:  "))
        starting_range = int(input("What is the lowest number you would like to be quized on?:  "))
        ending_range = int(input("What is the highest number you would like to be quized on?:  ")) 
        # generate 10 random questions with numbers from 1 to 10
        for _ in range(how_many_questions):
            num1 = random.randint(starting_range, ending_range)
            num2 = random.randint(1, 10)
            question = random.choice(question_types)(num1, num2)
            # add these questions into self.questions
            self.questions.append(question)
        
    def take_quiz(self):

        self.start_time = datetime.datetime.now()
      
        for question in self.questions:

            self.answers.append(self.ask(question))
        else:

            self.end_time = datetime.datetime.now()
        
        return self.summary()
        

    def ask(self, question):
        correct = False

        question_start = datetime.datetime.now()
        
        answer = input(question.text + ' = ')
        
        if answer == str(question.answer):
            correct = True
            
        question_end = datetime.datetime.now()
        
        return correct, question_end - question_start
        
    def total_correct(self):
        # return the total # of correct answers
        total = 0
        for answer in self.answers:
            if answer[0]:
                total += 1
        return total
        
    def summary(self):
        # print how many you got right and the total # of questions. 5/10
        print("You got {} out of {} right.".format(
                self.total_correct(), len(self.questions)
        ))
        # print the total time for the quiz: 30 seconds!
        print("It took you {} seconds total.".format(
                (self.end_time-self.start_time).seconds
        ))
        

Quiz().take_quiz()
