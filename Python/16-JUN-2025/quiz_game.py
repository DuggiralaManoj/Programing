print("**********************************")
print("Welcome to Quiz marathon")
quiz_question=[
    {"text":"1.What is the largest lake in the world?","answer":"B"},
    {"text":"2.Which planet in the solar system is known as the “Red Planet”?","answer":"C"},
    {"text":"3.What is the capital of Japan?","answer":"B"},
    {"text":"4.Which river is the longest in the world?","answer":"C"},
    {"text":"5. What gas is used to extinguish fires?","answer":"B"}
]
options=[["1.Caspian Sea","2.Baikal","3.Lake Superior","4.Ontario"],
         ["1.Venus","2.Earth","3.Mars","4.Jupiter"],
         ["1.Beijing","2.Tokyo","3.Seoul","4.Bangkok"],
         ["1.Amazon","2.Mississippi","3.Nile","4.Yangtze"],
         ["1.Oxygen","2.Nitrogen","3.Carbon dioxide","4.Hydrogen"]
       ]
score=0
def check_answer(user_answer,correct_answer):
    if user_answer==correct_answer:
        return True
    else:
        return False
for question in range(len(quiz_question)):
    print("********************************")
    print(quiz_question[question]["text"])
    for i in options[question]:
        print(i)
    guess=input(" Select the the character (A/B/C/D):").upper()
    is_correct=check_answer(guess,quiz_question[question]["answer"])
    if is_correct:
        print("Correct answer")
        score +=1
    else:
        print("Incorrect answer")
        print(f"The correct answer is:{quiz_question[question]['answer']}")

print(f"Your have given {score} correct answers")
print(f"You have scored {(score/len(quiz_question))*100}%")