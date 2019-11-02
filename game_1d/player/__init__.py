class player():
    def __init__(self):
        print("Character creation")
        print("Enter Player Name: ", end='')
        self.name = input()
        print("Enter Player Symbol: ", end='')
        self.symbol = input()
        self.health = 70
        self.max_pips = 5
        self.attack_pips = 0
        self.defense_pips = 5
        self.move_pip = 0
        self.position = 0
        self.ac = 6

