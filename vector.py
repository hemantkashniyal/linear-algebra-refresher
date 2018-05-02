from math import sqrt, acos, degrees
from decimal import Decimal, getcontext

getcontext().prec = 30

class Vector(object):
    # error messages
    ERR_COORDINATES_MUST_BE_NON_EMPTY_MSG = 'The coordinates must be nonempty'
    ERR_COORDINATES_MUST_BE_ITERABLE_MSG = 'The coordinates must be an iterable'
    ERR_CANNOT_NORMALIZE_ZERO_VECTOR_MSG = 'Cannot normalize zero vector'
    ERR_CANNOT_COMPUTE_ANGLE_WITH_ZERO_VECTOR_MSG = 'Cannot compute angle with zero vector'

    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(coordinates)
            self.dimension = len(coordinates)

        except ValueError:
            raise ValueError(self.ERR_COORDINATES_MUST_BE_NON_EMPTY_MSG)

        except TypeError:
            raise TypeError(self.ERR_COORDINATES_MUST_BE_ITERABLE_MSG)


    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)


    def __eq__(self, v):
        return self.coordinates == v.coordinates

    def plus(self, v):
        new_coordinates = [x+y for x, y in zip(self.coordinates, v.coordinates)]
        return Vector(new_coordinates)

    def minus(self, v):
        new_coordinates = [x-y for x, y in zip(self.coordinates, v.coordinates)]
        return Vector(new_coordinates)

    def times_scalar(self, c):
        new_coordinates = [c*x for x in self.coordinates]
        return Vector(new_coordinates)

    def magnitude(self):
        sq_magnitude = sum([x**2 for x in self.coordinates])
        return sqrt(sq_magnitude)

    def normalized(self):
        try:
            return self.times_scalar(1.0/self.magnitude())
        except ZeroDivisionError:
            raise Exception(self.ERR_CANNOT_NORMALIZE_ZERO_VECTOR_MSG)

    def dot(self, v):
        new_coordinates = [x*y for x, y in zip(self.coordinates, v.coordinates)]
        return sum(new_coordinates)

    def angle_with(self, v, in_degrees = False):
        try:
            u1 = self.normalized()
            u2 = v.normalized()
            angle_radian = acos(u1.dot(u2))
            if in_degrees:
                return degrees(angle_radian)
            else:
                return angle_radian
        except Exception as e:
            if str(e) == self.ERR_CANNOT_NORMALIZE_ZERO_VECTOR_MSG:
                raise Exception(self.ERR_CANNOT_COMPUTE_ANGLE_WITH_ZERO_VECTOR_MSG)
            else:
                raise e

    def angle_degree(self, v):
        return degrees(self.angle_radian(v))

my_vector = Vector([1,2,3])
print my_vector
my_vector1 = Vector([1,2,3])
my_vector2 = Vector([-1,2,3])
print my_vector == my_vector1
print my_vector == my_vector2

v = Vector([8.218, -9.341])
w = Vector([-1.129, 2.111])
print v, w
print v.plus(w)

v = Vector([7.119, 8.215])
w = Vector([-8.223, 0.878])
print v, w
print v.minus(w)

v = Vector([1.671, -1.012, -0.318])
c = 7.41
print v, w
print v.times_scalar(c)

v = Vector([1, 1])
print v
print v.magnitude()

v = Vector([-0.221, 7.437])
print v
print v.magnitude()
print v.normalized()

v = Vector([8.813, -1.331, -6.247])
print v
print v.magnitude()
print v.normalized()

v = Vector([5.581, -2.136])
print v
print v.magnitude()
print v.normalized()

v = Vector([1.996, 3.108, -4.554])
print v
print v.magnitude()
print v.normalized()

v = Vector([7.887, 4.138])
w = Vector([-8.802, 6.776])
print v,w
print v.dot(w)

v = Vector([-5.955, -4.904, -1.874])
w = Vector([-4.496, -8.755, 7.103])
print v,w
print v.dot(w)

v = Vector([3.183, -7.627])
w = Vector([-2.668, 5.319])
print v,w
print v.angle_with(w)

v = Vector([7.35, 0.221, 5.188])
w = Vector([2.751, 8.259, 3.985])
print v,w
print v.angle_with(w, True)
