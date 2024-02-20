import numpy as np
import pygame as pg
"""
wszystkie klasy modyfikujące planszę (na bazie AbstractAgent) robią to przez zawieranie obiektu board z tej klasy
"""
pg.init()
class Plansza:

    def __init__(self, szerokosc_planszy, liczba_jedzenia, liczba_duszkow, width, duchow_strategie):

        self.pola =[[0] * szerokosc_planszy for _ in range(szerokosc_planszy)]
        self.pozycja_player = [0,0]
        self.szerokosc = szerokosc_planszy
        self.ekran = pg.display.set_mode((width, width))
        self.pozycje_jedzenie = np.random.choice(range(self.szerokosc), (liczba_jedzenia,2), replace=False).tolist()
        self.pozycje_duszki = [[4,4] for i in range(liczba_duszkow)]
        self.all_strategies = duchow_strategie.tworz()
        self.strategy_index = 0
        self.duchy_strategy = self.all_strategies[self.strategy_index] #definicja domyślnej strategii - tutaj są to Zwykle_Duszki
        self.target_pozycje_duszkow = np.random.choice(range(self.szerokosc), (liczba_jedzenia,2), replace=False).tolist()

    def czykolizja(self):
        if self.pola[self.pozycja_player[0]][self.pozycja_player[1]] != 0:
            """
            plansza przechowuje informacje o tym kto jest na którym jej polu przez numerację wg legendy
            """

            return True
        else:
             return False
    # def change_strategy(self):
    #     self.strategy_index = (self.strategy_index +1)%len(self.all_strategies)
    #     self.duchy_strategy = self.all_strategies[self.strategy_index]
"""
legenda:
1 - duszki
2 - jedzenie
"""