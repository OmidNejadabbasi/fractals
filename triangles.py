import stddraw


def recursive_draw_triangle(n, x1, y1, x2, y2, x3, y3):
    if n <= 1:
        return

    draw_triangle(x1, y1, x2, y2, x3, y3)
    stddraw.show(50)
    newx_offset = (x1 - x2) / 2
    newy_offset = (y1 - y2) / 2
    #        *
    #      /   \
    #     /     \
    #    a-------b
    #   /   \ /   \
    #  /-----c-----\

    a = (x2 + newx_offset, y2 + newy_offset)
    b = (x3 - newx_offset, y3 + newy_offset)
    c = ((x2 + x3) / 2, y3)

    recursive_draw_triangle(n - 1, x1, y1, a[0], a[1], b[0], b[1])
    recursive_draw_triangle(n - 1, a[0], a[1], x2, y2, c[0], c[1])
    recursive_draw_triangle(n - 1, b[0], b[1], c[0], c[1], x3, y3)


def draw_triangle(x1, y1, x2, y2, x3, y3):
    stddraw.line(x1, y1, x2, y2)
    stddraw.line(x2, y2, x3, y3)
    stddraw.line(x3, y3, x1, y1)


stddraw.setPenRadius(0.002)
from math import sqrt

h = sqrt(3) / 2

recursive_draw_triangle(7, .5, h, 0, 0, 1, 0)
stddraw.show()
