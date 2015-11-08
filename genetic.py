from PIL import Image

'''
AIMA: page 129

'''

class Myimage(object):

    size = (200, 200)

    def __init__(self):
        self.image = None
        self.image_data = None


    def from_file(self, filename="sample.png"):
        self.image = Image.open(filename)
        self.image_data = self.image.getdata()


    def similarity(self, other):
        pass


class Genetic(object);
    pass












