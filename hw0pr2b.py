# coding: utf-8
#c
# hw0pr2b.py
# Jessica Farmer and Natalie Syverud worked together on this program.

""" 
Title for your adventure:   Hogwarts.

"""

import time

def adventure():
    """ this function runs one session of interactive fiction
        Well, it's "fiction," depending on the pill color chosen...
        arguments: no arguments (prompted text doesn't count as an argument)
        results: no results     (printing doesn't count as a result)
    """
    delay = 0.0          # change to 0.0 for testing or speed runs,
                         # ..larger for dramatic effect!

    username = input("What do they call you, worthy adventurer? ")

    print()
    print("Welcome,", username, "the Hogswarts Express, awaits")
    print("of mighty wonders and unreal magic... the learning begins!")
    print()

    print("Your quest: To find--and partake in--wizarding adventures!")
    print()

    thrill = input("What kind of Adventures await within our halls? ")

    if thrill == "three headed dogs":
        print("Wise! I hope you brought a song.")
    elif thrill == "trolls":
        print("Your wand many get a few boogies!")
    else:
        print("Hmm try an adventuous conquest in books 1-2")
    print()

    print("On to the quest!\n\n")
    print("A corridor stretches before you; its dim lighting portrays, a cat, It's Filch's Cat,")
    print("Quick grab the invisiblity cloak, throw Ron and Hermione under there with you,")
    print("The cat doesn't see you and walks away, look, what is that....spiders.")
    time.sleep(delay)
    print()

    choice1 = input("Do you choose to continue following the spiders or get Snape to kill them or return to your dormitory? [Spiders/Snape/Dormitory] ")
    print()

    if choice1 == "Spiders":
        print("As you follow the spiders, you notice theyre leading into the forbiden forrest.")
        time.sleep(delay)
        print("You succeed, in following the trail of Spiders.")
        print("Good job,", username, "!")
    elif choice1 == "Snape":
        print("500 points lost from Gryffindor")
    elif choice1 == "Dormitory":
        print("Your classmate was petrified the next day.")
    else:  
        print("You head back to your dormitory and hear...")
        time.sleep(delay)
        print("...a voice, only you can hear it, is that...two yellow eyes.")
        print("Good thing you had a mirror with you", username, ".")

    choice2 = input("Theres a dance coming up, do you ask Ginny? ")
    print()

    if choice2 == "Yes":
        print("Sorry shes already going with someone else")
    else:
        print("aww is the young harry potter afraid")
    
    choice3 = input("Ron just showed up at your window with a flying car, do you get in?[yes/no] ")
    print()

    if choice3 == "yes":
        print("well you escaped your aunt and uncles but are all over the news")
    elif choice3 == "no":
        print("looks like youre stuck at your aunts and uncles, hope you like your room")
    
    choice4 = input("How was your first couple of adventures at Hogwarts? ")
    print()

    if choice4 == "good":
        print("Full points", username,"!")
    print("Your first couple of years at Hogwarts was a success! You had some mighty adventures and barely escaped with your life. Go forth young adventurer!")

    