import pygame as pg

from Window import Window
from Structures import *
from Menu import Menu
pg.init()

window: Window = Window(Pos(1000, 750), Pos(800, 600), "menu maker")
menu: Menu = Menu(Pos(1000,750))

bg = Color(150,150,220)

menu.set_color(bg)

while window.is_running:
    event_list = pg.event.get()
    menu.run(window.get_mask(),event_list)
    window.run(event_list)
