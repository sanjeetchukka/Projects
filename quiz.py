import csv

def save_score(name, score, filename='scores.csv'):
    with open(filename, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([name, score])

def load_scores(filename='scores.csv'):
    scores = {}
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            name, score = row
            scores[name] = int(score)
    return scores

def run_quiz(name):
    score = 0
    # code for running the quiz
    
    ns=0    #ns=Score
    print("1.Capital of Afgahanistan\nA)Tirana\tB)Kabul\nC)Luanda\tD)Baku")
    a1=input()
    if a1=="B" or a1=="b":
        print("Correct Answer")
        ns=ns+1
    else:
        print("Wrong Answer,Correct option is B)Kabul")
    print("2.Capital of Argentina\nA)Vienna\tB)St.John's\nC)Algiers\tD)Buenos Aires")
    a2=input()
    if a2=="D" or a2=="d":
        print("Correct Answer")
        ns=ns+1
    else:
        print("Wrong Answer,Correct option is D)Buenos Aires")

    print("3.Capital of India\nA)New Delhi \tB)Berlin\nC)Dublin\tD)Dubai")
    a3=input()
    if a3=="A" or a3=="a":
        print("Correct Answer")
        ns=ns+1
    else:
        print("Wrong Answer,Correct option is B)Kabul")
    print("4.Capital of Belgium\nA)Brasilia \tB)Sofia\nC)Brussels\tD)Ottawa")
    a4=input()
    if a4=="C" or a4=="c":
        print("Correct Answer")
        ns=ns+1
    else:
        print("Wrong Answer,Correct option is C)Brussels")
    print("5.Capital of Mali\nA)Kuala Lumpur \tB)Bamako\nC)Majuro\tD)Port Louis")
    a5=input()
    if a5=="B" or a5=="b":
        print("Correct Answer")
        ns=ns+1
    else:
        print("Wrong Answer,Correct option is B)Bamako")  
    
    print("Your Score is ",ns)
    
    save_score(name, ns)
    scores = load_scores()
    print(scores)

name=input("What is your name:")
run_quiz(name)    
        
    


