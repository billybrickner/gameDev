import random

def hit(pip1, pip2, ac2):
    values = [  (  2, 19),
                (  3, 18),
                (  4, 17),
                (  6, 16),
                (  8, 15),
                ( 11, 14)]
    r = random.randint(1,20)
    #print("Roll:", r)
    value = values[pip1]
    if r <= value[0]:
        r2 = random.randint(1,20)
        if r2 > ac2 + 2*pip2 + 6:
            return 10
        else:
            return 0
    elif r <= value[1]:
        r2 = random.randint(1,20)
        if r2 > ac2 + 2*pip2:
            return 20
        else:
            return 0
    else:
        return 40


def main():
    winRate = [[0 for i in range(6)] for _ in range(6)]
    for x in range(6):
        for y in range(6):
            p1 = 0
            trials = 10000
            for i in range(trials):
                health1 = [70]
                health2 = [70]
                player = 1
                while health1[0] > 0 and health2[0] > 0:
                    if player == 2:
                        player = 1
                        health = health2
                        pip1 = y
                        pip2 = x

                    else:
                        player = 2
                        health = health1
                        pip1 = x
                        pip2 = y
                    health[0] -= hit(pip1, 5 - pip2, 6)
                # print("P1: ", health1[0])
                # print("P2: ", health2[0])
                if health1[0] > 1:
                    p1 += 1
            print("X: ", x, "Y: ", y)
            # print("Results: ", p1/trials)
            winRate[x][y] = p1/trials
    print("     ", end="")
    for i in range(6):
        print(f"p1 {i+1:3d}", end=" ")
    print()
    for i, row in enumerate(winRate):
        print(f"p2 {i+1:1d}", end=" ")
        for elem in row:
            print(f"{elem:0.4f}", end=" ")
        print()
    
        


main()
