import math


class Vector2d:
    x = 0.0
    y = 0.0

    def __init__(self):
        self.x = 0.0
        self.y = 0.0

    # parameterized constructor
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # operator overloads
    def __add__(self, other):
        self.x = self.x + other.x
        self.y = self.y + other.y

    def __sub__(self, other):
        self.x = self.x - other.x
        self.y = self.y - other.y

    def __mul__(self, other):
        self.x = self.x * other
        self.y = self.y * other

    def __truediv__(self, other):
        self.x = self.x / other
        self.y = self.y / other

    # functions
    def zero(self):
        self.x = 0.0
        self.y = 0.0

    def isZero(self):
        return self.x == 0.0 and self.y == 0.0

    def length(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def lengthSq(self):
        return self.x ** 2 + self.y ** 2

    def normalize(self):
        l = self.length()
        self.x = (self.x / l)
        self.y = (self.y / l)

    def dot(self, vector):
        return self.x * vector.x + self.y * vector.y

    def sign(self, vector):
        if self.y * vector.x > self.x * vector.y:
            return -1
        else:
            return 1

    def perp(self):
        return Vector2d(-self.y, self.x)

    def distance(self, vector):
        ySeparation = vector.y - self.y;
        xSeparation = vector.x - self.x;

        return math.sqrt(ySeparation * ySeparation + xSeparation * xSeparation)

    def distanceSq(self, vector):
        ySeparation = vector.y - self.y;
        xSeparation = vector.x - self.x;

        return ySeparation * ySeparation + xSeparation * xSeparation

    def truncate(self, maxLength):
        if self.length() > maxLength:
            self.normalize()
            self = self * maxLength

    def reflect(self, normalizedVector):
        d = self.dot(normalizedVector) * 2.0
        reversed = normalizedVector.getReverse()
        reversed * d
        self += reversed

    def getReverse(self):
        return Vector2d(-self.x, -self.y);
