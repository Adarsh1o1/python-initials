questions = [
    ["The International Literacy Day is observed on", "sep 8", "nov 28", "may 2",
     "sep 22", "A"],
    ["The International Literacy Day is observed on", "sep 8", "nov 28", "may 2",
     "sep 22", "A"],
    ["The International Literacy Day is observed on", "sep 8", "nov 28", "may 2",
     "sep 22", "A"],
    ["The International Literacy Day is observed on", "sep 8", "nov 28", "may 2",
     "sep 22", "A"],
    ["The International Literacy Day is observed on", "sep 8", "nov 28", "may 2",
     "sep 22", "A"],
    ["The International Literacy Day is observed on", "sep 8", "nov 28", "may 2",
     "sep 22", "A"],
    ["The International Literacy Day is observed on", "sep 8", "nov 28", "may 2",
     "sep 22", "A"],
    ["The International Literacy Day is observed on", "sep 8", "nov 28", "may 2",
     "sep 22", "A"],
    ["The International Literacy Day is observed on", "sep 8", "nov 28", "may 2",
     "sep 22", "A"],
    ["The International Literacy Day is observed on", "sep 8", "nov 28", "may 2",
     "sep 22", "A"],
]
levels = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000]
take_away_money=0
for i in range(0,len(questions)):
    question=questions[i]
    print(f"Question for Rs.{levels[i]}\n")  
    print(question[0])
    print(f"a.{question[1]}             b.{question[2]}")
    print(f"c.{question[3]}             d.{question[4]}")
    ans=input("Enter your answer: ")
    if ans.upper()==question[5]:
        print(f"Correct, You have won {levels[i]}rs")
        if i==4:
            take_away_money=10,000
        if i==9:
            take_away_money=3,20,000
    else:
        print("Incorrect!")
        break
print(f"Your Take away money is Rs{take_away_money}")