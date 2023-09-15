from graphics import Canvas
import time

CANVAS_WIDTH = 300
CANVAS_HEIGHT = 300
CIRCLE_SIZE = 20
DELAY = 0.01

def main():
    # setup
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
   
   # heartbeat
    while True:
       # create circle
        start_x = canvas.get_mouse_x()
        start_y = canvas.get_mouse_y()
        if start_x < (CANVAS_WIDTH - CIRCLE_SIZE) and start_y < (CANVAS_HEIGHT - CIRCLE_SIZE) and start_x >= 0 and start_y >=0:
            canvas.create_oval(start_x, start_y, start_x+CIRCLE_SIZE, start_y+CIRCLE_SIZE, 'red')
        
        # pause
        time.sleep(DELAY)
        
if __name__ == "__main__":
    main()
