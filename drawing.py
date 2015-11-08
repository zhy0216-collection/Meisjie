from PIL import Image
import pyglet

"""
Load pyglet image from PIL
https://gist.github.com/jamesadney/1971332
temp_image = Image.open("picture.png")
raw_image = temp_image.tostring()

image = pyglet.image.ImageData(width, height, 'RGB', raw_image, pitch= -resized_x * 3)

"""

window = pyglet.window.Window()
label = pyglet.text.Label('Hello, world',
                          font_name='Times New Roman',
                          font_size=36,
                          x=window.width//2, y=window.height//2,
                          anchor_x='center', anchor_y='center')
image = pyglet.resource.image('sample.png')

@window.event
def on_draw():
    window.clear()
    label.draw()
    image.blit(0, 0)


if __name__  == "__main__":
    # im = Image.open("sample.png")
    # im.show()
    pyglet.app.run()

