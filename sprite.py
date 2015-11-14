from PIL import Image, ImageDraw
import pyglet
from genetic import ImagePopulation, Myimage

class ImagePopulationSprite(pyglet.sprite.Sprite, ImagePopulation):
    def __init__(self, image, x=220, y=140, population=None):
        pyglet.sprite.Sprite.__init__(self, image, x=x, y=y)
        ImagePopulation.__init__(self, population=population)

    def update_image(self):
        temp_image = Image.new('RGB', (200, 200))
        drw = ImageDraw.Draw(temp_image, 'RGBA')
        for poly in self.population:
            drw.polygon(poly.points, poly.colors)

        self.myimage = Myimage(temp_image)
        self.image = pyglet.image.ImageData(200, 200, 'RGB', temp_image.tobytes(), pitch= -200 * 3)
        # sprite = pyglet.sprite.Sprite(image)
        # self.random_population()