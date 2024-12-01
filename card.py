import pygame

class Card:
    # статическая переменная, предотвращающая взятие нескольких карт за раз
    is_card_selected = False
    selection = []

    def __init__(self, color, rank, wild=None, wild_plus=None):
        # атрибуты инициализации
        self.special = False

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

        self.surface = pygame.Surface((self.image.get_width(), self.image.get_height()))
        self.surface.blit(self.image, (0, 0))
        self.rect = self.surface.get_rect(topleft=(0, 0))

        # ресайз со старта потому что пнг-шки слишком большие
        self.resize(1 / 2)

        # атрибуты методов
        self.dragging = False
        self.offset_x = self.rect.x
        self.offset_y = self.rect.y

    def display(self, screen):
        # метод отображения чтобы одно и то же двадцать раз не писать
        if Card.selection == [self.rank, self.color]:
            self.image = self.add_border(self.surface, 25)

        screen.blit(self.surface, self.rect)

    def move(self, x, y):
        # метод перемещения
        self.rect.x = x
        self.rect.y = y

    def add_border(self, surface, border_width):
        border_surface = pygame.Surface(
            (surface.get_width() + 2 * border_width, surface.get_height() + 2 * border_width)
        )

        border_surface.fill((0, 100, 0))  # White border
        border_surface.blit(surface, (border_width, border_width))
        return border_surface

    def resize(self, scale):
        # создаем плоскость, пропорционально размеру
        self.surface = pygame.transform.scale(
            self.image,
        (int(self.image.get_width() * scale),
            int(self.image.get_height() * scale))
        )

        # и обновляем ее хит бокс
        self.rect = self.surface.get_rect(topleft=(self.rect.x, self.rect.y))

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                data = [self.rank, self.color]

                if (not Card.is_card_selected) or Card.selection[0] == data:
                    self.dragging = True
                    self.offset_x = event.pos[0] - self.rect.x
                    self.offset_y = event.pos[1] - self.rect.y
                    Card.selection = data
                    Card.is_card_selected = True

        elif event.type == pygame.MOUSEBUTTONUP:
            self.dragging = False
            Card.is_card_selected = False

        elif event.type == pygame.MOUSEMOTION:
            if self.dragging:
                self.rect.x = event.pos[0] - self.offset_x
                self.rect.y = event.pos[1] - self.offset_y