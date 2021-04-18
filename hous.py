def main():
    x, y = 200, 300
    width, heigth = 200, 300

    drow_house(x, y, width, heigth)


def drow_house(x, y, width, heigth):
    """
    фуркция рисует домик ширины width и высоты height от опортной точки (х, у)
    которая находится в середине нижней точки фундамента.
    х: координата х середины домика 
    у: координата у низа фундамента
    width: полная ширина домика (фундамент или вылеты крыши включены)
    height: полная высота домика
    """
    print('рисую домик')
    foundation_heigth = 0.05 * heigth
    walls_width = 0.9 * width
    walls_heigth = 0.5 * heigth
    roof_heigth = heigth - foundation_heigth - walls_heigth

    draw_house_foundation(x, y, width, foundation_heigth)
    draw_house_walls(x, y - foundation_heigth, walls_width, walls_heigth)
    draw_house_roof(x, y - foundation_heigth - walls_heigth, width, roof_heigth)


def draw_house_foundation(x, y, width, heigth):
    """
    Рисование основание домика ширины width  и высоты height от опорной точки (x, y),
    которая находится в середине нижней точки фундамента.
    х: координата середины фундамента
    у: координата низа фундамента
    width: полная ширина фундамента
    height: полная высота фундамента
    """
    print('рисую основание')
    pass


def draw_house_walls(x, y , walls_width, heigth):
    print('рисую стены')
    pass


def draw_house_roof(x, y , width, heigth):
    print('рисую крышу')
    pass

main()
