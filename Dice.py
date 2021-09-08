# -*- coding: utf-8 -*-
"""
Created on Mon Aug  9 07:04:46 2021

@author: kalai
"""
import random
# snakes and ladders game app
 
# digitize the board, be creative with the data types
#    establish the starting position 1 
p1_position=p2_position=1
iteration=0
#    establish the ending position 100
d_end_position=100
#Ladder
Ladder = [(5,25), (10,29), (22,41), (28, 55), (44,95), (70,89), (79,81)]
#Snake
Snake = [(31, 14), (37, 17), (73, 53), (78, 39), (92, 35), (99, 7)]

p1=input('Enter the Name of player1 : ')
p2=input('Enter the Name of player2 : ')
while p1_position < d_end_position and p2_position < d_end_position:
    ladder_start=0
    Snake_start=0
    iteration+=1
    if not(iteration%2):
        dice_value=random.randint(1, 7)
        # if dice_value.isnumeric():
        #     dice_value=int(dice_value)
        #     dice_value=dice_value if 0<dice_value<7 else 0
        # else:
        #     print(f'Enter a valid dice value missed your current turn {p2}')
        #     continue
        
        if p2_position+dice_value>d_end_position:
            print(f'Current position of {p2} is {p2_position}')
            print(f'Current position of {p1} is {p1_position}')
            continue
        else:
            p2_position+=dice_value
        if [Ladder[i][0] for i in range(len(Ladder))].count(p2_position):
            ladder_start=[Ladder[i][0] for i in range(len(Ladder))].index(p2_position)
            p2_position=Ladder[ladder_start][1]
        if [Snake[i][0] for i in range(len(Snake))].count(p2_position):
            Snake_start=[Snake[i][0] for i in range(len(Snake))].index(p2_position)
            p2_position=Snake[Snake_start][1]
    else:
        dice_value=random.randint(1, 7)
        # if dice_value.isnumeric():
        #     dice_value=int(dice_value)
        #     dice_value=dice_value if 0<dice_value<7 else 0
        # else:
        #     print(f'Enter a valid dice value missed your current turn {p1}')
        #     continue
        
        if p1_position+dice_value>100:
            print(f'Current position of {p2} is {p2_position}')
            print(f'Current position of {p1} is {p1_position}')
            continue
        else:            
            p1_position+=dice_value
        if [Ladder[i][0] for i in range(len(Ladder))].count(p1_position):
            ladder_start=[Ladder[i][0] for i in range(len(Ladder))].index(p1_position)
            p1_position=Ladder[ladder_start][1]
        if [Snake[i][0] for i in range(len(Snake))].count(p1_position):
            Snake_start=[Snake[i][0] for i in range(len(Snake))].index(p1_position)
            p1_position=Snake[Snake_start][1]
    print(f'Current position of {p2} is {p2_position}')
    print(f'Current position of {p1} is {p1_position}')
    
if p1_position==100:
    print('*-*'*15)
    print('Good try '+p2)
    print(f'Congratulation {p1}')
    print('*-*'*15)
if p2_position==100:
    print('*-*'*15)
    print('Good try '+p1)
    print(f'Congratulation {p2}')
    print('*-*'*15)