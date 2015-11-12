from PIL import Image, ImageDraw
import pyglet

from genetic import Myimage, ImagePopulation

window = pyglet.window.Window() # 640x480

if __name__ == "__main__":
    current_generation = 0
    current_evolve = 0
    refer_image = Myimage.from_file()

    image = Image.new('RGB', (200, 200))
    image = pyglet.image.ImageData(200, 200, 'RGB', image.tobytes(), pitch= -200 * 3)
    initial_population = ImagePopulation(image)
    initial_population.random_population()

    @window.event
    def on_draw():
        window.clear()
        initial_population.draw()

    def ga(dt):
        initial_population.random_population()

    # clock.schedule_interval(callback, .5)
    pyglet.clock.schedule_interval(lambda dt: initial_population.update_image(), 1/60.)
    pyglet.clock.schedule(ga)
    pyglet.app.run()











