def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list gracefully
    return sum(numbers) / len(numbers)

# Example usage (this will now work correctly):
my_numbers = []
average = calculate_average(my_numbers)
print(f"The average is: {average}")

my_numbers = [10, 20, 30]
average = calculate_average(my_numbers)
print(f"The average is: {average}") 