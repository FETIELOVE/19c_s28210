def e_squares(start_range, end_range):
    squares = [x**2 for x in range(start_range, end_range + 1)]
    return squares


start = int(input("Enter the starting number of the range: "))
end = int(input("Enter the ending number of the range: "))
squares_list = e_squares(start, end)
print("List of squares of numbers from {} to {}:".format(start, end))
print(squares_list)
