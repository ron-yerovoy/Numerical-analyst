#work by:
#Ron Yerovoy 205591142
#Doron Spitzer 313262594 Doron 
#Naor Waitzenberg 315875997


# Lagrange Polynomial Interpolation
def lagrange(x_values, y_values, target_x):
    """
    Perform Lagrange Polynomial Interpolation.

    Parameters:
    x_values (list): List of x-values for the data points.
    y_values (list): List of y-values for the data points.
    target_x (float): The x-value where the interpolated value is required.

    Returns:
    float: The interpolated y-value at the specified x.
    """
    n = len(x_values)
    interpolated_y = 0.0

    for i in range(n):
        term = y_values[i]
        for j in range(n):
            if i != j:
                term *= (target_x - x_values[j]) / (x_values[i] - x_values[j])
        interpolated_y += term

    return interpolated_y

# Polynomial Interpolation using the general polynomial form
def general_polynomial_interpolation(x_values, y_values, target_x):
    """
    Perform Polynomial Interpolation using the general polynomial form.

    Parameters:
    x_values (list): List of x-values for the data points.
    y_values (list): List of y-values for the data points.
    target_x (float): The x-value where the interpolated value is required.

    Returns:
    float: The interpolated y-value at the specified x.
    """
    n = len(x_values)
    interpolated_y = 0.0

    for i in range(n):
        term = y_values[i]
        for j in range(n):
            if i != j:
                term *= (target_x - x_values[j]) / (x_values[i] - x_values[j])
        interpolated_y += term

    return interpolated_y

# Linear Interpolation
def linear(x_values, y_values, target_x):
    """
    Perform Linear Interpolation.

    Parameters:
    x_values (list): List of x-values for the data points.
    y_values (list): List of y-values for the data points.
    target_x (float): The x-value where the interpolated value is required.

    Returns:
    float: The interpolated y-value at the specified x.
    """
    for i in range(len(x_values) - 1):
        if x_values[i] <= target_x <= x_values[i + 1]:
            x1, y1 = x_values[i], y_values[i]
            x2, y2 = x_values[i + 1], y_values[i + 1]
            return y1 + (y2 - y1) * (target_x - x1) / (x2 - x1)
    raise ValueError("The provided x-value is out of the interpolation range.")

# Main code to use the interpolation methods
if __name__ == '__main__':
    x_values = [1, 5, 10]
    y_values = [1, 7, 12]
    target_x = 5  # The x-value for which interpolation is required

    # Prompt the user to select the interpolation method
    print("Select the interpolation method:")
    print("1. Lagrange Polynomial Interpolation")
    print("2. General Polynomial Interpolation")
    print("3. Linear Interpolation")
    method_choice = input("Enter the number corresponding to your choice: ")

    if method_choice == '1':
        interpolated_y = lagrange(x_values, y_values, target_x)
        method_name = "Lagrange Polynomial Interpolation"
    elif method_choice == '2':
        interpolated_y = general_polynomial_interpolation(x_values, y_values, target_x)
        method_name = "General Polynomial Interpolation"
    elif method_choice == '3':
        interpolated_y = linear(x_values, y_values, target_x)
        method_name = "Linear Interpolation"
    else:
        print("Invalid selection. Please restart the program and select a valid option.")
        exit()

    print(f"\n{method_name}:\nInterpolated value at x = {target_x} is y = {interpolated_y}")
