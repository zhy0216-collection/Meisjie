from PIL import Image, ImageDraw
import pyglet

"""
Load pyglet image from PIL
https://gist.github.com/jamesadney/1971332
temp_image = Image.open("picture.png")
raw_image = temp_image.tostring()

image = pyglet.image.ImageData(width, height, 'RGB', raw_image, pitch= -resized_x * 3)

"""

window = pyglet.window.Window() # 640x480
label = pyglet.text.Label('Hello, world',
                          font_name='Times New Roman',
                          font_size=16,
                          x=window.width//2, y=window.height-50,
                          anchor_x='center', anchor_y='center')
# image = pyglet.resource.image('sample.png')

# temp_image = Image.open("sample.png").convert('RGB')
# print temp_image.mode
# drw = ImageDraw.Draw(temp_image, 'RGBA')
# drw.polygon([(50, 0), (100, 100), (0, 100)], (255, 0, 0, 125))
# drw.polygon([(50,100), (100, 0), (0, 0)], (0, 255, 0, 125))
# #.transpose(Image.FLIP_TOP_BOTTOM)
# raw_image = temp_image.tobytes()
image = Image.new('RGB', (200, 200))
image = pyglet.image.ImageData(200, 200, 'RGB', image.tobytes(), pitch= -200 * 3)
sprite = pyglet.sprite.Sprite(image)
# def draw_image(raw_image):
#     global image
#     image = pyglet.image.ImageData(200, 200, 'RGB', raw_image, pitch= -200 * 3)


def draw_poly(dt):
    global sprite
    temp_image = Image.new('RGB', (200, 200))
    drw = ImageDraw.Draw(temp_image, 'RGBA')
    for poly in sprite.population.population:
        drw.polygon(*poly)

    image = pyglet.image.ImageData(200, 200, 'RGB', temp_image.tobytes(), pitch= -200 * 3)
    p = sprite.population
    sprite = pyglet.sprite.Sprite(image)
    sprite.population = p
    sprite.population.random_population()
##
sprite.update = draw_poly


@window.event
def on_draw():
    window.clear()
    label.draw()
    sprite.draw()
    # image.blit(220, 140)

if __name__  == "__main__":
    # im = Image.open("sample.png")
    # im.show()


    pyglet.app.run()

