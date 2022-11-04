import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):  # 继承Sprite类
    """在飞船当前位置创建一个子弹对象"""

    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # 在(0,0)处创建一个表示子弹的矩形，再设置正确的位置
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        # 从飞船的顶部发射子弹
        self.rect.midtop = ai_game.ship.rect.midtop
        # self.rect.right = ai_game.ship.rect.left  # 从左边发射子弹

        # 利用小数表示子弹的位置
        self.y = float(self.rect.y)
        # self.x = float(self.rect.x)

    def update(self):
        """向上移动子弹"""
        # 更新表示会子弹位置的小数值
        self.y -= self.settings.bullet_speed
        # self.x += self.settings.bullet_speed  # 向右移动子弹
        # 更新表示子弹的rect的位置
        self.rect.y = self.y
        # self.rect.x = self.x

    def draw_bullet(self):
        """在屏幕上绘制子弹"""
        pygame.draw.rect(self.screen, self.color, self.rect)