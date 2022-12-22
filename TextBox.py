import pygame as pg

from TextHolder import TextHolder
from Structures import *
from Constants import Colors
from Sprite import Sprite
from MSprite import MSprite

class TextBox:
    def __init__(self,rect:Rect,textHolder:TextHolder):

        self.__text_holder = textHolder
        self.__rect = rect
        self.__surface = pg.surface.Surface(self.__rect.get_size().get_tuple()).convert_alpha()

        self.__background_color = Color(50,50,50)
        self.__background_hover_color = Color(150,150,255)

        self.__current_background_color = self.__background_color.get_joined(
            self.__background_hover_color , 0.5)

        self.__hover_transition_speed_scale = 0.01

        self.border_color = 0

        self.__background_image = None
        self.__background_clip = None

        self.__image_on_top = False

        self.update_surface()

    def get_rect( self ):
        return self.__rect

    def reset_color( self ,color:Color=None,hover_color:Color=None):
        if color is None: color = Color(0,0,0)
        if hover_color is None: hover_color = Color(0,0,0)

        self.__background_color = color
        self.__background_hover_color = hover_color

        return self

    def reset_hover_transition( self , speed_scale:float = 0.1 ):
        self.__hover_transition_speed_scale = speed_scale

    def set_background_image( self , sprite:Sprite):
        self.__background_clip = None
        self.__background_image = sprite


    def set_background_clip( self , msprite:MSprite ):
        self.__background_image = None
        self.__background_clip = msprite



    def update_surface( self ):
        pass

    def check_events( self ):
        pass

    def render( self , surface:pg.surface.Surface , render_pos:Pos=None):
        if render_pos is None: render_pos = self.__rect.get_pos()

        print(self.__current_background_color)
        self.__surface.fill(self.__current_background_color.get_tuple())

        surface.blit(self.__surface,render_pos.get_tuple())

        self.__text_holder.render(surface,render_pos.copy())


