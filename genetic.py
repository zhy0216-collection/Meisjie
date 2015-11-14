import copy
import random

from PIL import Image, ImageDraw


'''
AIMA: page 129

'''

## return True if one nth possiblity happened, else False
def is_randomized(n):
    return random.randint(0, n) == 0


class Myimage(object):

    SIZE = (200, 200)

    def __init__(self, image=None):
        self.image = image
        self._image_data = image and image.getdata() or None

    @classmethod
    def from_file(cls, filename="sample.png"):
        self = cls()
        self.image = Image.open(filename).convert('RGB')
        self._image_data = self.image.getdata()
        return self


    @property 
    def image_data(self):
        if self._image_data:
            return self._image_data
        self._image_data = self.image.getdata()
        return self._image_data 

    @classmethod
    def pix_diff(cls, pix1, pix2):
        return sum([ (x-y)**2 for x, y in zip(pix1, pix2)])

    def fitness(self, other):
        return sum([self.pix_diff(x, y) for x, y in zip(self.image_data, other.image_data)])

class PolygonImage(object):
    COLOR_CHANGE_RATE = 1500
    MAX_VERTEX = 10

    def __init__(self):
        self.points = None
        self.colors = None

    def randomize(self, max_vertex=0):
        max_vertex = max_vertex or PolygonImage.MAX_VERTEX
        self.points = [self.make_random_point() for i in range(3)]
        self.colors = self.random_color()
        return self

    def random_color(self):
        return tuple([random.randint(0, 255) for i in range(4)])

    @classmethod
    def make_random_point(cls):
        return (random.randint(0, Myimage.SIZE[0]), random.randint(0, Myimage.SIZE[1]))

    def mutate(self):
        dirty = False
        if is_randomized(1500):
            dirty = self.add_point()

        if is_randomized(1500):
            dirty = dirty or self.remove_point()

        for position in range(4):
            if is_randomized(1500):
                self._mutate_color(position=position)
                dirty = True

        for i, point in enumerate(self.points):
            if is_randomized(1500):
                self.make_random_point()
                self.points[i] = self.make_random_point()
                dirty = True

        return dirty

    def add_point(self):
        length = len(self.points)
        if length < PolygonImage.MAX_VERTEX:
            index = random.randint(0, length)
            self.points.insert(index, self.make_random_point())
            return True

    def remove_point(self):
        length = len(self.points)
        if length > 2:
            index = random.randint(0, length-1)
            self.points.pop(index)
            return True


    def _mutate_color(self, position=0):
        colors = list(self.colors)
        colors[position] = random.randint(0, 255)
        self.colors = tuple(colors)

class ImagePopulation(object):
    
    SIZE = 50
    MAX_SIZE = 255
    REFRENCE_IMAGE = None

    def __init__(self, population=None):
        ## this contain population
        self.population = population or []
        self.dirty = False
        self._fitness = None
        self.myimage = None


    def mutate(self):
        if is_randomized(700):
            self.add_polygon()

        if is_randomized(1500):
            self.remove_polygon()

        if is_randomized(700):
            self.move_polygon()

        for polyimage in self.population:
            self.dirty = self.dirty or polyimage.mutate()

    def add_polygon(self):
        length = len(self.population)
        if length < self.MAX_SIZE:
            index = random.randint(0, length)
            self.population.insert(index, PolygonImage().randomize())
            self.dirty = True

    def remove_polygon(self):
        length = len(self.population)
        if length > 0:
            index = random.randint(0, length-1)
            self.population.pop(index)
            self.dirty = True

    def move_polygon(self):
        ## the original implementation seems verbose,
        ## i think its just swap

        length = len(self.population)
        if length < 1:
            return
        index1 = random.randint(0, length-1)
        index2 = random.randint(0, length-1)
        temp = self.population[index1]
        self.population[index1] = self.population[index2]
        self.population[index2] = temp
        self.dirty = True

    def random_population(self):
        self.population = []
        for i in range(self.SIZE):
            self.population.append(PolygonImage().randomize())

    def copy(self):
        new_self = copy.copy(self)
        new_self.population = copy.deepcopy(self.population)
        new_self._fitness = None
        new_self.dirty = False
        return new_self

    @property 
    def fitness(self):
        if self._fitness:
            return self._fitness

        # calculate it and assign to _fitness and return it
        self._fitness = self.myimage.fitness(ImagePopulation.REFRENCE_IMAGE)
        return self._fitness














