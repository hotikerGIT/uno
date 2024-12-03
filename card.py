import pygame
from values import *


class Card:
    # статическая переменная, предотвращающая взятие нескольких карт за раз
    selection = None

    # статическая переменная определения наложения карт друг на друга
    top_z = 0

    def __init__(self, color, rank, wild=None, wild_plus=None):
        # атрибуты инициализации
        self.special = False
        self.z = 0

        # для диких карт все отдельно
        if wild:
            self.rank = -1
            self.color = -1

            self.special = 'wild'
            self.image = pygame.image.load(f'assets/wild/wild_card.png')

            if wild_plus:
                self.special = 'wild_plus'
                self.image = pygame.image.load(f'assets/wild/4_plus.png')

        if not self.special:
            self.rank = rank
            self.color = color
            self.image = pygame.image.load(f'assets/{color}/{rank}_{color}.png')

        self.data = [self.rank, self.color]

        self.surface = pygame.Surface((self.image.get_width(), self.image.get_height()))
        self.surface.blit(self.image, (0, 0))
        self.rect = self.surface.get_rect(topleft=(0, 0))

        # ресайз со старта потому что пнг-шки слишком большие
        self.surface = self.resize(self.image, 1 / 2)

    def display(self, screen):
        screen.blit(self.surface, self.rect)

    def match_selection(self):
        if self == Card.selection:
            return True

        return False

    def move(self, x, y, *z):
        # метод перемещения
        self.rect.x = x
        self.rect.y = y

        if z:
            self.z = z[0]

    def hide(self):
        self.image = pygame.image.load('assets/card back/card_back.png')

        self.surface = pygame.Surface((self.image.get_width(), self.image.get_height()))
        self.surface.blit(self.image, (0, 0))

        self.surface = self.resize(self.image, 1 / 2)

    def determine_top(self, reset=False):
        if reset:
            Card.top_z = 0

        elif self.z > Card.top_z:
            Card.top_z = self.z

    def resize(self, image_to_resize, scale):
        # создаем плоскость, пропорционально размеру
        surface_to_resize = pygame.transform.scale(
            image_to_resize,
        (int(image_to_resize.get_width() * scale),
            int(image_to_resize.get_height() * scale))
        )

        # и обновляем ее хит бокс
        # ОПАСНО
        self.rect = surface_to_resize.get_rect(topleft=(self.rect.x, self.rect.y))
        return surface_to_resize

    def __eq__(self, other):
        if other:
            if (
                self.rank == other.rank
                or
                self.color == other.color
                or
                self.rank == -1
            ):
                return True

        return False

    def duplicate(self, other):
        return self.color == other.color and self.rank == other.rank

    def handle_event(self, event, current_card):
        # нажатие мыши
        if event.type == pygame.MOUSEBUTTONDOWN:
            # проверка нажатия на карту
            if self.rect.collidepoint(event.pos):
                if current_card == Card.selection:
                    # играем карту
                    Card.selection.move(X_CENTER, Y_CENTER)
                    Card.selection.z = 0
                    Card.selection.surface = Card.selection.resize(Card.selection.image, 1 / 2)

                    # до свидания, карта!
                    current_card.move(-100, -100)

                    # обновляем значения карт
                    current_card = Card.selection
                    Card.selection = None

        # перемещение мышки
        elif event.type == pygame.MOUSEMOTION:
            # проверка наведения курсора на карту
            if self.rect.collidepoint(event.pos):
                # определяем наивысшую выбранную карту
                self.determine_top()

                # среди всех карт выбираем только ту чей параметр наивысший
                if self.z == Card.top_z:
                    # убираем изменение одной и той же карты
                    if Card.selection != self:
                        # если до этого была выбрана какая-то карта, возвращаем ее размер
                        if Card.selection:
                            Card.selection.surface = Card.selection.resize(Card.selection.image, 1 / 2)

                        Card.selection = self
                        self.surface = self.resize(self.image, 1 / 1.6)

            # если не нашлось соприкосновения с картой
            else:
                if Card.selection == self:
                    # обнуляем значения выбранных карт
                    Card.selection = None
                    Card.top_z = 0

                # возвращаем карты в прежнее состояние
                self.surface = self.resize(self.image, 1 / 2)
