from selfdefine import *
import pygame as pg
import json

pg.init()

settings = readjson('settings.json')
info = pg.display.Info()

Color_wall = tuple(settings["Color_wall"])
Color_floor = tuple(settings["Color_floor"])
Color_ceiling = tuple(settings["Color_ceiling"])
Fov = int(settings["Fov"])
run_speed = float(settings["run_speed"])
roll_speed = float(settings["roll_speed"])
width = info.current_w
height = info.current_h
I_ambient = float(settings["I_ambient"])
I_sourse = float(settings["I_sourse"])
map_maza_height = int(settings["map_maza_height"])
map_maza_width = int(settings["map_maza_width"])
