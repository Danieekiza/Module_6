import arcade
from arcade.experimental.perspective_parallax import SCREEN_WIDTH, SCREEN_HEIGHT
from arcade.experimental.query_demo import SCREEN_TITLE

SCREEN_WIDTH = 800 # ширина
SCREEN_HEIGHT = 600 # высота
SCREEN_TITLE = 'Pong Game' # заголовок

class Game(arcade.Window): # класс наследуется от arcade.Window
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.bar = Bar()

    def on_draw(self):
        self.clear((255,255,255)) # заливка белым
        self.bar.draw

class Bar(arcade.Sprite.): # класс объекта ракетки
    def __init__(self):
        super().__init__('bar.png', 1.0) # путь к файлу и масштаб

if __name__ == '__main__':
    window = Game(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.run() # метод запуска


