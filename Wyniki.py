import numpy as np
from AbstractAgent import *
import pygame as pg
import time
from constants import *
from abc import ABC

class Wyniki(AbstractAgent):
    def __init__(self, plansza):
        self.wynik = 0
        self.zycia = liczba_zyc
        self.plansza = plansza
    def pokaz(self):
        my_font = pg.font.SysFont('Comic Sans MS', 30)
        text_surface = my_font.render('Punkty {} życia {}'.format(self.wynik, self.zycia), False, (0, 0, 0))
        self.plansza.ekran.blit(text_surface, (0, 0))
    def jaki_stan_gry(self):
        if self.zycia <= 0:

            return Przegrana(self.plansza, self.wynik, self.zycia)
        if self.wynik == liczba_jedzenia:
            return Wygrana(self.plansza, self.wynik, self.zycia)
        return False

class AbstractResult(ABC):
    def result(self):
        pass

class Wygrana(AbstractResult):
    def __init__(self, plansza, wyn, zyc):
        self.plansza = plansza
        self.wyniki = wyn
        self.zyc = zyc
    def result(self):
        self.plansza.ekran.fill("green")
        my_font = pg.font.SysFont('Comic Sans MS', 30)
        text_surface = my_font.render("Wygrywasz", False, (0, 0, 0))
        self.plansza.ekran.blit(text_surface, (0, 0))
        pg.display.flip()
        pg.display.update()
        time.sleep(time_for_sleep)

class Przegrana(AbstractResult):
    def __init__(self, plansza, wyn, zyc):
        self.plansza = plansza
        self.wyniki = wyn
        self.zyc = zyc

    def result(self):
        self.plansza.ekran.fill("red")
        my_font = pg.font.SysFont('Comic Sans MS', 30)
        text_surface = my_font.render(f'Przegrywasz, ale twoje punkty =  {self.wyniki} ', False, (0, 0, 0))
        self.plansza.ekran.blit(text_surface, (0, 0))
        pg.display.flip()
        pg.display.update()
        time.sleep(time_for_sleep)

