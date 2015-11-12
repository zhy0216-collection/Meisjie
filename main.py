from PIL import Image, ImageDraw
import pyglet

from genetic import Myimage, ImagePopulation

window = pyglet.window.Window() # 640x480

if __name__ == "__main__":
    current_generation = 0
    current_evolve = 0
    refer_image = Myimage.from_file(filename="sample.png")
    ImagePopulation.REFRENCE_IMAGE = refer_image

    image = Image.new('RGB', (200, 200))
    image = pyglet.image.ImageData(200, 200, 'RGB', image.tobytes(), pitch= -200 * 3)
    initial_population = ImagePopulation(image)
    initial_population.random_population()

    @window.event
    def on_draw():
        window.clear()
        initial_population.draw()

    started = False

    def ga(dt):
        global started, initial_population, current_generation
        if started:
            return
        started = True
        new_population = initial_population.copy()
        new_population.mutate()
        if new_population.dirty:
            current_generation += 1
            # fintness = 
            ## calculate the fitness
            if new_population.fitness < initial_population.fintness:
                ## need
                initial_population = new_population

        initial_population.random_population()
        
        started = False


    # clock.schedule_interval(callback, .5)
    pyglet.clock.schedule_interval(lambda dt: initial_population.update_image(), 1/60.)
    pyglet.clock.schedule(ga)
    pyglet.app.run()











