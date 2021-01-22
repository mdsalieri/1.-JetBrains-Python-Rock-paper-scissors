import random

# Write your code here
current_rating = 0
rating_dict = {}
rating_file = open("rating.txt", "r")
for line in rating_file:
    nick, score = line.split()
    rating_dict[nick] = score
rating_file.close()


def rating_check(nickname):
    if nickname in rating_dict:
        print(f"Your rating: {current_rating + int(rating_dict[nickname])}")
    else:
        print(f"Your rating: {current_rating}")


def win_check(user, comp):
    user_index = actions_list.index(user) + 1
    comp_index = actions_list.index(comp) + 1
    difference = user_index - comp_index
    if difference < 0:
        difference = len(actions_list) + (user_index - comp_index)
    if len(actions_list) // 2 >= difference:
        return True
    else:
        return False


username = input("Enter your name: ")
print(f"Hello, {username}")

actions_list = input().split(",")
if actions_list[0] == "":
    actions_list = ['rock', 'paper', 'scissors']
print("Okay, let's start")

while True:
    user_action = input()
    random.seed()
    comp_action = random.choice(actions_list)
    if user_action == "!exit":
        print("Bye!")
        break
    elif user_action in actions_list:
        if comp_action == user_action:
            print(f'There is a draw ({comp_action})')
            current_rating += 50
        else:
            win = win_check(user_action, comp_action)
            if win:
                print(f'Well done. The computer chose {comp_action} and failed')
                current_rating += 100
            else:
                print(f'Sorry, but the computer chose {comp_action}')
    elif user_action == "!rating":
        rating_check(username)
    else:
        print("Invalid input")
