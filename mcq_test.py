class question:
    def __init__(self,ques,ans):
        self.ques=ques
        self.ans=ans



my_question=["what is your name \na.gaurav \nb anmiksha",
"hwt is your fav sports \n a.cricket \n b.football"]

que=[question(my_question[0],"a"),question(my_question[1],"b")]

def run_test(que):
    print("enter your name\n")
    name=input("")
    scrore=0
    for question in que:
        answer=input(question.ques)
        if answer== question.ans:
            scrore=scrore+1
        else:
            continue
    
    int(scrore)
    user=open("user.txt","a")
    user.write("\n"+ name+"\t" + str(scrore))
    user.close()
    print(str(scrore) +"/"+ str(len(que)) )




run_test(que)

