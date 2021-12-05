import tkinter as tk
import math
import time


def move_objects(objects, x, y):
    for o in objects:
        canv.move(o, x, y)
    pass


class ComposedObject:
    def __init__(self, canvas):
        self.canvas = canvas

    def move_composed_object(self, objects, nmove, xstart, ystart, xend, yend, delay_time, move_time):
        dt = move_time / nmove
        dx = (xend - xstart) / nmove
        dy = (yend - ystart) / nmove
        x = xstart
        y = ystart
        x_int_prev = xstart
        y_int_prev = ystart
        for i in range(nmove):
            x += dx
            y += dy
            x_int = int(x)
            y_int = int(y)
            self.canvas.after(delay_time + int(i * dt),
                              move_objects,
                              objects,
                              x_int - x_int_prev,
                              y_int - y_int_prev)
            x_int_prev = x_int
            y_int_prev = y_int


class Sun(ComposedObject):
    def __init__(self, canvas):
        super().__init__(canvas)
        nb = 10
        beam_length = 80
        circle_radius = 30
        xstart = 580
        ystart = 400
        xend = 450
        yend = 50
        nmove = 100
        move_time = 1000
        pi_n = math.pi / nb
        objects = []
        for i in range(nb):
            objects.append(self.canvas.create_line(xstart - beam_length * math.cos(i * pi_n),
                                                   ystart - beam_length * math.sin(i * pi_n),
                                                   xstart + beam_length * math.cos(i * pi_n),
                                                   ystart + beam_length * math.sin(i * pi_n),
                                                   fill='yellow', width='3'))
        objects.append(self.canvas.create_oval(xstart - circle_radius,
                                               ystart - circle_radius,
                                               xstart + circle_radius,
                                               ystart + circle_radius,
                                               fill='yellow'))

        self.move_composed_object(objects, nmove, xstart, ystart, xend, yend, 0, move_time)


class Cloud(ComposedObject):
    def __init__(self, canvas):
        super().__init__(canvas)
        xstart = -80
        ystart = 100
        xend = 200
        yend = 100
        nmove = 100
        move_time = 1000
        rects = (
            (-100, -30, 100, 30),
            (-120, -60, 0, 0),
            (-10, -70, 80, 0),
            (-10, 0, 90, 40)
        )
        objects = [
            self.canvas.create_oval(xstart + xleft, ystart + ytop, xstart + xright, ystart + ybottom,
                                    fill='white', width=0)
            for xleft, ytop, xright, ybottom in rects
        ]

        self.move_composed_object(objects, nmove, xstart, ystart, xend, yend, 0, move_time)


class Flowers(ComposedObject):
    def __init__(self, canvas):
        super().__init__(canvas)

        ystart = 550
        yend = 470
        nmove = 100
        move_time = 1000
        xstarts = [10,
                   430,
                   500,
                   220,
                   290,
                   80,
                   150,
                   360]
        delay_time = 200
        for i in range(len(xstarts)):
            objects = []
            image = self.canvas.create_image(xstarts[i], ystart, image=rose)
            objects.append(image)
            self.move_composed_object(objects, nmove, xstarts[i], ystart, xstarts[i], yend, i * delay_time, move_time)


top = tk.Tk()
top.title('Landscape')

canv = tk.Canvas(top, bg="blue", height=500, width=500)
canv.pack()

buttons = tk.Frame(top)
buttons.pack()

tk. \
    Button(buttons, text='Sun', command=lambda: Sun(canv)). \
    pack(side=tk.LEFT)

tk. \
    Button(buttons, text='Cloud', command=lambda: Cloud(canv)). \
    pack(side=tk.LEFT)

tk.Button(buttons, text='Flowers', command=lambda: Flowers(canv)). \
    pack(side=tk.LEFT)

tk. \
    Button(buttons, text='Clear', command=lambda: canv.delete('all')). \
    pack(side=tk.LEFT)

rose = tk.PhotoImage(file='../files/rose_2_40x53.png')

top.mainloop()
