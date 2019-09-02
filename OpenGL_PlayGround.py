import sys
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *




def init():
    glClearColor(1, 1, 1, 1)
    # glClearColor(0, 0, 0, 1)
    gluOrtho2D(0, 1000, 0, 1000)


def triangle():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1, 0, 0)
    glBegin(GL_TRIANGLES)

    glColor3f(1, 0, 0)
    glVertex2f(-1, -1)

    glColor3f(0, 1, 0)
    glVertex2f(1, -1)

    glColor3f(0, 0, 1)
    glVertex2f(0, 1)

    glEnd()
    glFlush()


class Points:
    points = []

    def draw_points(self):
        glColor3f(1, 0, 0)
        glPointSize(5)
        glBegin(GL_POINTS)
        for point in self.points:
            if point[2] == 0:
                glColor3f(1, 1, 1)
            elif point[2] == 1:
                glColor3f(0, 1, 0)
            elif point[2] == 2:
                glColor3f(0, 0, 1)
            elif point[2] == 3:
                glColor3f(0, 1, 1)
            glVertex2i(point[0] * 5, point[1] * 5)
        glEnd()
        glFlush()


points = Points()



def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(1000, 1000)
    glutInitWindowPosition(50, 50)
    glutCreateWindow("FuckCPP")
    glutDisplayFunc(points.draw_points)
    init()
    glutMainLoop()


def draw_pixel(x, y, color):
    points.points.append([x, y, color])


if __name__ == '__main__':
    main()
