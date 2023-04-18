def calc_midpoint(point1, point2) -> tuple:
    x_cords = (point1[0], point2[0])
    y_cords = (point1[1], point2[1])

    midx = (x_cords[0] + x_cords[1]) / 2
    midy = (y_cords[0] + y_cords[1]) / 2 

    return(midx, midy)