import sys
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

class Renderer:
    points = []
    POINT_SIZE = 5
    
    def init(self):
        glClearColor(0, 0, 0, 0)
        gluOrtho2D(0,1000, 0, 1000)

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
        self.draw_points()
        glutSwapBuffers()
        

    def main(self):
        glutInit(sys.argv)
        glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
        glutInitWindowSize(1000, 1000)
        glutInitWindowPosition(50, 50)
        glutCreateWindow("FUCkCPP")
        self.init()
        glutDisplayFunc(self.draw_scene)
        glutIdleFunc(self.draw_scene)
        glutMainLoop()

    def test_points(self):
        for i in range(1000):
            point = Point(i, i ,(1,0,1))
            self.set_points(point)


class Point:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
    x = 0
    y = 0
    color = (1,1,1)
        
if __name__ == "__main__":
    render = Renderer()
    render.main()
    render.test_points()
