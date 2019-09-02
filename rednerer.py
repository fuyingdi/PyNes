import sys
import threading
import time
import random
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

class Renderer:
    points = []
    canvas_width = 0
    canvas_height = 0
    POINT_SIZE = 5

    def __init__(self, canvas_width=1000, canvas_height=1000):
        self.canvas_height = canvas_height
        self.canvas_width = canvas_width
    
    def init(self):
        glClearColor(0, 0, 0, 0)
        gluOrtho2D(0,self.canvas_width, 0, self.canvas_height)

    def test(self):
        glClear(GL_COLOR_BUFFER_BIT)
        glColor3f(1, 0, 0)
        glBegin(GL_TRIANGLES)

        glColor3f(1, 0, 0)
        glVertex2f(0, 0)

        glColor3f(0, 1, 0)
        glVertex2f(500, 1000)

        glColor3f(0, 0, 1)
        glVertex2f(1000, 0)

        glEnd()
        glFlush()

    def set_points(self, point):
        print("Set Point")
        assert isinstance(point, Point)
        self.points.append(point)

        
    def draw_points(self):
        glClear(GL_COLOR_BUFFER_BIT)
        glPointSize(self.POINT_SIZE)
        glBegin(GL_POINTS)
        for point in self.points:
            assert isinstance(point , Point)
            glColor3f(point.color[0], point.color[1], point.color[2])
            glVertex2i(point.x * self.POINT_SIZE, point.y * self.POINT_SIZE)

        glEnd()
        glFlush()

            

    def draw_scene(self):
        print("Draw")
        self.draw_points()
        

    def main(self):
        glutInit(sys.argv)
        glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
        glutInitWindowSize(self.canvas_width, self.canvas_height)
        glutInitWindowPosition(50, 50)
        glutCreateWindow("FUCkCPP")
        self.init()
        glutDisplayFunc(self.draw_scene)
        glutIdleFunc(self.draw_scene)
        glutMainLoop()

    def test_points(self):
        print("Test Point")
        for i in range(self.canvas_height):
            point = Point(i, i ,(1,0,1))
            self.set_points(point)
            time.sleep(0.01)

    def test_random_points(self):
        while True:
            print("new point")
            x = random.randint(0, self.canvas_width)
            y = random.randint(0, self.canvas_height)
            color = (random.uniform(0, 1), random.uniform(
            0, 1), random.uniform(0, 1))
            # color = (1,1,0)
            point = Point(x, y, color)
            self.set_points(point)
            time.sleep(0.001)
        

    def run(self):
        mainloop_thread = threading.Thread(target=self.main, args=())
        mainloop_thread.start()

        


class Point:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
    x = 0
    y = 0
    color = (1,1,1)


        
if __name__ == "__main__":
    render = Renderer(500, 500)
    render.run()
    render.test_random_points()