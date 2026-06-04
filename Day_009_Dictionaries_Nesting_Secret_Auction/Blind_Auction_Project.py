name_bid = {}
auction = True

while auction:
    name = input("What is your name?\n")
    bid = int(input("What is your bid?\n"))
    name_bid[name] = bid

    more = input("Are there more bids, 'yes', 'no' ? \n")
    if more == "no":
        auction = False


highest_bid = 0
highest_bidder = str()
for name in name_bid:
    if name_bid[name] > highest_bid:
        highest_bid = name_bid[name]
        highest_bidder = name


print(f"The highest bid is {highest_bidder} with a bid of {highest_bid}")
