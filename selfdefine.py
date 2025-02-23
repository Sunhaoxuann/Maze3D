import json
import pygame as pg
import random

def generate_maze(width, height):
    # 创建一个二维数组，初始值为1（表示墙）
    maze = [[1 for _ in range(width)] for _ in range(height)]
    
    def carve_path(x, y):
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        random.shuffle(directions)
        
        for dx, dy in directions:
            nx, ny = x + dx * 2, y + dy * 2
            if 0 <= nx < width and 0 <= ny < height and maze[ny][nx] == 1:
                maze[ny][nx] = 0
                maze[y + dy][x + dx] = 0
                carve_path(nx, ny)
    
    # 从随机起点开始生成迷宫
    start_x = random.randint(0, (width - 1) // 2) * 2
    start_y = random.randint(0, (height - 1) // 2) * 2
    maze[start_y][start_x] = 0
    carve_path(start_x, start_y)
    
    return maze

def readjson(filename):
    with open(filename, 'r') as f:
        return json.load(f)
        
def fillbackground(screen, Color_floor, Color_ceiling, height, width, I_ambient, I_souse):
    lenth = height // 2
    R, G, B = Color_ceiling
    for i in range(lenth):
        light = I_ambient + I_souse * (lenth - i) / lenth
        line_color_ceiling = (int(R * light), int(G * light), int(B * light))
        pg.draw.line(screen, line_color_ceiling, (0, i), (width, i))
    R, G, B = Color_floor
    for i in range(height-lenth):
        light = 1 - (I_ambient + I_souse * (lenth - i) / lenth)
        line_color_floor = (int(R * light), int(G * light), int(B * light))
        pg.draw.line(screen, line_color_floor, (0, i + lenth), (width, i + lenth))
