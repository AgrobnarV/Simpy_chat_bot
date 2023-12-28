def greet(bot_name, birth_year):
    print(f"Hello! My name is {bot_name}.")
    print(f"I was created in {birth_year}.")


def remind_name():
    print('Please, remind me your name.')
    name = input()
    print('What a great name you have, ' + name + '!')


def guess_name():
    print("Let me guess your age.")
    print("Enter the remainders of dividing your age by 3, 5, and 7:")

    num3 = abs(int(input())) % 3
    num5 = abs(int(input())) % 5
    num7 = abs(int(input())) % 7
    guess_age = (num3 * 70 + num5 * 21 + num7 * 15) % 105

    print("Your age is " + str(guess_age) + "; that's a good time to start programming!")


def count():
    print("Now I will prove to you that I can count to any number you want.")
    print("Enter a positive number:")
    positive_number = int(input())
    
    for i in range(positive_number + 1):
        print(f"{i}!")


def program_methods():
    print("Let's test your programming knowledge.")
    print("""Why do we use methods?
            1. To repeat a statement multiple times.
            2. To decompose a program into several small subroutines.
            3. To determine the execution time of a program.
            4. To interrupt the execution of a program.""")

    meth_num = int(input())
    if 1 <= meth_num <= 4:
        if meth_num == 3:
            print("Correct! We use methods to determine the execution time of a program.")
        else:
            print("Incorrect. Please review and try again.")
    else:
        print("You must enter a number between 1 and 4.")


def bye():
    print('Congratulations, have a nice day!')


greet('Andrew', '2021')
remind_name()
guess_name()
count()
program_methods()
bye()
