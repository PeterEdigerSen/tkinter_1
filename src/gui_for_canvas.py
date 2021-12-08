import math
import random
import tkinter as tk


class ComposedObject:
    def __init__(self, canvas):
        self.canvas = canvas
        self.objects = []

    def move_objects(self, x, y):
        for o in self.objects:
            canv.move(o, x, y)

    def move_composed_object(self, x_start, y_start, x_end, y_end, move_time, n_move):
        dt = move_time / n_move
        dx = (x_end - x_start) / n_move
        dy = (y_end - y_start) / n_move
        x = x_start
        y = y_start
        x_int_prev = x_start
        y_int_prev = y_start
        for i in range(n_move):
            x += dx
            y += dy
            x_int = int(x)
            y_int = int(y)
            self.canvas.after(int(i * dt),
                              self.move_objects,
                              x_int - x_int_prev,
                              y_int - y_int_prev)
            x_int_prev = x_int
            y_int_prev = y_int

    def kill(self):
        for o in self.objects:
            self.canvas.delete(o)


class Sun(ComposedObject):
    def __init__(self, canvas, x_start, y_start, x_end, y_end, move_time):
        super().__init__(canvas)
        nb = 10
        beam_length = 80
        circle_radius = 30
        n_move = 100
        pi_n = math.pi / nb
        for i in range(nb):
            self.objects.append(self.canvas.create_line(x_start - beam_length * math.cos(i * pi_n),
                                                        y_start - beam_length * math.sin(i * pi_n),
                                                        x_start + beam_length * math.cos(i * pi_n),
                                                        y_start + beam_length * math.sin(i * pi_n),
                                                        fill='yellow', width='3'))
        self.objects.append(self.canvas.create_oval(x_start - circle_radius,
                                                    y_start - circle_radius,
                                                    x_start + circle_radius,
                                                    y_start + circle_radius,
                                                    fill='yellow', activewidth=5))

        self.move_composed_object(x_start, y_start, x_end, y_end, move_time, n_move)


class Cloud(ComposedObject):
    def __init__(self, canvas, x_start, y_start, x_end, y_end, move_time):
        super().__init__(canvas)
        n_move = 500
        rects = []
        for i in range(7):
            cx = random.randint(-80, 80)
            lx = random.randint(30, 70)
            cy = random.randint(-25, 25)
            ly = random.randint(20, 40)
            rects.append((cx - lx, cy - ly, cx + lx, cy + ly))

        self.objects = [
            self.canvas.create_oval(x_start + x_left, y_start + y_top, x_start + x_right, y_start + y_bottom,
                                    fill='white', activefill='grey', width=0)
            for x_left, y_top, x_right, y_bottom in rects
        ]

        self.move_composed_object(x_start, y_start, x_end, y_end, move_time, n_move)


class Flower(ComposedObject):
    def __init__(self, canvas, x_start, y_start, x_end, y_end, move_time):
        super().__init__(canvas)

        n_move = 100
        image = self.canvas.create_image(x_start, y_start,
                                         image=small_rose, activeimage=big_rose)
        self.objects.append(image)
        self.move_composed_object(x_start, y_start, x_end, y_end, move_time, n_move)


class Clouds:
    def __init__(self, canvas, x_start, y_start, x_end, y_end, move_time, delay_time):
        self.canvas, self.x_start, self.y_start, self.x_end, self.y_end, self.move_time, self.delay_time = \
            canvas, x_start, y_start, x_end, y_end, move_time, delay_time
        self.active = False

    def start_stop(self):
        self.active = not self.active
        if self.active:
            clouds_button.config(fg='green')
            self.generate_clouds()
        else:
            clouds_button.config(fg='red')

    def generate_clouds(self):
        if self.active:
            cloud = Cloud(self.canvas, self.x_start, self.y_start, self.x_end, self.y_end, self.move_time)
            self.canvas.after(self.move_time, cloud.kill)
            self.canvas.after(self.delay_time, self.generate_clouds)


class Flowers:
    def __init__(self, canvas):
        y_start = 550
        y_end = 470
        move_time = 1000
        x_starts = [10,
                    430,
                    500,
                    220,
                    290,
                    80,
                    150,
                    360]
        delay_time = 200
        for i in range(len(x_starts)):
            canvas.after(i * delay_time, Flower, canvas, x_starts[i], y_start, x_starts[i], y_end, move_time)


top = tk.Tk()
top.title('Landscape')

canv = tk.Canvas(top, bg="blue", height=500, width=500)
canv.pack()

buttons = tk.Frame(top)
buttons.pack()

tk. \
    Button(buttons, text='Sun', command=lambda: Sun(canv, 580, 400, 450, 50, 1000)). \
    pack(side=tk.LEFT)

tk. \
    Button(buttons, text='Cloud', command=lambda: Cloud(canv, -80, 100, 200, 100, 1000)). \
    pack(side=tk.LEFT)

clouds = Clouds(canv, -120, 100, 700, 100, 5000, 2000)
clouds_button = tk. \
    Button(buttons, text='Clouds', fg='red', command=clouds.start_stop)
clouds_button.pack(side=tk.LEFT)

tk. \
    Button(buttons, text='Flowers', command=lambda: Flowers(canv)). \
    pack(side=tk.LEFT)

tk. \
    Button(buttons, text='Clear', command=lambda: canv.delete('all')). \
    pack(side=tk.LEFT)

small_rose = tk.PhotoImage(file='../files/rose_2_40x53.png')
big_rose = tk.PhotoImage(file='../files/rose_2_100x133.png')

top.mainloop()

