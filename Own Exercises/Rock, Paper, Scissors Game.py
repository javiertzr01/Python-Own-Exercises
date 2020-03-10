import random

def compare(choice1, choice2):
    if WinCondition[choice1] == choice2:
        return "win"
    elif DrawCondition[choice1] == choice2:
        return "draw"
    else:
        return "lose"

def CheckDef(variable):
    try:
        return definitions[variable]
    except Exception:
        return "invalid"


definitions = {
    "Rock" : "Rock",
    "rock" : "Rock",
    "ROCK" : "Rock",
    "ROck" : "Rock",
    "ROCk" : "Rock",
    "Paper" : "Paper",
    "paper" : "Paper",
    "PAPER" : "Paper",
    "PAper" : "Paper",
    "PAPer" : "Paper",
    "PAPEr" : "Paper",
    "Scissors" : "Scissors",
    "scissors" : "Scissors",
    "SCISSORS" : "Scissors",
    "SCIssors" : "Scissors",
    "Ok" : "Yes",
    "ok" : "Yes",
    "Sure" : "Yes",
    "sure" : "Yes",
    "Yes" : "Yes",
    "Y" : "Yes",
    "y" : "Yes",
    "yes" : "Yes",
    "YES" : "Yes",
    "YEs" : "Yes",
    "no" : "No",
    "No" : "No",
    "N" : "No",
    "n" : "No",
    "NO" : "No",   
    "Nah" : "No",
    "nah" : "No"
}



WinCondition = {
    "Rock" : "Paper",
    "Paper": "Scissors",
    "Scissors": "Rock"
}
DrawCondition = {
    "Rock" : "Rock",
    "Paper" : "Paper",
    "Scissors": "Scissors"
}

playing = True

choices = ["Rock", "Paper", "Scissors"]
while playing is True:
    computerchoice = random.choice(choices)
    userchoice = input("Please enter Rock, Paper or Scissors: ")
    userchoice = CheckDef(userchoice)
    while userchoice == "invalid":
        userchoice = input("Please enter correctly. Rock, Paper or Scissors: ")
        userchoice = CheckDef(userchoice)
    print("Computer threw " + computerchoice)
    print("You chose " + userchoice)
    if compare(computerchoice, userchoice) == "win":
        print("You win!")
    elif compare(computerchoice, userchoice) == "draw":
        print("You drew!")
    elif compare(computerchoice, userchoice) == "lose":
        print("You lose!")
    WantToPlay = input("Another round? Y/N: ")
    WantToPlay = CheckDef(WantToPlay)
    if WantToPlay == "Yes":
        continue
    elif WantToPlay == "No":
        playing = False
    while WantToPlay == "invalid":
        WantToPlay = input("Please enter correctly. Another round? Y/N: ")
        WantToPlay = CheckDef(WantToPlay)
        if WantToPlay == "Yes":
            continue
        elif WantToPlay == "No":
            playing = False
    
