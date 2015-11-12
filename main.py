import time
from PIL import Image, ImageDraw
import pyglet

from genetic import Myimage, ImagePopulation

window = pyglet.window.Window() # 640x480

if __name__ == "__main__":
    current_generation = 0
    current_evolve = 0
    start_time = time.time()
    refer_image = Myimage.from_file(filename="sample.png")
    ImagePopulation.REFRENCE_IMAGE = refer_image

    image = Image.new('RGB', (200, 200))
    image = pyglet.image.ImageData(200, 200, 'RGB', image.tobytes(), pitch= -200 * 3)
    initial_population = ImagePopulation(image)
    initial_population.random_population()
    initial_population.update_image()

    @window.event
    def on_draw():
        window.clear()
        initial_population.draw()

    started = False

    def ga(dt):
        global started, initial_population, current_generation, current_evolve
        if started:
            return
        started = True
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

        # initial_population.random_population()
        
        started = False

    def show_time(dt):
        total_time = time.time() - start_time
        print "evolve speed:%s times/s"%int(current_generation/float(total_time))


    # clock.schedule_interval(callback, .5)
    pyglet.clock.schedule_interval(lambda dt: initial_population.update_image(), 1/60.)
    pyglet.clock.schedule_interval(show_time, 30)
    pyglet.clock.schedule(ga)
    pyglet.app.run()











