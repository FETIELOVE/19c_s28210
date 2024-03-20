from .square_generator import SquareGenerator


class CubicGenerator(SquareGenerator):
    @staticmethod
    def generate_cubes(start_range, end_range):
        return [x**3 for x in range(start_range, end_range + 1)]

    @staticmethod
    def generate_squares(start_range, end_range):
        if start_range > end_range:
            raise ValueError("Start of the range must be less than or equal to end.")
        return [x**2 for x in range(start_range, end_range + 1)]
