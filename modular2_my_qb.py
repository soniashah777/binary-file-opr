import pickle
import os
question_bank={"questions":["Where is taj mahal","Who was the first Prime Minister of India"],
               "option1":["Delhi","R.Vankat Raman"],
               "option2": ["Agra","V V Giri"],
               "option3": ["Madras","Jawahar Lal Nehru"],
               "answer":["Agra","Jawahar Lal Nehru"]}

if (os.path.getsize("qb.dat")==0):
    create_file=open("qb.dat","wb")
    pickle.dump(question_bank,create_file)
    create_file.close()


def start_quiz():
    score=0
    open_file=open("qb.dat","rb")
    open_file.seek(0)
    dict_qb=pickle.load(open_file)
    print (dict_qb)
    for i in range(0,len(dict_qb["questions"])):
        print ("question number",i)
        print (dict_qb["questions"][i])
        print (dict_qb["option1"][i])
        print (dict_qb["option2"][i])
        print (dict_qb["option3"][i])
        ans=input ("Enter your answer")
        if (ans==dict_qb["answer"][i]):
            score+=1
    print ("you have scored "+str(score)+ "scores")
    open_file.close()
    
def add_question():
    add_file=open("qb.dat","rb+")
    new_qb=pickle.load(add_file)
    cont="y"
    while cont=="y":
        new_qb["questions"].append(input("Enter question")) 
        new_qb["option1"].append(input("Enter option1"))
        new_qb["option2"].append(input("Enter option2"))
        new_qb["option3"].append(input("Enter option3"))
        new_qb["answer"].append(input("Enter answer"))
        cont=input ("Enter y to contunue and n to stop")
    add_que=open("qb.dat","wb+")
    pickle.dump(new_qb,add_que)
    add_que.flush()
    add_que.close()
    add_file.close()
print ("Welcome to my quiz")
while True:
    print ("Enter a to add questions")
    print ("Enter p to play quiz")
    ch=input("Enter your choice")
    if (ch=="a"):
        add_question()
    elif (ch=="p"):
        start_quiz()
