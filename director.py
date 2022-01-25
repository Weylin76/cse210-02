from game.card import Card

class Director:
    """
    A person who directs the game.

    The responsibility of hte Director is to control the sequence of the play.

    Attributes:
    random_card_selection (random int)
    is_playing (boolean)
    score (int)
    score_adjustment
    """

    def __init__(self):
        self.dealer_card_selection = 0
        self.next_card_selection = 0
        self.is_playing = True
        self.total_score = 300
        self.score_adjustment = 0

    def start_game(self):
        while self.is_playing:
            self.get_inputs()
            self.do_updates()
            self.do_outputs()

    def get_inputs(self):
        """
        Ask user if they want to continue to play.

        Args: self(Director): An instance of the Director.
        """
        play_again = input("Do you wnat to play again? [Y/N] ")
        self.is_playing = (play_again.upper =="Y")

    def do_updates(self):
        """
        Updates the player's score.

        Args:
        self(Director): An instance of the Director.
        """
        if not self.is_playing:
            return
        
        self.total_score += self.score_adjustment
        print(f"Your total point value is now {self.total_score}")
    
    def do_outputs(self):
        """
        Display current score.  Ask the player if they wish to continue.

        Args:
        self(Director): An instance of the Director.
        """
        if not self.is_playing:
            return
    
        self.is_playing == (self.score >0)