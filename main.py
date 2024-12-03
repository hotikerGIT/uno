import pygame
from card import Card
from deck import Deck
from hand import Hand

# раздача
def generate_hand():
    deck = Deck()

    # создаем объект класса Hand
    hand = Hand([deck.get_random_card() for _ in range(7)])

    x, y = 0, 100
    # создание карт требует распределения по месту, поэтому
    # мы не делегируем метод, так как параметр разный
    for i, tmp_card in enumerate(hand.get_cards()):
        x = 50 * i
        tmp_card.move(x, y, i)
        tmp_card.display(screen)

    return deck, hand

pygame.init()
screen = pygame.display.set_mode((1000, 1000))
clock = pygame.time.Clock()

playing_deck, current_hand = generate_hand()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        current_hand.handle_event(event)

    screen.fill((0, 0, 0))
    current_hand.display(screen)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()