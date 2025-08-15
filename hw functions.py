import math

def calculate_circumference(radius):
    """
    Function to calculate the circumference of a circle.
    :param radius: Radius of the circle
    :return: Circumference of the circle
    """
    if radius < 0:
        return "Radius cannot be negative."
    return 2 * math.pi * radius

# Example usage
radius = float(input("Enter the radius of the circle: "))
circumference = calculate_circumference(radius)
print(f"The circumference of the circle is: {circumference}")
