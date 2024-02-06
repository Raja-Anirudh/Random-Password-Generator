# Importing the Requirements
import random

# Defining the Variables
alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
upper_alphabets = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
special_characters = ['_', '*', '$', '@', '&', '^', '#']

string = alphabets + upper_alphabets + numbers + special_characters

length = 8
length1 = 9
length2 = 10
length3 = 11
length4 = 12
length5 = 13
length6 = 14

password_a = "".join(random.sample(string, length))
password_b = "".join(random.sample(string, length1))
password_c = "".join(random.sample(string, length2))
password_d = "".join(random.sample(string, length3))
password_e = "".join(random.sample(string, length4))
password_f = "".join(random.sample(string, length5))
password_g = "".join(random.sample(string, length6))

questions = [
    "How many characters in a password is safe and easy to remember?\na)12\nb)14\nc)13",
    "Which country has the best cyber security?\na)China\nb)India\nc)United States of America?",
    "Which country has the lowest cybercrime rate?\na)China\nb)Australia\nc)Denmark"
]
answers = [
    "a",
    "c",
    "b"
]

# Introducing the Password Generator
print("Hi I am your Password generator")
print("I am used for generating passwords to protect your data.")
print("Please select the level of the password")
print("The best option to select is the option 'd' because it is easy to remember and hard to crack.Thanks!")
print("a = Very Easy")
print("b = Easy")
print("c = Simple")
print("d = Hard")
print("e = Very Hard")
print("f = Impossible")
print("g = Out of the Box")

