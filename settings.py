import pygame

#20 spaces in the rows
level_map = [
'                              ',
'                           XXX',
'         XXX                 X',
'   XXXXX     XXX             X',
'X           XXXXX           XX',
'XX         X     X       X    ',
'   X   X                XXX   ',
'P XX   XXX             XXXXX  ',
'XXXX  XXXXXXX   XXXX XXXXXXXX ',
'XXXX  XXXXXXX   XXXX XXXXXXXX ',
]

tile_size = 64

#Very IMPORTANT! Needs to be consistent as well!
screen_width = 1200
screen_height = len(level_map) * tile_size


