# -*- coding: utf-8 -*-
"""
Created on Sun Aug 11 18:37:13 2019

@author: GRENTOR
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 11:43:36 2019
@author: GRENTOR
"""

pos = [10,10]
init_pos = [10,10]
init_direct = 'N'

def turn_left():
    if init_direct == 'N':
        return 'W'
    elif init_direct == 'W':
        return 'S'
    elif init_direct == 'S':
        return 'E'
    elif init_direct == 'E':
        return 'N'
        
def turn_right():
    if init_direct == 'N':
        return 'E'
    elif init_direct == 'W':
        return 'N'
    elif init_direct == 'S':
        return 'W'
    elif init_direct == 'E':
        return 'S'
        
def move_pos(pos):
    if init_direct == 'N':
        pos[1] = pos[1] + 1
        return pos
    elif init_direct == 'E':
        pos[0] = pos[0] + 1
        return pos
    elif init_direct == 'W':
        pos[0] = pos[0] - 1
        return pos
    elif init_direct == 'S':
        pos[1] = pos[1] - 1
        return pos
    
n = input().upper()
for elem in n:
    if elem == 'L':
        init_direct = turn_left()
    elif elem == 'R':
        init_direct = turn_right()
    elif elem == 'G':
        pos = move_pos(pos)
if len(set(n)) == 1:
    print('no')
else:
    if pos == init_pos:
        print('yes')
    else:
        print('no')