import numpy as np
import matplotlib.pyplot as plt

def main():
    print("Enter the coordinates as x,y (e.g., 1,2). Type 'done' to finish.")
    points = []
    
    while True:
        user_input = input("Enter coordinate (or 'done'): ").strip()
        if user_input.lower() == 'done':
            break
        try:
            x, y = map(float, user_input.split(','))
            points.append((x, y))
        except ValueError:
            print("Invalid format. Please enter coordinates as x,y.")
    
    if len(points) < 2:
        print("You need at least two points to calculate a best-fit line.")
        return
    
    # Separate x and y values
    x_values, y_values = zip(*points)
    
    # Calculate the slope with the constraint that the line passes through (0, 0)
    numerator = sum(x * y for x, y in zip(x_values, y_values))
    denominator = sum(x ** 2 for x in x_values)
    slope = numerator / denominator
    
    print(f"Slope of the constrained best-fit line: {slope:.2f}")
    labelx=input("Enter the label for X: ");
    labely=input("Enter the label for Y: ");
    title=input("Enter the title for the plot: ")
    
    # Generate the line values
    x_fit = np.linspace(min(x_values), max(x_values), 100)
    y_fit = slope * x_fit  # No intercept, so line starts at (0, 0)
    
    # Plot the points and the best-fit line
    plt.scatter(x_values, y_values, color='blue', label='Data Points')
    plt.plot(x_fit, y_fit, color='red', label=f'Best-Fit Line: y = {slope:.2f}x')
    plt.title(title)
    plt.xlabel(labelx)
    plt.ylabel(labely)
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()
