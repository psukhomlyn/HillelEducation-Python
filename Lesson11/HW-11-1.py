"""
1.Реализовать класс фигуры. На основе фигуры реализовать класс треугольника, квадрата и прямоугольника с
методами подсчета площади и периметра. Методы должны возвращать (return) значение, а не принтить (это важно)
"""


class Figure:

    def perimeter(self):
        raise NotImplementedError

    def square(self):
        raise NotImplementedError


class Triangle(Figure):
    def __init__(self, side_a, side_b, side_c):
        assert isinstance(side_a, int), 'Triangle side should be integer'
        assert isinstance(side_b, int), 'Triangle side should be integer'
        assert isinstance(side_c, int), 'Triangle side should be integer'
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c
        self.validate_triangle()

    def validate_triangle(self):
        sides = [self.side_a, self.side_b, self.side_c]
        sorted_sides = sorted(sides)
        if sorted_sides[0] + sorted_sides[1] < sorted_sides[-1]:
            raise ValueError
        else:
            print('Triangle is valid')

    def perimeter(self):
        return self.side_a + self.side_b + self.side_c

    def square(self):
        semi_per = self.perimeter() / 2
        return (semi_per * (semi_per - self.side_a) * (semi_per - self.side_b) * (semi_per - self.side_c)) ** (1/2)


class Rectangle(Figure):
    def __init__(self, side_a, side_b):
        assert isinstance(side_a, int), 'Rectangle side should be integer'
        assert isinstance(side_b, int), 'Rectangle side should be integer'
        self.side_a = side_a
        self.side_b = side_b

    def perimeter(self):
        return (self.side_a + self.side_b) * 2

    def square(self):
        return self.side_a * self.side_b


class Square(Figure):
    def __init__(self, side_a):
        assert isinstance(side_a, int), 'Square side should be integer'
        self.side_a = side_a

    def perimeter(self):
        return self.side_a * 4

    def square(self):
        return self.side_a ** 2


def triangle_calc(side_a, side_b, side_c):
    tri = Triangle(side_a, side_b, side_c)
    tri.validate_triangle()
    tri.perimeter()
    print(f'Triangle perimeter is {tri.perimeter()}')
    tri.square()
    print(f'Triangle square is {tri.square()}')


# triangle_calc(4,7,10)


def rectangle_calc(side_a, side_b):
    rec = Rectangle(side_a, side_b)
    print(f'Rectangle perimeter is {rec.perimeter()}')
    print(f'Rectangle square is {rec.square()}')


# rectangle_calc(4,7)


def square_calc(side_a):
    sq = Square(side_a)
    print(f'Square perimeter is {sq.perimeter()}')
    print(f'Square square is {sq.square()}')

# square_calc(5)


def input_figure():
    fig = input('Please select a figure: triangle / rectangle / square ')
    if fig == "triangle":
        side_a = input('Please enter triangle 1st side ')
        side_b = input('Please enter triangle 2nd side ')
        side_c = input('Please enter triangle 3rd side ')
        triangle_calc(int(side_a), int(side_b), int(side_c))
    elif fig == "rectangle":
        side_a = input('Please enter rectangle 1st side ')
        side_b = input('Please enter rectangle 2nd side ')
        rectangle_calc(int(side_a), int(side_b))
    elif fig == "square":
        side_a = input('Please enter square side ')
        square_calc(int(side_a))
    else:
        print(f'{fig} figure is not valid.')


input_figure()




