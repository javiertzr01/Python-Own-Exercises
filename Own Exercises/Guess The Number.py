import random

num = (random.randint(1, 20))
condition = False
numguess = int(input())
if numguess != num:
    print(str(numguess) + ' is wrong')
    if numguess > num:
        print("Your number is higher than the correct number")
    elif numguess < num:
        print("Your number is lower than the correct number")
    print('Please Try Again')
    numguess = int(input())
elif numguess == num:
    print(str(numguess) + ' is correct')
    condition = True
while condition is not True:
    if numguess != num:
        print(str(numguess) + ' is wrong')
        if numguess > num:
            print("Your number is higher than the correct number")
        elif numguess < num:
            print("Your number is lower than the correct number")
        print('Please Try Again')
        numguess = int(input())
    elif numguess == num:
        print(str(numguess) + ' is correct')
        condition = True