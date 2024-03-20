from .square_generator import SquareGenerator


class CubicGenerator(SquareGenerator):
    @staticmethod
    def generate_cubes(start_range, end_range):
        return [x**3 for x in range(start_range, end_range + 1)]
