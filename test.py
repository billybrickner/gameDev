import random

def hit(pip1, pip2, ac2):
    values = [  ( 2, 19),
                ( 3, 18),
                ( 4, 17),
                ( 6, 16),
                ( 8, 15),
                (1, 2)]
    r = random.randint(1,20)
    #print("Roll:", r)
    value = values[pip1]
    if r <= value[0]:
        r2 = random.randint(1,20)
        if r2 > ac2 + 2*pip2 + 5:
            return 15
        else:
            return 0
    elif r <= value[1]:
        r2 = random.randint(1,20)
        if r2 > ac2 + 2*pip2:
            return 30
        else:
            return 0
    else:
        return 45


def main():
    winRate = [[0 for i in range(6)] for _ in range(6)]
    for x in range(6):
        for y in range(6):
            p1 = 0
            trials = 1000
            for i in range(trials):
                health1 = [700]
                health2 = [700]
                player = random.randint(1,2)
                while health1[0] > 0 and health2[0] > 0:
                    if player == 2:
                        player = 1
                        health = health2
                        pip1 = x
                        pip2 = y

                    else:
                        player = 2
                        health = health1
                        pip1 = y
                        pip2 = x
                    health[0] -= hit(x,y,6)
                # print("P1: ", health1[0])
                # print("P2: ", health2[0])
                if health1[0] > 1:
                    p1 += 1
            print("X: ", x, "Y: ", y)
            print("Results: ", p1/trials)
            winRate[x][y] = p1/trials
    for row in winRate:
        print(row)
    
        


main()
