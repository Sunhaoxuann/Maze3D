import selfdefine
from selfdefine import *
from vars import *
import pygame as pg

# pg.init()

# maza_map = generate_maze(map_maza_width, map_maza_height)

# screen = pg.display.set_mode((width, height))

# while True:
#     fillbackground(screen,Color_floor, Color_ceiling, height, width, I_ambient, I_sourse)
    
#     pg.display.update()
# generate_maze(10, 10)

map = generate_maze(map_maza_width, map_maza_height)
print(map)
map = creatmap(map)
for i in map:
    print(i)