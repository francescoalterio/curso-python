import random
import time
import os
from colorama import Back, Fore, Style,init
init()

PLAYER_COLORS = (Fore.BLUE, Fore.GREEN, Fore.RED, Fore.YELLOW, Fore.CYAN, Fore.MAGENTA, Fore.WHITE)
PLAYER_COLORS_TITLE = ("AZUL", "VERDE", "ROJO", "AMARILLO", "CIAN", "MAGENTA", "BLANCO")
CAR_CHARACTER = "*"

def preparation(number_of_players):
    print("Selecciona tu color:")
    for index in range(0, number_of_players):
        print(PLAYER_COLORS[index] + PLAYER_COLORS_TITLE[index])
    print(Style.RESET_ALL)

def race(number_of_players):
    max_movement = 3
    finish = 100
    players_position = [0] * number_of_players
    time_to_refresh = 1

    # Pintando linea de carrera
    line = ""
    for color in PLAYER_COLORS:
        line += Style.RESET_ALL + color + CAR_CHARACTER +" "
    print(line)

    while max(players_position) < finish:
        time.sleep(time_to_refresh)
        os.system('cls')
        for index, position in enumerate(players_position):
            players_position[index] += random.randint(1, max_movement)
    
        max_row = max(players_position)
        window = []
        for row in range(0, max_row + 1):
            line = ""
            for column in range(0, number_of_players):
                car_position = players_position[column]
                if row < car_position:
                    line += Style.RESET_ALL + PLAYER_COLORS[column] + "|" + " "
                elif row == car_position:
                    line += Style.RESET_ALL + PLAYER_COLORS[column] + "*" + " "
                else:
                    line += " " + " "
            window.append(line)
        
        line_concatened = ""
        for line in window:
            line_concatened += line + "\n"
        print(line_concatened)
    
    return players_position
        
def podium(players_position):
    number_of_players = len(players_position)
    players_position_copy = players_position.copy()

    result_list = []
    for index in range(0, number_of_players):
        result_of_player = max(players_position_copy)
        number_index = players_position_copy.index(result_of_player)
        # Determinar la posición de podio correctamente
        if len(result_list) > 0 and result_of_player == result_list[-1]['result']:
            podium_position = result_list[-1]['podium_position']
        else:
            podium_position = len(result_list) + 1
        data = {
            'result': result_of_player,
            'podium_position': podium_position,
            'foreground': PLAYER_COLORS[number_index],
            'color_title': PLAYER_COLORS_TITLE[number_index]
        }
        result_list.append(data)
        players_position_copy[number_index] = 0

    for data in result_list:
        print(Style.RESET_ALL + str(data['podium_position']) + "." + " " + data['foreground'] + data["color_title"] + " - " + str(data['result']))


def main():
    number_of_players = 0
    while True:
        question_of_players = input("Cuantos corredores son? maximo de jugadores (7): ")
        try:
            to_int = int(question_of_players)
            if to_int < 0 or to_int > len(PLAYER_COLORS):
                print(f"El maximo de jugadores es ({len(PLAYER_COLORS)}), usted ingreso ({to_int})")
                continue
            number_of_players = to_int
            break
        except:
            print("Tiene que ingresar un numero valido")

    while True:
        preparation(number_of_players)
        ready = input("Estas listo para empezar? (s/n)")
        if ready.lower() == "s":
            break 
    
    players_position = race(number_of_players)
    podium(players_position)
main()