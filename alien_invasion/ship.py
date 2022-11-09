import pygame
from pygame.sprite import Sprite


class Ship(Sprite):
    """管理飞船的类"""

    def __init__(self, ai_game):
        """初始化飞船并设置其初试位置"""
        super().__init__()
        # 1.屏幕
        self.screen = ai_game.screen  #
        self.screen_rect = ai_game.screen.get_rect()  # 方法访问屏幕的属性rect
        self.settings = ai_game.settings

        # 加载飞船图像并获取其外接矩形
        # 2.图像
        self.image = pygame.image.load('images/ship.bmp')  # 加载图像
        self.rect = self.image.get_rect()  # 使用方法获取surface的属性rect

        # 对于每艘新飞船，都将其放在屏幕底部的中央
        self.rect.midbottom = self.screen_rect.midbottom  # 屏幕和图像

        # 在飞船的属性x中存储小数值
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)  # 存储y

        # 移动标志
        self.moving_right = False
        self.moving_left = False  # 左移动
        self.moving_upper = False  # 向上移动
        self.moving_down = False  # 向下移动

    def update(self):
        """根据移动标志调整飞船的位置"""
        # 更新飞船
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:  # 右上角的坐标从零开始
            self.x -= self.settings.ship_speed
        if self.moving_upper and self.rect.top > 0:
            self.y -= self.settings.ship_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.height:
            self.y += self.settings.ship_speed

        # 根据self.x更新rect对象
        self.rect.x = self.x
        self.rect.y = self.y  # 更新y

    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """让飞船在屏幕底端居中"""
        self.rect.midbottom = self.screen_rect.midbottom
        # self.rect.y = self.screen_rect.bottom
        self.x = float(self.rect.x)
