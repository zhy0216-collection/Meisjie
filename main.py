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

    cur_gen_label = pyglet.text.Label('current generation:%s'%current_generation,
                          font_name='Times New Roman',
                          font_size=16,
                          x=window.width//2, y=window.height-50,
                          anchor_x='center', anchor_y='center')

    cur_evo_label = pyglet.text.Label('current evolve:%s'%current_evolve,
                          font_name='Times New Roman',
                          font_size=16,
                          x=window.width//2, y=window.height-100,
                          anchor_x='center', anchor_y='center')

    @window.event
    def on_draw():
        window.clear()
        initial_population.draw()
        cur_gen_label.text = 'current generation:%s'%current_generation
        cur_gen_label.draw()
        cur_evo_label.text = 'current evolve:%s'%current_evolve
        cur_evo_label.draw()


    started = False

    def ga(dt):
        global started, initial_population, current_generation, current_evolve
        # if started:
        #     return
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

    def show_data(dt):
        pass


    # clock.schedule_interval(callback, .5)
    pyglet.clock.schedule_interval(lambda dt: initial_population.update_image(), 1/60.)
    # pyglet.clock.schedule_interval(show_data, 1)
    pyglet.clock.schedule(ga)
    pyglet.app.run()











