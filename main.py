import pyglet

from genetic import Myimage, ImagePopulation
from drawing import draw_poly, window, on_draw, sprite



if __name__ == "__main__":
    current_generation = 0
    current_evolve = 0
    refer_image = Myimage.from_file()
    initial_population = ImagePopulation()
    initial_population.random_population()
    pyglet.clock.schedule_interval(sprite.update, 1/60.)
    sprite.population = initial_population
    # draw_poly(initial_population.population)
    pyglet.app.run()


