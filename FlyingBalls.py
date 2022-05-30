import tkinter as tk
from random import randint

WIDTH = 600
HEIGHT = 400

class Ball:
    def __init__(self):
        self.R = randint(10, 30)
        self.x = WIDTH/2#randint(self.R, WIDTH - self.R)
        self.y = HEIGHT/2#randint(self.R, HEIGHT - self.R)
        self.dx, self.dy = randint(-10,10), randint(-10,10)
        c='#' + str("{0:X}".format(randint(16,255))) + \
                str("{0:X}".format(randint(16,255))) + \
                str("{0:X}".format(randint(16,255))) # цвет в формате '#12AB5F'
        #print(c)
        self.ball_id = canvas.create_oval(
            self.x - self.R,
            self.y - self.R,
            self.x + self.R,
            self.y + self.R,
            fill = c
            )

    def move(self):
        self.x += self.dx
        self.y += self.dy
        if self.x + self.R > WIDTH or self.x - self.R <= 0:
            self.dx = -self.dx
        if self.y + self.R > HEIGHT or self.y - self.R <= 0:
            self.dy = -self.dy

    def show(self):
        canvas.move(self.ball_id, self.dx, self.dy)


def canvas_click_handler(event):
    print('x =', event.x, 'y =', event.y)
    


def tick():
    for ball in balls:
        ball.move()
        ball.show()
    root.after(50, tick)


def main():
    global root, canvas, balls
    
    root = tk.Tk()
    xcenter = (root.winfo_screenwidth() - WIDTH) / 2
    ycenter = (root.winfo_screenheight() - HEIGHT) / 2
    root.geometry('%dx%d+%d+%d' % (WIDTH, HEIGHT, xcenter, ycenter))
        
    canvas = tk.Canvas(root)
    
    
    canvas.pack(fill=tk.BOTH, expand=1)
    
    canvas.bind('<Button-1>', canvas_click_handler)
    balls = [Ball() for i in range(10)]
    tick()
    root.mainloop()


if __name__ == "__main__":
    main()
