import pygame
from card import Card
from deck import Deck
from hand import Hand

# раздача
def generate_hand(hand_x, hand_y, deck):
    # создаем объект класса Hand
    hand = Hand([deck.get_random_card() for _ in range(7)])

    # создание карт требует распределения по месту, поэтому
    # мы не делегируем метод, так как параметр разный
    for i, tmp_card in enumerate(hand.get_cards()):
        tmp_x = 50 * i + hand_x
        tmp_card.move(tmp_x, hand_y, i)
        tmp_card.display(screen)

    return hand

pygame.init()
screen = pygame.display.set_mode((1000, 1000))
clock = pygame.time.Clock()

playing_deck = Deck()
current_hand = generate_hand(300, 800, playing_deck)
enemy_hand = generate_hand(300, 200, playing_deck)
enemy_hand.hide()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        current_hand.handle_event(event)

    screen.fill((0, 0, 0))
    current_hand.display(screen)
    enemy_hand.display(screen)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()