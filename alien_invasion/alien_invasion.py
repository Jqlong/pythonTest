import sys
import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet  # 从文件中导入类
from alien import Alien


class AlienInvasion:
    """管理游戏资源和行为的类"""

    def __init__(self):
        """初始化游戏并创建游戏资源"""
        pygame.init()

        # 创建设置类实例
        self.settings = Settings()
        # 传入长宽参数  注意括号
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        # self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))

        # self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invasion")

        # 创建ship实例
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()  # 类似一个列表
        self.aliens = pygame.sprite.Group() # 创建一个外星人

        self._creat_fleet()

    def run_game(self):
        """开始游戏的主循环"""

        # 监听键盘和鼠标事件
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_screen()

            # print(len(self.bullets))

            # 每次循环时都重绘屏幕 填充屏幕
            # self.screen.fill(self.settings.bg_color)
            # self.ship.blitme()
            # # 让最近绘制的屏幕可见
            # pygame.display.flip()

    # 辅助run_game的方法，用‘_’表示
    def _check_events(self):
        """响应按键和鼠标事件"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:  # 如果事件是keydown事件，检测是否是向右
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:  # 抬起按键
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """响应按键,向下按"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True  # 设置标志
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_UP:  # 向上
            self.ship.moving_upper = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True  # 向下
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:  # 按空格时调用方法
            self._fire_bullet()

    def _check_keyup_events(self, event):
        """响应松开"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        elif event.key == pygame.K_UP:
            self.ship.moving_upper = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False

    def _update_bullets(self):
        """更新子弹的位置并删除消失的子弹"""
        # 更新子弹的位置
        self.bullets.update()

        # 删除消失的子弹
        for bullet in self.bullets.copy():
            if bullet.rect.x >= self.ship.screen_rect.right:
                self.bullets.remove(bullet)

    def _update_screen(self):
        """更新屏幕上的图像，并切换到新屏幕"""
        self.screen.fill(self.settings.bg_color)  # 设置颜色
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)
        pygame.display.flip()

    def _fire_bullet(self):
        """创建一颗子弹，并将其加入bullets中"""
        if len(self.bullets) < self.settings.bullet_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _creat_fleet(self):
        """创建外星人群"""
        # 创建一个外星人
        alien = Alien(self)
        alien_width = alien.rect.width
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)

        self.aliens.add(alien)  # 要让外星人现身，draw()方法


if __name__ == '__main__':
    # 创建实例并运行
    ai = AlienInvasion()
    ai.run_game()
