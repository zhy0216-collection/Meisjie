from PIL import Image, ImageDraw
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
# image = pyglet.resource.image('sample.png')

temp_image = Image.open("sample.png").convert('RGB')
print temp_image.mode
drw = ImageDraw.Draw(temp_image, 'RGBA')
drw.polygon([(50, 0), (100, 100), (0, 100)], (255, 0, 0, 125))
drw.polygon([(50,100), (100, 0), (0, 0)], (0, 255, 0, 125))
#.transpose(Image.FLIP_TOP_BOTTOM)
raw_image = temp_image.tobytes()


image = pyglet.image.ImageData(200, 200, 'RGB', raw_image, pitch= -200 * 3)

##



@window.event
def on_draw():
    window.clear()
    label.draw()
    image.blit(0, 0)

if __name__  == "__main__":
    # im = Image.open("sample.png")
    # im.show()


    pyglet.app.run()

