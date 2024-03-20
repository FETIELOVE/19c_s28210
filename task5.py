class SquareGenerator:
    @staticmethod
    def generate_squares(start_range, end_range):
        if end_range < start_range:
            raise ValueError("End of the range must be greater than or equal to the start.")
        return [x ** 2 for x in range(start_range, end_range + 1)]

try:
    squares = SquareGenerator.generate_squares(10, 1)  # This will raise a ValueError
except ValueError:
    pass