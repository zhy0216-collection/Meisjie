import random
from PIL import Image, ImageDraw
import pyglet

'''
AIMA: page 129

'''

def random_gen_poly(max_vertex=6):
        return [[(random.randint(0, Myimage.SIZE[0]), random.randint(0, Myimage.SIZE[1])) \
                     for i in range(random.randint(3, max_vertex))], random_color()]


def random_color():
    return tuple([random.randint(0, 255) for i in range(4)])

class Myimage(object):

    SIZE = (200, 200)

    def __init__(self):
        self.image = None
        self._image_data = None

    @classmethod
    def from_file(cls, filename="sample.png"):
        self = cls()
        self.image = Image.open(filename).convert('RGB')
        self._image_data = self.image.getdata()
        return self


    @property 
    def image_data(self):
        return self._image_data or self.image.getdata()

    @classmethod
    def pix_diff(cls, pix1, pix2):
        return sum([ x*x - y*y for x, y in zip(pix1, pix2)])

    def fitness(self, other):
        return sum([pix_diff(x, y) for x, y in zip(self.image_data, other.image_data)])

class PolygonImage(object):

    
    def __init__(self):
        self.points = None
        self.colors = None

    def randomlize(self, max_vertex=6):
        self.points = [(random.randint(0, Myimage.SIZE[0]), random.randint(0, Myimage.SIZE[1])) \
                     for i in range(random.randint(3, max_vertex))]
        self.colors = random_color()

    def mutate(self):
        pass

    def _mutate_point(self):
        pass

    def _mutate_color(self):
        pass

class ImagePopulation(pyglet.sprite.Sprite):
    
    SIZE = 50
    MAX_SIZE = 255

    def __init__(self, image, x=0, y=0, population=None):
        super(self.__class__, self).__init__(image, x=x, y=y)

        ## this contain population
        self.population = population or []


    def mutate(self):
        x = random.random()

    def add_polygon(self):
        if len(self.population) <= 255:
            pass

    def remove_polygon(self):
        pass

    def move_polygon(self):
        pass

    def update_image(self):
        temp_image = Image.new('RGB', (200, 200))
        drw = ImageDraw.Draw(temp_image, 'RGBA')
        for poly in self.population:
            drw.polygon(*poly)

        self.image = pyglet.image.ImageData(200, 200, 'RGB', temp_image.tobytes(), pitch= -200 * 3)
        # sprite = pyglet.sprite.Sprite(image)
        # self.random_population()


    def random_population(self):
        self.population = []
        for i in range(self.SIZE):
            self.population.append(random_gen_poly())

    def save(self, name="test"):
        pass

    def read(self, name="test"):
        pass

















