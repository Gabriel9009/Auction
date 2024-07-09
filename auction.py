import os

bidders = {}
name = input("What is your name: ")
bid = int(input("What is your bid: "))
question = input("Are there any other bidders? Type 'yes' or 'no'. ").lower()

bidders[name] = bid

top_bid = 0
highest_bidder = ""

while question == "yes" or question == "y":
    os.system("cls")
    name = input("What is your name: ")
    bid = int(input("What is your bid: "))
    bidders[name] = bid
    question = input("Are there any other bidders? Type 'yes' or 'no'. ").lower()

    if question == "no" or question == 'n':
        for name, amount in bidders.items():
            if amount > top_bid:
                top_bid = amount
                highest_bidder = name

print(f"The winner is {highest_bidder} with bid of {top_bid}")