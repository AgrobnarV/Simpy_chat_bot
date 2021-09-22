print('Hello! My name is Test-bot.')
print('I was created in 2021.')
print('Please, remind me your name.')

name = input()

print('What a great name you have, ' + name + '!')
print('Let me guess your age.')
print('Enter remainders of dividing your age by 3, 5 and 7.')

# reading all remainders
first = abs(int(input())) % 3
second = abs(int(input())) % 5
third = abs(int(input())) % 7

age = (first * 70 + second * 21 + third * 15) % 105
print("Your age is " + str(age) + "; that's a good time to start programming!")

print("Now I will prove to you that I can count to any number you want.")
positive_number = int(input())
count = 0

while positive_number >= count:
    print(str(count) + "!")
    count += 1
print("Completed, have a nice day!")
