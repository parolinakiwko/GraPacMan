import numpy as np
import pygame as pg
class Jedzonko:
    def __init__(self, plansza):
        self.plansza = plansza
        self.jedzenie = plansza.pozycje_jedzenie
        self.obrazek = pg.transform.rotozoom(pg.image.load("banan.png"),1, 0.05).convert_alpha()
    def pokaz(self):
        for pojedyncze_jedzenie in self.jedzenie:
            self.plansza.pola[pojedyncze_jedzenie[0]][pojedyncze_jedzenie[1]] = 2
            self.plansza.ekran.blit(self.obrazek, (pojedyncze_jedzenie[0] * self.plansza.szerokosc, pojedyncze_jedzenie[1] * self.plansza.szerokosc))