import random

class Card:

    def __init__(self):
        self.points =0


    def card(self):
        self.dealer_card_selection = random.randint(1,13)
        print(f"The dealer card is {self.dealer_card_selection}.")
        player_guess = input ("Do you belive the card will be higher or lower? [H/L]: ")
        self.next_card_selection = random.randint(1,13)
        print (f"The next card value is {self.next_card_selection}")
        if player_guess.upper() == "H" and self.dealer_value > self.next_card_value\
        or player_guess.upper() == "L" and self.dealer_value < self.next_card_value:
            self.score_adjustment = 100
            print ("You were correct!  You earned 100 points!")

        elif player_guess.upper() == "H" and self.dealer_value < self.next_card_value\
        or player_guess.upper() == "L" and self.dealer_value > self.next_card_value:
            self.score_adjustment = -75
            print ("You were incorrect!  You loss 75 points!")
