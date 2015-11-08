from PIL import Image

'''
AIMA: page 129

'''

class Myimage(object):

    SIZE = (200, 200)

    def __init__(self):
        self.image = None
        self._image_data = None


    def from_file(self, filename="sample.png"):
        self.image = Image.open(filename)
        self._image_data = self.image.getdata()


    def produce(self, other):
        pass

    @property 
    def image_data(self):
        return self._image_data or self.image.getdata()

    @classmethod
    def pix_diff(cls, pix1, pix2):
        return sum([ x*x - y*y for x, y in zip(pix1, pix2)])

    def fitness(self, other):
        return sum([pix_diff(x, y) for x, y in zip(self.image_data, other.image_data)])

class ImagePopulation(object);
    
    SIZE = 50

    def __init__(self, population=None):
        self.population = population or set()


    def random_selection(self):
        pass

    def generate_next(self):
        pass

    def save(self, name="test"):
        pass

    def read(self, name="test"):
        pass



















