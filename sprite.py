from PIL import Image, ImageDraw
import pyglet
from genetic import ImagePopulation, Myimage

class ImagePopulationSprite(pyglet.sprite.Sprite, ImagePopulation):
    def __init__(self, image, x=220, y=140, population=None):
        pyglet.sprite.Sprite.__init__(self, image, x=x, y=y)
        ImagePopulation.__init__(self, population=population)

    def update_image(self):
        ImagePopulation.update_image(self)
        self.image = pyglet.image.ImageData(200, 200, 'RGB', 
                                            self.myimage.image.tobytes(), 
                                            pitch= -200 * 3)
        # sprite = pyglet.sprite.Sprite(image)
        # self.random_population()