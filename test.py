import os
import time
from pokemon import Pokemon
from colors import bcolors


def colorText(color, text):
    return color + text + bcolors.ENDC


pokemon = bcolors.OKBLUE + 'Pokémon' + bcolors.ENDC
pytn = bcolors.OKGREEN + 'PYTHON' + bcolors.ENDC


def welcome():
    print('************************************')
    print('************************************')
    print('********* ', pokemon, pytn, ' *********')
    print('************************************')
    print('************************************')


def countdownF(countdown):
    for count in reversed(range(1, countdown+1)):
        print(count)
        time.sleep(1)


def getNumber():
    try:
        val = int(input())
        return val
    except ValueError:
        print("Hey! era un número")


def startBattle(pokemon1: Pokemon, pokemon2: Pokemon):
    os.system('cls')  # For Windows
    print("""
   _       ___  __  __    __  _      __    _
  /_\     / _ \/__\/ /   /__\/_\    /__\  /  /
 //_\/   / /_)/_\ / /   /_\ //_\/  / \// /  /
/  _  \ / ___//__/ /___//__/  _  \/ _  \/\_/
\_/ \_/ \/   \__/\____/\__/\_/ \_/\/ \_/\/
  """)
    print(pokemon1.name() + ' versus ' + pokemon2.name())
    print('Escoge un número para atacar!')
    print(' 1. Tackle')
    print(' 2. Growl')
    print(' 3. Bubblebean')
    print(' 4. Water Gun')
    ataque = getNumber()
    countdownF(3)
    print('Esta parte aún no está implementada, te toca a ti terminar este juego!')
    time.sleep(5)
    byebye()


def dialogF(pokemon1: Pokemon, pokemon2: Pokemon):
    print('Escogiste ' + pokemon1.name())
    time.sleep(2)
    print('Gary: Pfff Ya que escojiste ' + pokemon1.name() +
          ' es mi turno de escoger el mejor pokemon.')
    time.sleep(2)
    print('Gary escogió ' + pokemon2.name())
    time.sleep(2)
    print('Gary: ' + pokemon2.name() + ', bienvenido al equipo de las estrellas')
    time.sleep(2)
    print('Gary: Antes de que me convierta en el mejor entrenador dejaré que mi ' +
          pokemon2.name() + ' le de una paliza a tu ' + pokemon1.name())
    time.sleep(2)
    input('Presiona una tecla para continuar...')
    startBattle(pokemon1, pokemon2)


def choose(name):
    print('Hola ' + colorText(bcolors.HEADER, name) +
          ', bienvenido al mostrador del ' + colorText(bcolors.OKBLUE, 'Profesor') + ' ! A quién escogerás?')
    print('Escoge a tu pokemon!')
    print(' 1. El tipo planta ' + colorText(bcolors.OKGREEN, 'Bulbasaur'))
    print(' 2. El tipo fuego ' + colorText(bcolors.FAIL, 'Charmander'))
    print(' 3. El tipo agua ' + colorText(bcolors.OKBLUE, 'Squirtle'))
    pokemon = getNumber()
    if pokemon == 1:
        selected = Pokemon('Bulbasaur', bcolors.OKGREEN, 'planta')
        gary = Pokemon('Bulbasaur2', bcolors.OKGREEN, 'planta2')
    elif pokemon == 2:
        selected = Pokemon('Charmander', bcolors.FAIL, 'fuego')
        gary = Pokemon('Bulbasaur2', bcolors.OKGREEN, 'planta2')
    elif pokemon == 3:
        selected = Pokemon('Squirtle', bcolors.OKGREEN, 'agua')
        gary = Pokemon('Bulbasaur2', bcolors.OKGREEN, 'planta2')
    else:
        print('No escogiste un pokemon :(')
        time.sleep(2)
        byebye()
        exit()

    dialogF(selected, gary)


def byebye():
    import os
    os.system('cls')  # For Windows
    print(
        """
                                  ,'-
    _.----.        ____         ,'  _\   ___    ___     ____
_,-'       `.     |    |  /`.   \,-'    |   \  /   |   |    \  |`.
\      __    \    '-.  | /   `.  ___    |    \/    |   '-.   \ |  |
 \.    \ \   |  __  |  |/    ,','_  `.  |          | __  |    \|  |
   \    \/   /,' _`.|      ,' / / / /   |          ,' _`.|     |  |
    \     ,-'/  /   \    ,'   | \/ / ,`.|         /  /   \  |     |
     \    \ |   \_/  |   `-.  \    `'  /|  |    ||   \_/  | |\    |
      \    \ \      /       `-.`.___,-' |  |\  /| \      /  | |   |
       \    \ `.__,'|  |`-._    `|      |__| \/ |  `.__,'|  | |   |
        \_.-'       |__|    `-._ |              '-.|     '-.| |   |
                                `'                            '-._| Hecho con {} por {}
        """.format(colorText(bcolors.FAIL, '<3'), colorText(bcolors.HEADER, 'Walter Leturia'))
    )


# pikachu = Pokemon('Pikachu', bcolors.WARNING, 'Electrico')
# pikachu.saludar()


# byebye(os)

# print(bcolors.WARNING + "Warning: No active frommets remain. Continue?" + bcolors.ENDC)
# print(bcolors.OKBLUE + "Warning: No active frommets remain. Continue?" + bcolors.ENDC)
# print(bcolors.OKGREEN + "Warning: No active frommets remain. Continue?" + bcolors.ENDC)

welcome()
name = input('Cuál es tu nombre? ')
choose(name)
