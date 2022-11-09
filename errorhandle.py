import pygame as py
import math as ma 

while True:
    try: 
        from sett import *
    except Exception as i:
        print("error (sett) >>")
        print(i) 

    try:    
        from menux import *
    except Exception as y:
        print("error (menu) >>")
        print(y)

    try:
        from player import *
    except Exception as z:
        print("error (player) >>")
        print(z)

    try:
        from main import *
    except Exception as x:
        print("error (main) >>")
        print(x)   
    break

