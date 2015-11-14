import time
from PIL import Image, ImageDraw

from genetic import Myimage, ImagePopulation

if __name__ == "__main__":
    current_generation = 0
    current_evolve = 0
    start_time = time.time()
    refer_image = Myimage.from_file(filename="sample.png")
    ImagePopulation.REFRENCE_IMAGE = refer_image

    initial_population = ImagePopulation()
    initial_population.random_population()
    initial_population.update_image()
    while 1:
        new_population = initial_population.copy()
        new_population.mutate()
        if new_population.dirty:
            # print "new_population.dirty:%s"%new_population.dirty
            current_generation += 1
            # fintness = 
            new_population.update_image()
            ## calculate the fitness
            print "new_population.fitness:%s"%new_population.fitness
            if new_population.fitness < initial_population.fitness:
                ## need
                current_evolve += 1
                print "current_evolve:%s"%current_evolve
                initial_population = new_population
                if current_evolve % 100 == 0:
                    new_population.save_image(name="%s.jpg"%current_evolve)



