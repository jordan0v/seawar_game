import re
import random
import math


def is_web():
    return "__BRYTHON__" in globals()

def write(message, end='\n'):
    if is_web():
        from browser import document
        console = document.getElementById('console')
        p = document.createElement('p')
        p.textContent = '> ' + message
        console.appendChild(p)
        console.scrollTop = console.scrollHeight
    else:
        print(message, end=end)


async def read():
    if is_web():
        from browser import document, aio
        inp = document.getElementById('input')
        while True:
            event = await aio.event(inp, 'keydown')
            if event.key == 'Enter':
                tmp = event.target.value
                event.target.value = ''
                write(tmp)
                return tmp
    else:
        return input()


def run(function):
    if is_web():
        from browser import aio
        aio.run(function)
    else:
        import asyncio
        asyncio.run(function)


async def game():
    
    write("\t\t\tSEAWAR")
    write("\t\t  CREATIVE COMPUTING")
    write("\t\tMORRISTOWN, NEW JERSEY")
    write("\n" * 3)
    write("YOU COMMAND A FLEET OF SHIPS OPERATING IN")
    write("ENEMY TERRITORY!!!")
    write("DO YOU NEED ANY ASSISTANCE? (YES/NO): ")
    need_assistance = await read()
    while need_assistance.upper() not in ["YES", "NO"]:
        write("INPUT 'YES' OR 'NO'")
        need_assistance = await read()
    if need_assistance.upper() == "YES":
        write("YOU TELL YOUR GUN CREWS THE ELEVATION TO SET THEIR GUNS.")
        write("ELEVATION IS IN DEGREES FROM 0 TO 360.")
        write("\nYour task force consists of 3 destroyers, 2 cruisers,")
        write("2 battleships, and 2 heavy aircraft carriers.")
        write("The enemy has 9 ships for defense.")
        write("If you succeed in sinking all his ships before he sinks")
        write("yours, you have won. However, if he sinks all your ships")
        write("before you have defeated him, you have lost!!")
    write("Let us begin!!!\n")
    round_count = 0
    enemy_ships = 9
    your_ships = 9
    ships = [
            "AIRCRAFT CARRIER", "U-BOAT", "TORPEDO BOAT",
            "E-TYPE DESTROYER", "GUIDED-MISSILE SHIP", "HEAVY FRIGATE",
            "BATTLESHIP", "TORPEDO BOAT", "HEAVY FRIGATE"]
    while enemy_ships > 0 and your_ships > 0:
        round_count += 1
        target_ship = random.choice([
            "AIRCRAFT CARRIER", "U-BOAT", "TORPEDO BOAT",
            "E-TYPE DESTROYER", "GUIDED-MISSILE SHIP", "HEAVY FRIGATE",
            "BATTLESHIP", "TORPEDO BOAT", "HEAVY FRIGATE"])
        write('\n')
        #write(f"ROUND {round_count}")

        write(f"\nYour flagship reports the sighting of an enemy {target_ship}")

        range_to_target = 43000 - 30000 * random.uniform(0, 1) + (random.uniform(0, 1) * 10) * 0.987654 + 102
        while range_to_target < 10000:
            range_to_target = 43000 - 30000 * random.uniform(0, 1) + (random.uniform(0, 1) * 10) * 0.987654 + 102
        write(f"Your instruments read the range to the target as {int(range_to_target)} meters.")
        write('WHAT ELEVATION ** ')
        shot_angle = int(await read())
        while 90 <= shot_angle or shot_angle <= 0:
            if your_ships == 0:
                continue
            if 90 < shot_angle < 180:
                write("HEY STUPID, YOU'RE FIRING ON YOUR OWN SHIPS!!!")
                write('WHAT ELEVATION ** ')
                your_ships -= random.randint(0, 1)
            elif shot_angle == 90:
                write("YOU IDIOT!! YOU SHOT STRAIGHT UP!!, AND THE SHELL")
                write("LANDED ON YOUR OWN GUN POSITION, DESTROYING IT!!!")
                write('WHAT ELEVATION ** ')
                your_ships -= 1
            elif shot_angle == 0 or 180 <= shot_angle <= 360:
                write("WHAT ARE YOU TRYING TO DO?? DRILL A NEW HATCH?? THE SHELL")
                write('WHAT ELEVATION ** ')
                your_ships -= random.randint(0, 1)
            elif 360 < shot_angle or shot_angle < 0:
                write("WHERE DID U LEARN TO TYPE? DEGREES EXCEEDS 360 BY")
                write('WHAT ELEVATION ** ')
                your_ships -= random.randint(0, 1)
            shot_angle = int(await read())
        write('\n\n-----FIRE!!!')
        target_ship = random.choice(ships[:])
        v1 = 675.285
        e = int(range_to_target - (v1**2 / 9.80665 * math.sin(2*shot_angle/57.3)))
        if abs(e) <= 4000:
            write('DEPTH CHARGE EXPLODED RIGHT ON TOP OF THAT BABY!!!')
            enemy_ships -= 1
            your_ships -= random.randint(0, 1)
        elif e > 100:
            write(f'DEPTH CHARGE EXPLODED {abs(e)} METERS AFT OF TARGET.')
            your_ships -= random.randint(0, 1)
        elif e < -100:
            write(f'DEPTH CHARGE EXPLODED {abs(e)} METERS SHORT OF TARGET.')
            your_ships -= random.randint(0, 1)
    write("            ********  PEACE  ********")
    if your_ships == 0:
        write("ALL OF YOUR SHIPS HAVE BEEN SUNK.  SO SORRY")
        write("THE BATTLE IS OVER..........THE ENEMY WINS!")
    else:
        write("YOU HAVE DECIMATED THE ENEMY..........THAT'S NICE")
        write("THE BATTLE IS OVER..........YOU WIN!!!!!")


run(game())
