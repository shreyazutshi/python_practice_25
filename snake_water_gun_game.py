import random

op = ["snake", "water", "gun"]
r=1
comp_point = 0
user_point = 0
a= input("Are you ready for a snake, water, gun game? Type yes to start! ")
if a == "yes":
    print("Good luck! Let's start.")
    while r <=10:
        comp_choice = random.choice(op)
        user_choice = input("Choose your choice - Snake, Water, Gun:").strip().lower()
        if user_choice not in op:
            print("Invalid choice. Please choose among given options.")
            continue
        if user_choice == comp_choice:
            print("It's a draw.", 10-r, "chance left. Points after this round are :\n"
                              "Computer points:", comp_point, "and User points:", user_point)

        elif comp_choice == "snake" and user_choice == "water":
            comp_point += 1

            print("Uh oh, bad luck.", 10-r,"chance left. Points after this round are:\n"
                                "Computer points:", comp_point, "and User points:", user_point)

        elif comp_choice == "snake" and user_choice == "gun":

            user_point += 1
            print("Yay, Keep going!", 10-r,"chance left. Points after this round are:\n"
                                "Computer points:", comp_point, "and User points:", user_point)

        elif comp_choice == "water" and user_choice == "snake":

            user_point += 1
            print("Yay, Keep going!", 10-r,"chance left. Points after this round are:\n"
                                "Computer points:", comp_point, "and User points:", user_point)

        elif comp_choice == "water" and user_choice == "gun":
            comp_point += 1

            print("Uh oh, bad luck.", 10-r,"chance left. Points after this round are:\n"
                                "Computer points:", comp_point, "and User points:", user_point)

        elif comp_choice == "gun" and user_choice == "snake":
            comp_point += 1

            print("Uh oh, bad luck.", 10-r,"chance left. Points after this round are:\n"
                                "Computer points:", comp_point, "and User points:", user_point)

        elif comp_choice == "gun" and user_choice == "water":

            user_point += 1
            print("Yay, Keep Going!", 10-r,"chance left. Points after this round are:\n"
                                "Computer points:", comp_point, "and User points:", user_point)
        r+=1

    if comp_point > user_point:
        print("Sorry, you lose. Better luck next time.")
        print("Final scores are:\n", "Computer points:", comp_point, "and User points:", user_point)

    elif comp_point < user_point:
        print("Congrats, you win. Come back soon.")
        print("Final scores are:\n", "Computer points:", comp_point, "and User points:", user_point)


    else:
        print("It's a draw. Good try.")
        print("Final scores are:\n", "Computer points:", comp_point, "and User points:", user_point)

else:
    print("Okay! Come back soon.")
