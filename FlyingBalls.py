import tkinter as tk
from random import randint
from math import hypot

WIDTH = 600
HEIGHT = 400
COUNT_BALLS = 10

class Ball:
    def __init__(self):
        self.r = randint(20, 50)
        self.x = WIDTH/2
        self.y = HEIGHT/2
        self.dx, self.dy = randint(-5,5), randint(-5,5)
        c='#' + str("{0:X}".format(randint(16,255))) + \
                str("{0:X}".format(randint(16,255))) + \
                str("{0:X}".format(randint(16,255))) # цвет в формате '#12AB5F'
        #print(c)
        self.ball_id = canvas.create_oval(
            self.x - self.r,
            self.y - self.r,
            self.x + self.r,
            self.y + self.r,
            fill = c
            )

    def move(self):
        self.x += self.dx
        self.y += self.dy
        if self.x + self.r > WIDTH or self.x - self.r <= 0:
            self.dx = -self.dx
        if self.y + self.r > HEIGHT or self.y - self.r <= 0:
            self.dy = -self.dy

    def show(self):
        canvas.move(self.ball_id, self.dx, self.dy)

    def kill_ball(self,number):
        #print(number)
        #canvas.delete(balls[number].ball_id)
        canvas.delete(self.ball_id)
        balls.pop(number)
  

def canvas_click_handler(event):
    #print('x =', event.x, 'y =', event.y)
    x, y = event.x, event.y
    i=0
    for ball in balls:
        if hypot(ball.x - x, ball.y - y) < ball.r:
            ball.kill_ball(i)
        i += 1
    if len(balls) == 0:
        canvas.create_text(WIDTH/2, HEIGHT/2, text = "GAME OVER", font = "Ubuntu 36")
    

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
    balls = [Ball() for i in range(COUNT_BALLS)]
    tick()
    root.mainloop()


if __name__ == "__main__":
    main()
