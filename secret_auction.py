
logo = """
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________
                         `'-------'`
                       .-------------.
                      /_______________
                       """
                       
print(logo)

bidders = {}

add_bidder = True
while add_bidder:
    name = input("Enter your name? ")
    bid = int(input("How much do you want to bid? $"))

    bidders[name] = bid

    other_bidders = input("Are there any other bidders? Type 'y' or 'n' :")

    if other_bidders == "n":
        add_bidder = False
        winning_bidder = ""
        winning_bid = 0
        for person in bidders:
            bid = bidders[person]
            if bid > winning_bid:
                winning_bid = bid
                winning_bidder = person
        print(f"The winning bidder is {winning_bidder} with a bid amount of ${winning_bid}")
                
