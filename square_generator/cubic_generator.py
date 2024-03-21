from .generator_base import SquareGenerator


class CubicGenerator(SquareGenerator):

    def generate_squares(self, start_range, end_range):
        return [x ** 3 for x in range(start_range, end_range + 1)]
