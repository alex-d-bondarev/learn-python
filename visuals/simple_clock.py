import pyglet
from pyglet import clock
from pyglet import shapes

fps = 60
angle_increment = 6/fps
angle = 0

window = pyglet.window.Window(500, 500)
rectangle = shapes.Rectangle(250, 250, 5, 200, color=(255, 22, 20))


@window.event
def on_draw():
    rectangle.rotation = angle

    window.clear()
    rectangle.draw()


def update_angle(_):
    global angle
    angle += angle_increment
    if angle >= 360:
        angle -= 360
    print(f'Angle is now {angle}')


clock.schedule_interval(update_angle, 1/fps)
pyglet.app.run()
