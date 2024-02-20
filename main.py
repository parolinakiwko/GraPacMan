
from constants import *
from Plansza import *
from Duszki import *
from Jedzonko import *
from Ser import *
from Wyniki import Wyniki

from AbstractCollision import *


run = True
clock = pg.time.Clock()


pg.font.init()
ghost_strategy = DuchyStrategiePrzechowalnia() #tworzymy obiekty strategii poruszania się duszków na sucho

board = Plansza(szer, liczba_jedzenia, liczba_duszkow, width, ghost_strategy)


player = Ser(board)
duchy = Duszki(board)
jadlo = Jedzonko(board)
tabela = Wyniki(board)
lista_obiektow = [player, duchy, jadlo,tabela]
fabryka = Factory()
pg.display.set_caption("Pac Man")
pg.event.set_blocked(pg.MOUSEMOTION)
komenda = pg.K_d
def poruszaj(komenda):
    """ta funkcja odpowiada za automatyczny ruch playera"""
    try:
        slownik_komend = {pg.K_w:[1,1,-1], pg.K_s:[1,1,1], pg.K_a:[0,0,-1], pg.K_d:[0,0,1]}
        board.pozycja_player[slownik_komend[komenda][0]] = (board.pozycja_player[slownik_komend[komenda][1]] + 1*slownik_komend[komenda][2])%szer
    except KeyError: pass
while run:
    maker = Maker(duchy, jadlo)
    board.ekran.fill("purple")
    clock.tick(fps)


    for obiekt in lista_obiektow:
        obiekt.pokaz()
    poruszaj(komenda)

    for event in pg.event.get():

        if event.type == pg.KEYDOWN:
            komenda = event.key
            if event.key == pg.K_ESCAPE:
                run = False
    if board.czykolizja():
        kolizja = Kolizja(board, fabryka, maker, tabela)
        kolizja.koliduj()
    elif tabela.jaki_stan_gry():
        Wynik = tabela.jaki_stan_gry()
        Wynik.result()
        run = False

    pg.display.flip()
    pg.display.update()

pg.quit()
