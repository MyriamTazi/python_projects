
import math

def repeat(*args):
    
    yn = (input("Would you like to calculate something else? please, enter 'Y' for yes and 'N' for no: "))
    print(yn)

    if yn == 'N' or 'n':
        print("Okay, have a lovely rest of the day, hope to see you soon")
    elif yn == 'Y' or 'y':
        print("Okay, let's calculate something else!")
        calculator()
    else: 
        print("Please print a valid answer : Y or N ")
        repeat()


def calculator(*args):
    print("Hello and thank you for using my calculator, in here you could add (+), subtract(-), multiply(*) and divide(/) numbers, please follow the rules set and only enter numbers, and only choose for the operators available, enjoy :)")
    add = '+'
    minus = '-'
    times = '*'
    division = '/'
    try:
        n1 = int(input('Enter your first number: '))
        op = input('Enter one of the following please: + , - , / or * :')
        n2 = int(input('Enter your second number: '))
        
        if op == add :
            print((f'Your result is: {n1} + {n2} ='), (n1 + n2))
            # print(n1 + n2)
        elif op == minus:
            print((f'{n1} - {n2} ='), (n1-n2))
        elif op == times:
            print((f'{n1} * {n2} ='), (n1 * n2))
        elif op == division:
            print((f'{n1} / {n2} = '),(n1/n2))
    except:
        print("Invalid input, please only enter numbers and choose from the operators provided")
    repeat()

calculator()


# my_dict= [
#     1 : one, 2 : two, 3 : three, 4 : four, 5 : five, 6 : six; 7 : seven, 8 : eight, 9 : nine  
# ]
import num2words 




# calculator(99, 78)


