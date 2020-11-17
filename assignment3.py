import random
import socket
import time
from _thread import *
import threading
from datetime import datetime
import json
import math



gamersList = [['Emil',1000],
              ['Tobias',850],
              ['Linus',800],
              ['Mark',1000],
              ['Lisa',1800],
              ['Tiffany',1250],
              ['Melissa',900],
              ['Dave',1500],
              ['Eli',1200],
              ['Lindsey',1425]
              ]


# to print the player data base
def showPlayers():
    print(*gamersList, sep = "\n")
    print("")


def simPlayerJoin():
    p1 = random.randint(0,9)
    p2 = random.randint(0,9)
    if p1 == p2:
        p2 = random.randint(0,9)
    return p1,p2
        

def simBattle():
    p1,p2 = simPlayerJoin()

    #prints the players joining the game
    print(gamersList[p1][0] + " have joined the game")
    print(gamersList[p1])
    print(gamersList[p2][0] + " have joined the game")
    print(gamersList[p2])

    while True:
        #ask the user to simulate the number of rounds
        battleNumber = input("pick the number of rounds: ")
        try:
            num = int(battleNumber)
            break;
        except ValueError:
            print("This is not a number. Enter a valid number")

    p1Score = 0
    p2Score = 0
    
    i = 0
    while i < num:
        p1x = random.randint(0,100)
        p2x = random.randint(0,100)
        if p1x > p2x:
            p1Score += 1
            print(gamersList[p1][0] + " wins a point")
        if p1x < p2x:
            p2Score += 1
            print(gamersList[p2][0] + " wins a point")
        i += 1
        if i == num:
            if p1Score > p2Score:
                print(gamersList[p1][0] + " wins the game!")
            if p1Score < p2Score:
                print(gamersList[p2][0] + " wins the game!")
            if p1Score == p2Score:
                print("It is a tie!")

    
    x = gamersList[p1][1] #player 1 elo
    y = gamersList[p2][1] #player 2 elo
    
    x1 = ((y + 400 * (p1Score - p2Score))/num) 
    y1 = ((x + 400 * (p2Score - p1Score))/num) 

    gamersList[p1][1] = x + round(x1)
    gamersList[p2][1] = y + round(y1)
    print(gamersList[p1])
    print(gamersList[p2])
    print("")


def main():
    while True:
        print("1. Print active players")
        print("2. Start Simulation")
        print("3. End program")
        txt = input("pick ")
        print("")
        if txt == "1":
            showPlayers()
        if txt == "2":
            simBattle()
        if txt == "3":
            break
        

main()