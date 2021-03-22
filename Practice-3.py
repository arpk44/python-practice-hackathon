import random

while True:

    items = ("Vanilla", "Chocolate", "Strawberry", "Boston Cream", "Powdered Sugar", "Red", "Blue", "Green")

    question = int(input("How many would you like to order today?"))

    if question == 1:
        print(question)
        choice1 = random.choice(items)
        print(choice1)
        randomint = 1
        print(randomint)

    elif question == 2:
        print(question)
        choice1 = random.choice(items)
        choice2 = random.choice(items)
        if choice1 == choice2:
            choice3 = random.choice (items)
            print(choice1)
            print(choice3)
            randomint = 2
            print(randomint)
        else:
            print(choice1)
            print(choice2)
            randomint = 1
            print(randomint)
            
    elif question == 3:
        print(question)
        choice1 = random.choice(items)
        choice2 = random.choice(items)
        choice3 = random.choice(items)
        if choice1 == choice2:
            choice3 = random.choice (items)
            print(choice1)
            print(choice3)
            randoms = ("1", "2", "3")
            radomint = random.choice(randoms)
            print(randomint)
        else:
            print(choice1)
            print(choice2)
            print(choice3)
            randoms = ("1", "2", "3")
            randomint = random.choice(randoms)
            print(randomint)

    else:
        print("Reorder, please.")
    
