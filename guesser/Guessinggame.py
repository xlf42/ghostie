#!/usr/bin/env python3
'''
Created on 19.11.2020

@author: axel
'''

import os


# snippet to clear the terminal window
clear = lambda: os.system('cls' if os.name=='nt' else 'clear')

if __name__ == '__main__':
    zahl = 0
    while (zahl < 1 or zahl > 100):
        s = input("Spieler 1: Gib die zu ratende Zahl zwischen 1 und 100 ein: ")
        if not s.isdecimal():
            print('Bitte gib nur Zahlen ein')
            continue
        zahl = int(s)
        if (zahl < 1 or zahl > 100):
            print('Bitte gib eine Zahl zwischen 1 und 100 ein')
        
    clear();
    found = False
    tries = 0
    while (not found):
        tries += 1
        i = int(input('Dein '+str(tries)+'. Versuch: '))
        if (i > zahl):
            print('Die gesuchte Zahl ist kleiner als ' + str(i))
        elif (i < zahl):
            print('Die gesuchte Zahl ist groesser als ' + str(i))
        else:
            print('Du hast die gesuchte Zahl erraten')
            found = True
            
    print('Du hast ' + str(tries) + ' Versuche gebraucht')
    
