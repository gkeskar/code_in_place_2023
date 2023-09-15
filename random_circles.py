from graphics import Canvas
import random

CANVAS_WIDTH = 300
CANVAS_HEIGHT = 300
CIRCLE_SIZE = 20


def main():
    print('Random Circles')
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    # counter for 20
    # while counter is under 20 repeat follwoing
    i = 0
    n_circles = random.randint(0, 20)
    while (i < n_circles):
        # draw circle with random
        # decrement counter
        draw_random_circles(canvas)
        i += 1
    # draw_random_circles(canvas)
    
def draw_random_circles(canvas):
    color = random_color()
    circle_size = random.randint(0, CANVAS_WIDTH)
    x1 = random.randint(0, CANVAS_WIDTH-circle_size)
    y1 = random.randint(0, CANVAS_HEIGHT-circle_size)
    x2 = x1 + circle_size
    y2 = y1 + circle_size
    # right axis values should be greater than left
    # x1 - x2 = y1 - y2
    #canvas.create_oval(100, 150, 130, 180, color)
    #canvas.create_oval(150, 200, 170, 220, color)
    canvas.create_oval(x1, y1, x2, y2, color)
    
def random_color():
    """
    This is a function to use to get a random color for each circle. We have
    defined this for you and there is no need to edit code in this function,
    but feel free to read it over if you are interested. 
    """
    colors = ['blue', 'purple', 'salmon', 'lightblue', 'cyan', 'forestgreen']
    return random.choice(colors)

if __name__ == '__main__':
    main()
