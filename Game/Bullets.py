import pygame
from GLOBALS import SCREEN_WIDTH
from GLOBALS import bullet_group
from GLOBALS import enemy_group

#Загрузка изображение пули
bullet_img = pygame.image.load('img/icons/bullet.png').convert_alpha()

#Загрузка изображение гранаты
grenade_img = pygame.image.load('img/icons/grenade.png').convert_alpha()

class Bullet(pygame.sprite.Sprite):
    """Класс Bullet используется для создания пуль
        Каждая пуля будет являться отдельным независимым объектом

        Атрибуты
        ----------
        speed : int
            Скорость пули (константа)
        image : ---
            Изображение пули
        rect : кортеж
            хитбокс пули
        direction : int
            Направление вылета пули

        Методы
        ----------
        update()
            Перемещает пулю в пространстве
    """
    def __init__(self, x, y, direction):
        pygame.sprite.Sprite.__init__(self)
        self.__speed = 10
        self.image = bullet_img
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.direction = direction

    def update(self):
        from Soldier import player
        """Метод для перемещения пуль в пространстве

        Перемещает пулю с определенной скоростью по экрану.
        После выхода пули за границу экрана или столкновением с перонажами
        удаляет объект пули из группы свобождая память."""

        self.rect.x += (self.direction * self.speed)
        #Проверка пули на выход за пределы экрана
        if self.rect.right < 0 or self.rect.left > SCREEN_WIDTH:
            self.kill()
        #Проверка столкновения с игроком
        if pygame.sprite.spritecollide(player, bullet_group, False):
            if player.alive:
                #При попадании в игрока уменьшает его здоровье на 5
                player.health -= 5
                self.kill()
        #Проверка столкновения с врагом
        for enemy in enemy_group:
            if pygame.sprite.spritecollide(enemy, bullet_group, False):
                if enemy.alive:
                    # При попадании во врага уменьшает его здоровье на 25
                    enemy.health -= 25
                    self.kill()

