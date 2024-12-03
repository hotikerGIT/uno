import pygame
from card import Card
from deck import Deck
from hand import Hand
from values import *

# раздача
def generate_hand(hand_x, hand_y, deck):
    # создаем объект класса Hand
    hand = Hand([deck.get_random_card() for _ in range(7)])

    # создание карт требует распределения по месту, поэтому
    # мы не делегируем метод, так как параметр разный
    for i, tmp_card in enumerate(hand.get_cards()):
        tmp_x = OFFSET_CARDS * i + hand_x
        tmp_card.move(tmp_x, hand_y, i)
        tmp_card.display(screen)

    return hand

pygame.init()
screen = pygame.display.set_mode((HEIGHT, WIDTH))
clock = pygame.time.Clock()

# создаем главные объекты игры
playing_deck = Deck()
current_hand = generate_hand(HAND_X, PLAYER_HAND_Y, playing_deck)
enemy_hand = generate_hand(HAND_X, ENEMY_HAND_Y, playing_deck)
enemy_hand.hide()

# вытягиваем игровую карту
current_card = playing_deck.get_random_card()
current_card.move(X_CENTER, Y_CENTER)

# создаем карту, изображающую карту колоды
deck_card = Card('blue', 1)
deck_card.hide()
deck_card.move(X_DECK, Y_CENTER)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        current_hand.handle_event(event, current_card)

    screen.fill(black)

    current_hand.display(screen)
    enemy_hand.display(screen)
    current_card.display(screen)
    deck_card.display(screen)

    pygame.display.flip()
    clock.tick(TICKS)

pygame.quit()