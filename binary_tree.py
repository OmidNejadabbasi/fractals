import stddraw


def draw_tree(n, x, y, size):
    if n <= 1:
        return

    stddraw.line(x, y, x - size/1.3, y - size)
    stddraw.filledCircle(x - size/1.3, y - size, 0.008)

    stddraw.line(x, y, x + size/1.3, y - size)
    stddraw.filledCircle(x + size/1.3, y - size, 0.008)

    draw_tree(n - 1, x - size/1.3, y - size, size / 2)
    draw_tree(n - 1, x + size/1.3, y - size, size / 2)


stddraw.setPenRadius(0.0025)
draw_tree(5, 0.5, 1, .3)
stddraw.show()
