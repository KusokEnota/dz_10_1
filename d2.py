"""Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей. Дано a, b, c - стороны
предполагаемого треугольника. Требуется сравнить длину каждого отрезка-стороны с суммой двух других. Если хотя бы в
 одном случае отрезок окажется больше суммы двух других, то треугольника с такими сторонами не существует. Отдельно
 сообщить является ли треугольник разносторонним, равнобедренным или равносторонним"""


class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def check_triangle_existence(self):
        if self.a + self.b <= self.c or self.a + self.c <= self.b or self.b + self.c <= self.a:
            return False
        return True

    def get_triangle_type(self):
        if self.a != self.b != self.c:
            return "Разносторонний"
        elif self.a == self.b == self.c:
            return "Равносторонний"
        else:
            return "Равнобедренный"


if __name__ == "__main__":
    a = int(input("Введите длину стороны a: "))
    b = int(input("Введите длину стороны b: "))
    c = int(input("Введите длину стороны c: "))

    triangle = Triangle(a, b, c)

    if not triangle.check_triangle_existence():
        print("Треугольник не существует")
    else:
        triangle_type = triangle.get_triangle_type()
        print(triangle_type)
