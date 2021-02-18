import stddraw, color


def draw_squares(n, center_x, center_y, size):
    if n <= 1:
        return

    draw_squares(n - 1, center_x - size, center_y - size, size / 2.1)
    draw_squares(n - 1, center_x + size, center_y - size, size / 2.1)
    draw_squares(n - 1, center_x - size, center_y + size, size / 2.1)
    draw_squares(n - 1, center_x + size, center_y + size, size / 2.1)

    stddraw.square(center_x, center_y, size)
    stddraw.setPenColor(color.GRAY)
    stddraw.filledSquare(center_x, center_y, size - 0.002)
    # you may need to change the value of 0.002 because of your screen resolution

    stddraw.setPenColor(color.BLACK)


stddraw.setPenRadius(0.002)
draw_squares(5, 0.5, 0.5, 0.22)
stddraw.show()
