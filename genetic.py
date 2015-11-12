import copy
import random

from PIL import Image, ImageDraw
import pyglet

'''
AIMA: page 129

'''

## return True if one nth possiblity happened, else False
def is_randomized(n):
    return random.randint(0, n) == 0



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
    COLOR_CHANGE_RATE = 1500


    def __init__(self):
        self.points = None
        self.colors = None

    def randomize(self, max_vertex=6):
        self.points = [(random.randint(0, Myimage.SIZE[0]), random.randint(0, Myimage.SIZE[1])) \
                     for i in range(random.randint(3, max_vertex))]
        self.colors = self.random_color()
        return self

    def random_color(self):
        return tuple([random.randint(0, 255) for i in range(4)])

    def mutate(self):
        pass

    def _mutate_point(self):
        pass

    def _mutate_color(self, position=0):
        colors = list(self.colors)
        colors[position] = random.randint(0, 255)
        self.colors = tuple(colors)

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
        length = len(self.population)
        if length < self.MAX_SIZE:
            index = random.randint(0, length+1)
            self.population.insert(index, PolygonImage().randomize())

    def remove_polygon(self):
        length = len(self.population)
        if length > 0:
            index = random.randint(0, length)
            self.population.pop(index)

    def move_polygon(self):
        ## the original implementation seems verbose,
        ## i think its just swap

        length = len(self.population)
        if length < 1:
            return
        index1 = random.randint(0, length)
        index2 = random.randint(0, length)
        temp = self.population[index1]
        self.population[index1] = self.population[index2]
        self.population[index2] = temp


    def update_image(self):
        temp_image = Image.new('RGB', (200, 200))
        drw = ImageDraw.Draw(temp_image, 'RGBA')
        for poly in self.population:
            drw.polygon(poly.points, poly.colors)

        self.image = pyglet.image.ImageData(200, 200, 'RGB', temp_image.tobytes(), pitch= -200 * 3)
        # sprite = pyglet.sprite.Sprite(image)
        # self.random_population()

    def random_population(self):
        self.population = []
        for i in range(self.SIZE):
            self.population.append(PolygonImage().randomize())

    def save(self, name="test"):
        pass

    def read(self, name="test"):
        pass

    def copy(self):
        return copy.deepcopy(self)














