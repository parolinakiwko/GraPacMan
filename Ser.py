import numpy as np
import pygame as pg
from AbstractAgent import *
"""
to jest player
"""
class Ser(AbstractAgent):
    def __init__(self, plansza):
        self.plansza = plansza
        self.pozycja = plansza.pozycja_player
        self.obrazek =pg.transform.rotozoom(pg.image.load("Cheese-PNG.png"),1, 0.05).convert_alpha()
    def pokaz(self):
        self.plansza.ekran.blit(self.obrazek, (self.pozycja[0] * self.plansza.szerokosc, self.pozycja[1] * self.plansza.szerokosc))
