import random
import time
import game_1d.player

def dramatic_pause():
    time.sleep(2 + random.random()*2)

def card(card_text):
    print("--------------------")
    print(card_text)
    print("--------------------")


class game():
    def __init__(self):
        print('Welcome to 1-D Gladiators')
        #create characters
        card("Character Creation")
        NUMBER_OF_PLAYERS = 2
        self.players = [player.player() for i in range(NUMBER_OF_PLAYERS)]
        BOARD_SIZE = 10
        self.board = [0 for i in range(BOARD_SIZE)]
        # Set positions
        self.players[0].position = 3
        self.players[1].position = 7
        card("Turn Order")
        choose = random.randint(0,NUMBER_OF_PLAYERS-1)
        self.curr_player = self.players[choose]
        self.opponent = self.players[(choose + 1)%NUMBER_OF_PLAYERS]
        print("%s Goes First" % self.curr_player.name)
        self.repeat = True
        while self.repeat == True:
            self.game_end = False
            self.loop()
            card("Play Again?")
            self.repeat = "N" != input("Play again (N to stop)?")
        card("Game End")


    def hit(self):
        hit_chances = [ (  2, 20),
                        (  3, 19),
                        (  4, 18),
                        (  6, 17),
                        (  8, 16),
                        ( 11, 15)]
        weak_hit, strong_hit = hit_chances[self.curr_player.attack_pips-1]
        attacks = ["Riposte", "Parry", "Jab", "Slash", "Lunge", "Overhead Swing"]
        card("Attack")
        print("Attack Type:    ",attacks[self.curr_player.attack_pips])
        print("Weak hit roll:  ", weak_hit)
        print("Strong hit roll:", strong_hit)
        print("Your roll:      ", end=' ')
        dramatic_pause()
        r = random.randint(1,20)
        print("%2d" % r, end = " ")
        r2 = random.randint(1,20)
        if r <= weak_hit:
            print("(Weak hit)")
            print("Miss chance: ", float(self.opponent.ac+2*self.opponent.defense_pips+6)/20*100)
            dramatic_pause()
            if r2 > self.opponent.ac + 2*self.opponent.defense_pips + 6:
                print("Hit confirmed! [10 Damage]")
                return 10
            else:
                print("Attack Missed")
                return 0
        elif r < strong_hit:
            print("(Hit)")
            print("Miss chance: ", float(self.opponent.ac+2*self.opponent.defense_pips)/20*100)
            dramatic_pause()
            if r2 > self.opponent.ac + 2*self.opponent.defense_pips:
                print("Hit confirmed! [20 Dammage]")
                return 20
            else:
                print("Attack Missed")
                return 0
        else:
            print("(Critical)")
            print("CRITICAL HIT [40 Damage]")
            return 40

    def loop(self):
        while self.game_end == False:
            card("%s Turn" % self.curr_player.name)
            self.curr_player.attack_pips = int(input("Attack strength(0-5): "))
            self.curr_player.defense_pips = 5 - self.curr_player.attack_pips
            self.opponent.health -= self.hit()

            card("STATUS")
            for player in self.players:
                print("%10s Health %4d" %(player.name, player.health))
                if player.health < 0:
                    game_end = True
            self.curr_player, self.opponent = self.opponent, self.curr_player


