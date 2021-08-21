def greet(bot_name, birth_year):
    print('Hello! My name is ' + bot_name + '.')
    print('I was created in ' + birth_year + '.')


def remind_name():
    print()
    name = input('Please, remind me your name: ')
    print('What a great name you have, ' + name + '!')


def guess_age():
    print()
    print('Let me guess your age.')
    print('Enter remainders of dividing your age by 3, 5 and 7.')

    rem3 = int(input())
    rem5 = int(input())
    rem7 = int(input())
    age = (rem3 * 70 + rem5 * 21 + rem7 * 15) % 105

    print("Your age is " + str(age) + "; that's a good time to start programming!")


def count():
    print()
    print('Now I will prove to you that I can count to any number you want.')

    num = int(input("Enter any number you want me to count up to: "))
    curr = 0
    while curr <= num:
        print(curr, '!')
        curr = curr + 1
    print("Count quite easily done :)")

def test():
    print()
    print("Let's test your programming knowledge.")
    # write your code here
    print("Why do we use methods?")
    print("1. To repeat a statement multiple times.")
    print("2. To decompose a program into several small subroutines.")
    print("3. To determine the execution time of a program.")
    print("4. To interrupt the execution of a program.")

    answer = "2"

    while True:
        reply = str(input("> "))

        if reply != answer:
            print("Wrong answer. Please try again")


        else:
            print('Completed, have a nice day!')
            break


def end():
    print('Congratulations, have a nice day!')


greet('Aid', '2021')
remind_name()
guess_age()
count()
test()
end()
