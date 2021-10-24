def greet(bot_name, birth_year):
    print('Hello! My name is Test-bot.')
    print('I was created in 2021.')


def remind_name():
    print('Please, remind me your name.')
    name = input()
    print('What a great name you have, ' + name + '!')


def guess_name():
    print('Let me guess your age.')
    print('Enter remainders of dividing your age by 3, 5 and 7.')

    num3 = abs(int(input())) % 3
    num5 = abs(int(input())) % 5
    num7 = abs(int(input())) % 7
    guess_age = (num3 * 70 + num5 * 21 + num7 * 15) % 105

    print("Your age is " + str(guess_age) + "; that's a good time to start programming!")


def count():
    print("Now I will prove to you that I can count to any number you want.")

    positive_number = int(input())
    i = 0
    while positive_number >= i:
        print(str(i) + "!")
        i += 1


def program_methods():
    print("Let's test your programming knowledge.")
    print("""Why do we use methods?
            1. To repeat a statement multiple times.
            2. To decompose a program into several small subroutines.
            3. To determine the execution time of a program.
            4. To interrupt the execution of a program.""")

    meth_num = int(input())
    while meth_num > 4 or meth_num < 1:
        print("You must enter 1 to 4")
        meth_num = int(input())
    while meth_num != 3:
        print("Please, try again.")
        meth_num = int(input())


def bye():
    print('Congratulations, have a nice day!')


greet('Andrew', '2021')
remind_name()
guess_name()
count()
program_methods()
bye()
