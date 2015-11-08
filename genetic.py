import random
from PIL import Image
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

class ImagePopulation(object):
    
    SIZE = 50

    def __init__(self, population=None):
        ## this contain population
        self.population = population or []


    def mutate(self):
        x = random.random()


    def random_population(self):
        self.population = []
        for i in range(self.SIZE):
            self.population.append(random_gen_poly())

    def save(self, name="test"):
        pass

    def read(self, name="test"):
        pass
















