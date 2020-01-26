#
#
def color_cell(cell):
    colorcell = 'white'
    if cell[0]  == 'A' or cell[0] == 'C' or cell[0] == 'E' or cell[0] == 'G':
        if int(cell[1]) % 2 == 0:
            return colorcell
        else:
            colorcell = 'black'
            return colorcell
    elif cell[0] == 'B' or cell[0] == 'D' or cell[0] == 'F' or cell[0] == 'H':
        if int(cell[1]) % 2 != 0:
            return colorcell
        else:
            colorcell = 'black'
            return colorcell
    else:
        colorcell = 'black'
        return colorcell


Cell1 = input("Введите координаты первой клетки: ")
Cell1 = Cell1.capitalize()
Cell2 = input("Введите координаты второй клетки: ")
Cell2 = Cell2.capitalize()
if color_cell(Cell1) == color_cell(Cell2):
    print ("Клетки одного цвета")
else:
    print ('Эти клетки разных цветов')