print("Welcome to my web development quiz")

playing = input("Do you want to play? ").lower()


if playing != "yes":
    quit()

print("Alright let's play :)")
score = 0


question = input("What does CPU stand for? ").lower()
if question == "central processing unit":
    print('Correct!')
    score += 1
else:
    print("That's incorrect, please try again")

question = input("What does GPU stand for? ").lower()
if question == "graphics processing unit":
    print('Correct!')
    score += 1
else:
    print("That's incorrect, please try again")

question = input("What does RAM stand for? ").lower()
if question == "random access memory":
    print('Correct!')
    score += 1
else:
    print("That's incorrect, please try again")

question = input("What does PSU stand for? ").lower()
if question == "power supply unit":
    print('Correct!')
    score += 1
else:
    print("That's incorrect, please try again")


print("You got " + str(score) + " questions correct!")
print("You got " + str((score/4) * 100) + " %")
