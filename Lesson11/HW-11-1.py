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
        assert isinstance(side_a, int), 'Переменная должна быть типа int'
        assert isinstance(side_b, int), 'Переменная должна быть типа int'
        assert isinstance(side_c, int), 'Переменная должна быть типа int'
        self._validate_trinangle(side_a, side_b, side_c)
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    def _validate_trinangle(self, side_a, side_b, side_c):
        # add some validation
        # raise some error if not valid
        pass

    def perimeter(self):
        return self.side_a + self.side_b + self.side_c

    def square(self):
        per = self.perimeter() / 2
        return (per * (per - self.side_a) * (per - self.side_b) * (per - self.side_c)) ** 0.5


class Rectangle(Figure):
    def __init__(self, side_a, side_b):
        assert isinstance(side_a, int), 'Переменная должна быть типа int'
        assert isinstance(side_b, int), 'Переменная должна быть типа int'
        self._validate_rectangle(side_a, side_b)
        self.side_a = side_a
        self.side_b = side_b

    def _validate_rectangle(self, side_a, side_b):
        # add some validation
        # raise some error if not valid
        pass

    def perimeter(self):
        return (self.side_a + self.side_b) * 2

    def square(self):
        return self.side_a * self.side_b


class Square(Figure):
    def __init__(self, side_a):
        assert isinstance(side_a, int), 'Переменная должна быть типа int'
        self.side_a = side_a

    def perimeter(self):
        return self.side_a * 4

    def square(self):
        return self.side_a ** 2
