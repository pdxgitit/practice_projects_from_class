import datetime
import random

from questions import Add, Multiply


class Quiz(object):
    questions = []
    answers = []

    def __init__(self):
        # generate 10 random questions with numbers from 1 to 10
        for count in range(0, 10):
            self.num1 = random.choice(range(1, 11))
            self.num2 = random.choice(range(1, 11))
            self.add_or_mult = random.choice(range(0, 2))
            if self.add_or_mult:
                self.ask = Add(self.num1, self.num2).text
                self.answer = Add(self.num1, self.num2).answer
                self.questions.append(self.ask)
                self.answers.append(self.answer)
            else:
                self.ask = Multiply(self.num1, self.num2).text
                self.answer = Multiply(self.num1, self.num2).answer
                self.questions.append(self.ask)
                self.answers.append(self.answer)

    def take_quiz(self):
        # log start time
        self.start = datetime.datetime.now()
        self.correct = 0
        # ask all of the question
        for indx, question in enumerate(self.questions):
            print("What is {} ? >>").format(question)
            attempt = int(raw_input())
            # log if they got the questions right
            if attempt == self.answers[indx]:
                self.correct += 1
        # log the end time
        self.end = datetime.datetime.now()
        # show a summary
        self.summary()

    def summary(self):
    # print how many you got right and the total # of questions. 5/10
        print "\n" * 50
        print "You got {}/{} correct!".format(self.correct, len(self.answers))
    # print the total time for the quiz: 30 seconds!
        print "The quiz took you {} seconds!".format((self.end - self.start).total_seconds())


quiz = Quiz()
quiz.take_quiz()