# Code of the Password Generator
while True:
    choice = input("Please select any one option to continue to the next step: ")

    if choice in ('a', 'b', 'c', 'd', 'e', 'f', 'g'):
        if choice == 'a':
            print(password_a)
            print("The password is above this line dont share it with anyone.")
            choice1 = input("Do you want to answer a question yes/no: ")
            print(choice1)
            if choice1 == 'yes':
                question_num = random.randint(0, len(questions) - 1)
                question = questions[question_num]
                answer = answers[question_num]
                user_answer = input("Question: " + question + "\nAnswer: ")
                if user_answer.lower() == answer.lower():
                    print("Correct!")
                    fb_1 = input("What is your experience after using Random Password Generator good/bad: ")
                    if fb_1 == 'good':
                        print("Thankyou for the feedback! Meet you again next time:).")
                        break
                    else:
                        if fb_1 == 'bad':
                            print("Sorry for the inconvenience. Meet you again next time.")
                            break
                        else:
                            print("It's a typo. Meet you again next time.")
                            break
                else:
                    print("Sorry, the correct answer is " + answer)
                    fb_1 = input("What is your experience after using Random Password Generator good/bad: ")
                    if fb_1 == 'good':
                        print("Thankyou for the feedback! Meet you again next time:).")
                        break
                    else:
                        if fb_1 == 'bad':
                            print("Sorry for the inconvenience. Meet you again next time.")
                            break
                        else:
                            print("It's a typo. Meet you again next time.")
                            break
            else:
                if choice1 == 'no':
                    fb_1 = input("What is your experience after using Random Password Generator good/bad: ")
                    if fb_1 == 'good':
                        print("Thankyou for the feedback! Meet you again next time:).")
                        break
                    else:
                        if fb_1 == 'bad':
                            print("Sorry for the inconvenience. Meet you again next time.")
                            break
                        else:
                            print("It's a typo. Meet you again next time.")
                            break

        if choice == 'b':
            print(password_b)
            print("The password is above this line dont share it with anyone.")
            choice2 = input("Do you want to answer a question yes/no: ")
            print(choice2)
            if choice2 == 'yes':
                question_num = random.randint(0, len(questions) - 1)
                question = questions[question_num]
                answer = answers[question_num]
                user_answer = input("Question: " + question + "\nAnswer: ")
                if user_answer.lower() == answer.lower():
                    print("Correct!")
                    fb_2 = input("What is your experience after using Random Password Generator good/bad: ")
                    if fb_2 == 'good':
                        print("Thankyou for the feedback! Meet you again next time:).")
                        break
                    else:
                        if fb_2 == 'bad':
                            print("Sorry for the inconvenience. Meet you again next time.")
                            break
                        else:
                            print("It's a typo. Meet you again next time.")
                            break
                else:
                    print("Sorry, the correct answer is " + answer)
                    fb_2 = input("What is your experience after using Random Password Generator good/bad: ")
                    if fb_2 == 'good':
                        print("Thankyou for the feedback! Meet you again next time:).")
                        break
                    else:
                        if fb_2 == 'bad':
                            print("Sorry for the inconvenience. Meet you again next time.")
                            break
                        else:
                            print("It's a typo. Meet you again next time.")
                            break
            else:
                if choice2 == 'no':
                    fb_2 = input("What is your experience after using Random Password Generator good/bad: ")
                    if fb_2 == 'good':
                        print("Thankyou for the feedback! Meet you again next time:).")
                        break
                    else:
                        if fb_2 == 'bad':
                            print("Sorry for the inconvenience. Meet you again next time.")
                            break
                        else:
                            print("It's a typo. Meet you again next time.")
                            break

        if choice == 'c':
            print(password_c)
            print("The password is above this line dont share it with anyone.")
            choice3 = input("Do you want to answer a question yes/no: ")
            print(choice3)
            if choice3 == 'yes':
                question_num = random.randint(0, len(questions) - 1)
                question = questions[question_num]
                answer = answers[question_num]
                user_answer = input("Question: " + question + "\nAnswer: ")
                if user_answer.lower() == answer.lower():
                    print("Correct!")
                    fb_3 = input("What is your experience after using Random Password Generator good/bad: ")
                    if fb_3 == 'good':
                        print("Thankyou for the feedback! Meet you again next time:).")
                        break
                    else:
                        if fb_3 == 'bad':
                            print("Sorry for the inconvenience. Meet you again next time.")
                            break
                        else:
                            print("It's a typo. Meet you again next time.")
                            break
                else:
                    print("Sorry, the correct answer is " + answer)
                    fb_3 = input("What is your experience after using Random Password Generator good/bad: ")
                    if fb_3 == 'good':
                        print("Thankyou for the feedback! Meet you again next time:).")
                        break
                    else:
                        if fb_3 == 'bad':
                            print("Sorry for the inconvenience. Meet you again next time.")
                            break
                        else:
                            print("It's a typo. Meet you again next time.")
                            break
            else:
                if choice3 == 'no':
                    fb_3 = input("What is your experience after using Random Password Generator good/bad: ")
                    if fb_3 == 'good':
                        print("Thankyou for the feedback! Meet you again next time:).")
                        break
                    else:
                        if fb_3 == 'bad':
                            print("Sorry for the inconvenience. Meet you again next time.")
                            break
                        else:
                            print("It's a typo. Meet you again next time.")
                            break

        if choice == 'd':
            print(password_d)
            print("The password is above this line dont share it with anyone.")
            choice4 = input("Do you want to answer a question yes/no: ")
            print(choice4)
            if choice4 == 'yes':
                question_num = random.randint(0, len(questions) - 1)
                question = questions[question_num]
                answer = answers[question_num]
                user_answer = input("Question: " + question + "\nAnswer: ")
                if user_answer.lower() == answer.lower():
                    print("Correct!")
                    fb_4 = input("What is your experience after using Random Password Generator good/bad: ")
                    if fb_4 == 'good':
                        print("Thankyou for the feedback! Meet you again next time:).")
                        break
                    else:
                        if fb_4 == 'bad':
                            print("Sorry for the inconvenience. Meet you again next time.")
                            break
                        else:
                            print("It's a typo. Meet you again next time.")
                            break
                else:
                    print("Sorry, the correct answer is " + answer)
                    fb_4 = input("What is your experience after using Random Password Generator good/bad: ")
                    if fb_4 == 'good':
                        print("Thankyou for the feedback! Meet you again next time:).")
                        break
                    else:
                        if fb_4 == 'bad':
                            print("Sorry for the inconvenience. Meet you again next time.")
                            break
                        else:
                            print("It's a typo. Meet you again next time.")
                            break
            else:
                if choice4 == 'no':
                    fb_4 = input("What is your experience after using Random Password Generator good/bad: ")
                    if fb_4 == 'good':
                        print("Thankyou for the feedback! Meet you again next time:).")
                        break
                    else:
                        if fb_4 == 'bad':
                            print("Sorry for the inconvenience. Meet you again next time.")
                            break
                        else:
                            print("It's a typo. Meet you again next time.")
                            break

        if choice == 'e':
            print(password_e)
            print("The password is above this line dont share it with anyone.")
            choice5 = input("Do you want to answer a question yes/no: ")
            print(choice5)
            if choice5 == 'yes':
                question_num = random.randint(0, len(questions) - 1)
                question = questions[question_num]
                answer = answers[question_num]
                user_answer = input("Question: " + question + "\nAnswer: ")
                if user_answer.lower() == answer.lower():
                    print("Correct!")
                    fb_5 = input("What is your experience after using Random Password Generator good/bad: ")
                    if fb_5 == 'good':
                        print("Thankyou for the feedback! Meet you again next time:).")
                        break
                    else:
                        if fb_5 == 'bad':
                            print("Sorry for the inconvenience. Meet you again next time.")
                            break
                        else:
                            print("It's a typo. Meet you again next time.")
                            break
                else:
                    print("Sorry, the correct answer is " + answer)
                    fb_5 = input("What is your experience after using Random Password Generator good/bad: ")
                    if fb_5 == 'good':
                        print("Thankyou for the feedback! Meet you again next time:).")
                        break
                    else:
                        if fb_5 == 'bad':
                            print("Sorry for the inconvenience. Meet you again next time.")
                            break
                        else:
                            print("It's a typo. Meet you again next time.")
                            break
            else:
                if choice5 == 'no':
                    fb_5 = input("What is your experience after using Random Password Generator good/bad: ")
                    if fb_5 == 'good':
                        print("Thankyou for the feedback! Meet you again next time:).")
                        break
                    else:
                        if fb_5 == 'bad':
                            print("Sorry for the inconvenience. Meet you again next time.")
                            break
                        else:
                            print("It's a typo. Meet you again next time.")
                            break

        if choice == 'f':
            print(password_f)
            print("The password is above this line dont share it with anyone.")
            choice6 = input("Do you want to answer a question yes/no: ")
            print(choice6)
            if choice6 == 'yes':
                question_num = random.randint(0, len(questions) - 1)
                question = questions[question_num]
                answer = answers[question_num]
                user_answer = input("Question: " + question + "\nAnswer: ")
                if user_answer.lower() == answer.lower():
                    print("Correct!")
                    fb_6 = input("What is your experience after using Random Password Generator good/bad: ")
                    if fb_6 == 'good':
                        print("Thankyou for the feedback! Meet you again next time:).")
                        break
                    else:
                        if fb_6 == 'bad':
                            print("Sorry for the inconvenience. Meet you again next time.")
                            break
                        else:
                            print("It's a typo. Meet you again next time.")
                            break
                else:
                    print("Sorry, the correct answer is " + answer)
                    fb_6 = input("What is your experience after using Random Password Generator good/bad: ")
                    if fb_6 == 'good':
                        print("Thankyou for the feedback! Meet you again next time:).")
                        break
                    else:
                        if fb_6 == 'bad':
                            print("Sorry for the inconvenience. Meet you again next time.")
                            break
                        else:
                            print("It's a typo. Meet you again next time.")
                            break
            else:
                if choice6 == 'no':
                    fb_6 = input("What is your experience after using Random Password Generator good/bad: ")
                    if fb_6 == 'good':
                        print("Thankyou for the feedback! Meet you again next time:).")
                        break
                    else:
                        if fb_6 == 'bad':
                            print("Sorry for the inconvenience. Meet you again next time.")
                            break
                        else:
                            print("It's a typo. Meet you again next time.")
                            break

        if choice == 'g':
            print(password_g)
            print("The password is above this line dont share it with anyone.")
            choice7 = input("Do you want to answer a question yes/no: ")
            print(choice7)
            if choice7 == 'yes':
                question_num = random.randint(0, len(questions) - 1)
                question = questions[question_num]
                answer = answers[question_num]
                user_answer = input("Question: " + question + "\nAnswer: ")
                if user_answer.lower() == answer.lower():
                    print("Correct!")
                    fb_7= input("What is your experience after using Random Password Generator good/bad: ")
                    if fb_7 == 'good':
                        print("Thankyou for the feedback! Meet you again next time:).")
                        break
                    else:
                        if fb_7 == 'bad':
                            print("Sorry for the inconvenience. Meet you again next time.")
                            break
                        else:
                            print("It's a typo. Meet you again next time.")
                            break
                else:
                    print("Sorry, the correct answer is " + answer)
                    fb_7 = input("What is your experience after using Random Password Generator good/bad: ")
                    if fb_7 == 'good':
                        print("Thankyou for the feedback! Meet you again next time:).")
                        break
                    else:
                        if fb_7 == 'bad':
                            print("Sorry for the inconvenience. Meet you again next time.")
                            break
                        else:
                            print("It's a typo. Meet you again next time.")
                            break
            else:
                if choice7 == 'no':
                    fb_7 = input("What is your experience after using Random Password Generator good/bad: ")
                    if fb_7 == 'good':
                        print("Thankyou for the feedback! Meet you again next time:).")
                        break
                    else:
                        if fb_7 == 'bad':
                            print("Sorry for the inconvenience. Meet you again next time.")
                            break
                        else:
                            print("It's a typo. Meet you again next time.")
                            break
