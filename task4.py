import math


class SquareGenerator:

    @staticmethod
    def generate_squares(start_range, end_range):
        return [x ** 2 for x in range(start_range, end_range + 1)]


squares = SquareGenerator.generate_squares(1, 10)

square_roots = [math.sqrt(x) for x in squares]

print(square_roots)



