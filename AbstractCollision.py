from abc import ABC
from Duszki import Zwykle_Duszki, Pijane_Duszki
class AbstactCollision(ABC):
    def kolizja(self, index):
        pass
class AbstractMakerObject(ABC):
    def produce(self, klucz):
        pass
    def add_key(self, key, value):
        pass


class Factory(AbstractMakerObject):
    def __init__(self):
        self.slownik = {1:Kolizja_z_duszkiem, 2:Kolizja_z_jedzeniem}
    def produce(self, klucz):
        return self.slownik[klucz]
    def add_key(self, key, value):
        self.slownik[key] = value

class Maker(AbstractMakerObject):
    def __init__(self, duszki, jedzenie):
        self.slownik = {1: duszki, 2: jedzenie}
    def produce(self, klucz):
        return self.slownik[klucz]
    def add_key(self, key, value):
        self.slownik[key] = value


class Kolizja:
    def __init__(self, plansza, fabryka, maker, tablica):
        self.plansza = plansza
        self.index = self.plansza.pozycja_player
        self.key_to_produce = self.plansza.pola[self.index[0]][self.index[1]]
        self.object_to_collide = maker.produce(self.key_to_produce)
        self.tabelka = tablica
        self.strategia_kolizji = fabryka.produce(self.key_to_produce)(self.plansza, self.object_to_collide, self.tabelka)
        """Kolizja tworzy strategię kolizji wg pola na którym doszło do kolizji"""
    def koliduj(self):
        self.strategia_kolizji.kolizja(self.index)

class Kolizja_z_jedzeniem(AbstactCollision):
    def __init__(self, plansza, jadlo, tablica_w):
        self.plansza = plansza
        self.nowe_jedzenie = jadlo
        self.tablica_wynikow = tablica_w
    def kolizja(self, index):
        for i in self.nowe_jedzenie.jedzenie:
            if i == index:
                self.nowe_jedzenie.jedzenie.remove(i)
                self.tablica_wynikow.wynik +=1
                self.plansza.duchy_strategy = self.plansza.all_strategies[1]



class Kolizja_z_duszkiem(AbstactCollision):
    def __init__(self, plansza, kolid_duszki, tablica_w):
        self.plansza = plansza
        self.tablica_wynikow = tablica_w
    def kolizja(self, index):

        for i in self.plansza.pozycje_duszki:
            if i == index:
                if isinstance(self.plansza.duchy_strategy,Zwykle_Duszki):
                    self.tablica_wynikow.zycia -=1
                else:
                    self.tablica_wynikow.zycia +=1
                    self.plansza.pozycje_duszki.remove(i)
                    self.plansza.duchy_strategy = self.plansza.all_strategies[0]