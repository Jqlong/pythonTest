import sys
import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet  # 从文件中导入类
from alien import Alien
from game_stats import GameStats
from time import sleep
from button import Button
from scoreboard import Scoreboard


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
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))

        # self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invasion")

        # 创建一个用于存储游戏统计信息的实例
        self.stats = GameStats(self)

        # 创建统计信息的实例
        self.sb = Scoreboard(self)

        # 创建ship实例
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()  # 类似一个列表
        self.aliens = pygame.sprite.Group() # 创建一个外星人

        self._creat_fleet()

        # 创建play按钮
        self.play_button = Button(self, "Play")

    def run_game(self):
        """开始游戏的主循环"""

        # 监听键盘和鼠标事件
        while True:
            self._check_events()

            if self.stats.game_active:

                self.ship.update()
                self._update_bullets()
                self._update_aliens()
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
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

    def _check_play_button(self, mouse_pos):
        """玩家在单击play是开始新游戏"""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            # 重置游戏设定
            self.settings.initialize_dynamic_settings()
            # 重置游戏统计信息
            self.stats.reset_stats()
            self.stats.game_active = True
            self.sb.prep_score()  # 重置游戏得分
            self.sb.prep_level()  # 重置等级

            # 清空余下的外星人和子弹
            self.aliens.empty()
            self.bullets.empty()

            # 创建一群新的外星人并让飞船居中
            self._creat_fleet()
            self.ship.center_ship()
            pygame.mouse.set_visible(False)

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
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        # 检查是否有子弹击中外星人
        # 如果是，就删除相应的子弹和外星人
        # 第一个Ture删除子弹，第二个Ture删除外星人
        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        """响应子弹和外星人碰撞"""
        # 删除发生碰撞的子弹和外星人
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
        if collisions:
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_points
                self.sb.prep_score()  # 更新分数图像
                self.sb.check_high_score()  # 更新得分后调用check_high_score()方法

        if not self.aliens:
            self.bullets.empty()
            self._creat_fleet()
            self.settings.increase_speed()

            # 提高等级
            self.stats.level += 1
            self.sb.prep_level()

    def _update_screen(self):
        """更新屏幕上的图像，并切换到新屏幕"""
        self.screen.fill(self.settings.bg_color)  # 设置颜色
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)  # 要让外星人现身，需要draw方法

        # 显示得分
        self.sb.show_score()

        # 如果游戏处于非活动状态，就绘制按钮
        if not self.stats.game_active:
            self.play_button.draw_button()
        pygame.display.flip()

    def _fire_bullet(self):
        """创建一颗子弹，并将其加入bullets中"""
        # if len(self.bullets) < self.settings.bullet_allowed:
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)

    def _creat_fleet(self):
        """创建外星人群"""
        # 创建一个外星人
        # 创建实例
        alien = Alien(self)

        # 从外星人的rect属性中获取外星人的宽度，并将其存储到变量中
        # alien_width = alien.rect.width
        # 返回一个元组
        alien_width, alien_height = alien.rect.size
        # 左右有边距
        # 计算可容纳多少个外星人
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)

        # 计算可以容纳多少行
        ship_height = self.ship.rect.height  # 获取飞船的高度
        available_space_y = (self.settings.screen_height - (3 * alien_height))
        number_rows = available_space_y // (2 * alien_height)

        # 创建第一行外星人
        for row_number in range(number_rows):  # 从1到number_rows
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)

    def _create_alien(self, alien_number, row_number):
        """创建一个外星人并将其放在当前行"""
        alien = Alien(self)
        # alien_width = alien.rect.width
        alien_width, alien_height = alien.rect.size  # 获取外星人的尺寸
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)

    def _check_fleet_edges(self):
        """有外星人到达边缘时采取相应的措施"""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """将整群外星人下移，并改变它们的方向"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _update_aliens(self):
        """更新外星人群中所有外星人的位置"""
        """检查是否有外星人位于屏幕边缘"""
        """更新外星人的位置"""
        self._check_fleet_edges()
        self.aliens.update()

        # 检查外星人和飞船之间的碰撞
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

        # 检测是否有外星人到达了屏幕底端
        self._check_alien_bottom()

    def _ship_hit(self):
        """相应飞船被外星人撞到"""

        if self.stats.ships_left > 0:
            # 将ship_lest减1
            self.stats.ships_left -= 1

            # 清空余下的外星人和子弹
            self.aliens.empty()
            self.bullets.empty()

            # 创建新的外星人
            self._creat_fleet()
            self.ship.center_ship()

            # 暂停
            sleep(0.5)
        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)

    def _check_alien_bottom(self):
        """检查是否有外星人到达了屏幕底端"""
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                # 像飞船被撞到一样处理
                self._ship_hit()
                break


if __name__ == '__main__':
    # 创建实例并运行
    ai = AlienInvasion()
    ai.run_game()
