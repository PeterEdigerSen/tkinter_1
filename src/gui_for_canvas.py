import math
import tkinter as tk
import random


class Clouds:
    def __init__(self, canvas, xstart, ystart, xend, yend, move_time):
        Cloud(canvas, xstart, ystart, xend, yend, move_time, True)


class ComposedObject:
    def __init__(self, canvas):
        self.canvas = canvas

    @staticmethod
    def move_objects(objects, x, y):
        for o in objects:
            canv.move(o, x, y)

    def move_composed_object(self, objects, nmove, xstart, ystart, xend, yend,
                             delay_time, move_time, kill=False):
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
                              self.move_objects,
                              objects,
                              x_int - x_int_prev,
                              y_int - y_int_prev)
            x_int_prev = x_int
            y_int_prev = y_int

        if kill:
            self.canvas.after(delay_time + move_time, self.kill, objects)

    def kill(self, objects):
        for o in objects:
            self.canvas.delete(o)


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
                                               fill='yellow', activewidth=5))

        self.move_composed_object(objects, nmove, xstart, ystart, xend, yend, 0, move_time)


class Cloud(ComposedObject):
    def __init__(self, canvas, xstart, ystart, xend, yend, move_time, kill):
        super().__init__(canvas)
        nmove = 500
        #        rects = (
        #            (-100, -30, 100, 30),
        #            (-120, -60, 0, 0),
        #            (-10, -70, 80, 0),
        #            (-10, 0, 90, 40)
        #        )
        rects = []
        for i in range(7):
            cx = random.randint(-80, 80)
            lx = random.randint(30, 70)
            cy = random.randint(-25, 25)
            ly = random.randint(20, 40)
            rects.append((cx - lx, cy - ly, cx + lx, cy + ly))

        objects = [
            self.canvas.create_oval(xstart + xleft, ystart + ytop, xstart + xright, ystart + ybottom,
                                    fill='white', activefill='grey', width=0)
            for xleft, ytop, xright, ybottom in rects
        ]

        self.move_composed_object(objects, nmove, xstart, ystart, xend, yend, 0, move_time, kill)
        if kill:
            self.canvas.after(int(move_time / 2), Cloud, self.canvas, xstart, ystart, xend, yend, move_time, kill)


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
            image = self.canvas.create_image(xstarts[i], ystart,
                                             image=small_rose, activeimage=big_rose)
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
    Button(buttons, text='Cloud', command=lambda: Cloud(canv, -80, 100, 200, 100, 1000, False)). \
    pack(side=tk.LEFT)

tk. \
    Button(buttons, text='Clouds', command=lambda: Clouds(canv, -120, 100, 700, 100, 8000)). \
    pack(side=tk.LEFT)

tk.Button(buttons, text='Flowers', command=lambda: Flowers(canv)). \
    pack(side=tk.LEFT)

tk. \
    Button(buttons, text='Clear', command=lambda: canv.delete('all')). \
    pack(side=tk.LEFT)

small_rose = tk.PhotoImage(file='../files/rose_2_40x53.png')
big_rose = tk.PhotoImage(file='../files/rose_2_100x133.png')

top.mainloop()
