import pygame

class Card:
    # статическая переменная, предотвращающая взятие нескольких карт за раз
    is_card_selected = False
    selection = []

    def __init__(self, color, rank, wild=None, wild_plus=None):
        # атрибуты инициализации
        self.special = False
        self.backup_surface = None
        self.backup_image = None

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
        self.surface = self.resize(self.surface, 1 / 2)

        # атрибуты методов
        self.dragging = False
        self.offset_x = self.rect.x
        self.offset_y = self.rect.y

    def display(self, screen):
        screen.blit(self.surface, self.rect)

    def move(self, x, y):
        # метод перемещения
        self.rect.x = x
        self.rect.y = y

    def pickup_card(self, border_width):
        # создаем бекапы
        backup_surface = self.surface
        backup_image = self.image

        # добавляем окаймление
        border_surface = pygame.Surface(
            (
            self.surface.get_width() + 2 * border_width,
            self.surface.get_height() + 2 * border_width
            )
        )
        border_surface.fill((255, 255, 255))
        border_surface.blit(self.surface, (border_width, border_width))

        # увеличиваем выбранную картинку
        border_surface = self.resize(border_surface, 1 / 1.6)  # не знаю почему, но это работает только так

        # возвращаем плоскость с окаймлением, а также бекапы
        return border_surface, backup_surface, backup_image

    def resize(self, surface, scale):
        # создаем плоскость, пропорционально размеру
        surface = pygame.transform.scale(
            self.image,
        (int(self.image.get_width() * scale),
            int(self.image.get_height() * scale))
        )

        # и обновляем ее хит бокс
        # ОПАСНО
        self.rect = surface.get_rect(topleft=(self.rect.x, self.rect.y))
        return surface

    def handle_event(self, event):
        # нажатие мыши
        if event.type == pygame.MOUSEBUTTONDOWN:
            # проверка нажатия на карту
            if self.rect.collidepoint(event.pos):
                # проверка отсутствия взятия двух карт одновременно
                if (not Card.is_card_selected) or Card.selection[0] == self.data:
                    # изменяем выбранные карты и задаем атрибут переноса
                    self.dragging = True
                    Card.selection = self.data
                    Card.is_card_selected = True

                    # задаем движение
                    self.offset_x = event.pos[0] - self.rect.x
                    self.offset_y = event.pos[1] - self.rect.y

                    # создаем окаймление карты
                    self.surface, self.backup_surface, self.backup_image = self.pickup_card(-5)

        # отпускание мышки
        elif event.type == pygame.MOUSEBUTTONUP:
            # убираем выделение карты
            if self.backup_surface:
                self.surface = self.backup_surface
                self.backup_surface = None

            if self.backup_image:
                self.image = self.backup_image
                self.surface = self.resize(self.surface, 1 / 2)
                self.backup_image = None

            # убираем выделенную карту и атрибут перемещения
            self.dragging = False
            Card.is_card_selected = False

        # перемещение мышки
        elif event.type == pygame.MOUSEMOTION:
            if self.dragging:
                self.rect.x = event.pos[0] - self.offset_x
                self.rect.y = event.pos[1] - self.offset_y