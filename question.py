class question:
    def __init__(self,promt,ans):
        self.promt=promt
        self.ans=ans




question_prompts=["what is you fav sport? \n a cricket \n b football",
"what is name of planet \n a. earth \n b. marks \n c. pluto",
"apple is----colour? \n a. blue \n b. yellow \n c. red"]

que=[ question(question_prompts[0],"b"),
question(question_prompts[1],"a"),
question(question_prompts[2],"c")
]


def run_test(que):
    score=0
    for question in que:
        answer = input(question.promt)
        if answer == question.ans:
            score+=1
    print("you got \t"+ str(score) +"/" + str(len(que)))

run_test(que)

