from random import randint
from math import sqrt

GAME_WIDTH = 10
GAME_HEIGHT = 10

key_x = randint(0, GAME_WIDTH)
key_y = randint(0, GAME_HEIGHT)

print(key_x, key_y)

player_x = 0
player_y = 0
player_found_key = False

distance_before = sqrt((key_x - player_x) ** 2 + (key_y - player_y) ** 2)

steps = 0

while not player_found_key:
    steps += 1
    print()
    print("Możesz udać się w kierunkach określonych jako [W/A/S/D]")
    move = input('Dokąd idziesz? ')
    match move.lower():
        case 'w':
            player_y += 1
            if player_y > GAME_HEIGHT:
                print("Auć! Uderzasz w ścianę!")
                player_y = GAME_HEIGHT
        case 's':
            player_y -= 1
            if player_y < 0:
                print("Auć! Uderzasz w ścianę!")
                player_y = 0
        case 'a':
            player_x -= 1
            if player_x < 0:
                print("Auć! Uderzasz w ścianę!")
                player_x = 0
        case 'd':
            player_x += 1
            if player_x > GAME_WIDTH:
                print("Auć! Uderzasz w ścianę!")
                player_x = GAME_WIDTH
        case 'q':
            print("Koniec gry")
            quit()
        case '-':
            print("Nie wiem dokąd idziesz :(")
            continue

    if player_x == key_x and player_y == key_y:
        print("Gorąco!")
        print(f"Wygrałxś w {steps} ruchach.")
        quit()

    distance_after = sqrt((key_x - player_x) ** 2 + (key_y - player_y) ** 2)

    if distance_before > distance_after:
        print("Cieplej")
    else:
        print("Zimnej")
    distance_before = distance_after
    print(player_x, player_y)