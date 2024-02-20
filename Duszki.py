import numpy as np
import pygame as pg
from AbstractAgent import *
from abc import ABC
pg.init()
class DuchyStrategiePrzechowalnia:
    def __init__(self):
        self.lista_strategii = [Zwykle_Duszki, Pijane_Duszki]
        self.stworzone_strategie = []
    def tworz(self):
        for strat in self.lista_strategii:
            i = strat()
            self.stworzone_strategie.append(i)
        return self.stworzone_strategie


class Duszki(AbstractAgent):
    def __init__(self,plansza):
        self.plansza = plansza
    def pokaz(self):
        self.plansza.duchy_strategy.wyswietl(self.plansza)
class AbstractDuchStrategy(ABC):
    def wyswietl(self, baza):
        pass
class Zwykle_Duszki(AbstractDuchStrategy):
    def __init__(self):
        self.obrazek = pg.transform.rotozoom(pg.image.load("maybeduch.png"),1, 0.04).convert_alpha()


    def wyswietl(self, baza_duchy):
        """modyfikuje atrybuty planszy, niestety odpowiada zarówno za ruch co i za wyświetlanie duszka"""
        i = 0
        for pojedynczy_duszek, target_duszek in zip(baza_duchy.pozycje_duszki, baza_duchy.target_pozycje_duszkow):
            speed = 0.4
            baza_duchy.pola[pojedynczy_duszek[0]][pojedynczy_duszek[1]] = 0
            if pojedynczy_duszek == target_duszek:
                target_duszek = np.random.choice(range(baza_duchy.szerokosc), (1, 2), replace=False).tolist()[0]

            dlax = np.random.randn()*1.5
            dlay = np.random.randn()*1.5
            dx = target_duszek[0] - pojedynczy_duszek[0]
            dy = target_duszek[1] - pojedynczy_duszek[1]
            next_x = pojedynczy_duszek[0] + speed * (dx + dlax)
            next_y = pojedynczy_duszek[1] + speed * (dy + dlay)

            pojedynczy_duszek = [int(next_x) % baza_duchy.szerokosc, int(next_y) % baza_duchy.szerokosc]
            baza_duchy.pozycje_duszki[i] = pojedynczy_duszek
            baza_duchy.pola[pojedynczy_duszek[0]][pojedynczy_duszek[1]] = 1
            baza_duchy.ekran.blit(self.obrazek, (pojedynczy_duszek[0] * baza_duchy.szerokosc, pojedynczy_duszek[1] * baza_duchy.szerokosc))
            i += 1
class Pijane_Duszki(AbstractDuchStrategy):
    """
    strategia poruszania się duszków po zjedzeniu owocu - obowiązuje do czasu zbicia duszka
    """
    def __init__(self):
        self.obrazek = pg.transform.rotozoom(pg.image.load("maybeduch.png"),180, 0.04).convert_alpha()

    def wyswietl(self, baza_duchy):
        i = 0
        for pojedynczy_duszek, target_duszek in zip(baza_duchy.pozycje_duszki, baza_duchy.target_pozycje_duszkow):
            speed = 0.3
            baza_duchy.pola[pojedynczy_duszek[0]][pojedynczy_duszek[1]] = 0
            if pojedynczy_duszek == target_duszek:
                target_duszek = np.random.choice(range(baza_duchy.szerokosc), (1, 2), replace=False).tolist()[0]

            dlax = np.random.randn()
            dlay = np.random.randn()
            dx = target_duszek[0] - pojedynczy_duszek[0]
            dy = target_duszek[1] - pojedynczy_duszek[1]
            next_x = pojedynczy_duszek[0] + speed * (dx + dlax)
            next_y = pojedynczy_duszek[1] + speed * (dy + dlay)

            pojedynczy_duszek = [int(next_x) % baza_duchy.szerokosc, int(next_y) % baza_duchy.szerokosc]
            baza_duchy.pozycje_duszki[i] = pojedynczy_duszek
            baza_duchy.pola[pojedynczy_duszek[0]][pojedynczy_duszek[1]] = 1
            baza_duchy.ekran.blit(self.obrazek, (pojedynczy_duszek[0] * baza_duchy.szerokosc, pojedynczy_duszek[1] * baza_duchy.szerokosc))
            i += 1
