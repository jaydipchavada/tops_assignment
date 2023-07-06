quiz = {
    1 : {
        "que" : "Most populer programming language ?",
        "ans" : "python"
    },
    2 : {
        "que" : "most populer cricketer ? ",
        "ans" : "ms dhoni"
    },
    3 : {
        "que" : "prime minister of india ? ",
        "ans" : "narender modi"
    }
}



score = 0

for i in range(1,len(quiz)+1):
    print(f"Que. {i} {quiz[i]['que']}")
    
    ans = input("Enter your ans : ").lower()
    if quiz[i]['ans'] == ans :
        score+=50
        print("Right Answer")
    else:
        score-=20
        print("wrong Answer")

print(f"score = {score}")