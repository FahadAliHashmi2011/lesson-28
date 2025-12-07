class A:
    def __init__(self, a):
        self.a = a

    def __lt__(self, other):
        if(self.a < other.a):
            return "ob1 is less than ob2"
        else:
            return "ob2 is less than ob1"

    def __eq__(self, other):
        if(self.a == other.a):
            return "Both are equal"
        else:
            
            return "They are not equal"

ob1 = A(2)
ob2 = A(3)
print(ob1 < ob2)
ob3= A(4)
ob4= A(5)
print(ob3 == ob4)
###################################################
class flashcard:
    def __init__(self, word, meaning):
        self.word = word
        self.meaning = meaning
    def __str__(self):
        return self.word + ' (' + self.meaning + ')'

flash = []
print("welcome to flashcard application")
while(True):
    word = input("enter the name you want to add to flashcard : ")
    meaning = input("enter the meaning of the word : ")
    
    flash.append(flashcard(word, meaning))
    
    option = int(input("enter 0 , if you want to add another flashcard otherwise enter 1 : "))
    
    if(option):
        break

print("\nYour flashcards")
for i in flash:
    print(">", i)
    
#############################################################################################
import random

class FruitQuiz:
    def __init__(self):
        self.fruits = {'apple':'red',
                       'orange':'orange',
                       'watermelon':'green',
                       'banana':'yellow'}

    def start_quiz(self):
        while True:
            fruit, color = random.choice(list(self.fruits.items()))

            print("What is the color of {}?".format(fruit))
            user_answer = input()

            if(user_answer.lower() == color):
                print("Correct answer")
            else:
                print("Wrong answer")

            option = int(input("enter 0 , if you want to play again otherwise enter 1 : "))
            if (option):
                break

quiz = FruitQuiz()
quiz.start_quiz()







    