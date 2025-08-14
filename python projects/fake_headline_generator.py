# 1- import the random module
import random

# 2- create subjects
subjects = [
    "Shaharukh khan",
    "Virat kohli",
    "A Mumbai cat",
    "A Group of Monkeys",
    "Prime Minister Modi",
    "Auto Rickshaw Driver from Delhi"
]

actions = [
    "launches",
    "cancels",
    "dances with",
    "eates",
    "declares war on",
    "orders",
    "celebrates"
]

places_or_things = [
    "at Red Fort",
    "in Mumbai Local Train",
    "a plate of samosa",
    "inside partliament",
    "at Ganga Ghat",
    "during IPL Match",
    " at India Gate"
]

# 3 start the headline generation loop
while True:
    subject = random.choice(subjects)
    action = random.choice(actions)
    place_or_thing = random.choice(places_or_things)

    headline = f" BREAKING NEWS: { subject} {action} {place_or_thing}"
    print("\n" + headline)
    user_input = input("\nDo you want another headline? (yes/no)").strip().casefold
    if user_input == "no":
        break

    #print goodbye message
    print("\nThanks for using the Fake News Headline Generator. Have a fun day")

 