# Just trying to build a program that asks questions then answers
class QuestionManager:
    def __init__(self, question, questionNumber):
        self.question = question
        self.questionNumber = questionNumber

    def append(self):
        print("Q",self.questionNumber, ":", self.question)

        #Conditional statement for answering the questions
        if self.question == "Did she ever love me?":
            print("Yes")
        elif self.question == "What is Computer":
            print("A machine, you fool")
        else:
            print("No, and that's ok")

# QUESTIONS
print("Ask me!")
questions = input()
q1 = QuestionManager("What is Computer",1)
q1.append()
q2 = QuestionManager(questions,2)
q2.append()

print(q1, q2)