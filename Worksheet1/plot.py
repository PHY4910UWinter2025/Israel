import numpy as np
import matplotlib.pyplot as plt

# Define a function to plot data from a file
def plot_func(filename, column=None, xlim=None, ylim=None):
    """
    This function loads data from a file, extracts specified columns, and plots the data.
   
    Parameters:
    - filename (str): Path to the file containing data.
    - column (list): List of two integers specifying the columns to plot (x and y).
    - xlim (list): Optional, list of two floats specifying x-axis limits [xmin, xmax].
    - ylim (list): Optional, list of two floats specifying y-axis limits [ymin, ymax].
    """
    # Load the file data using numpy, assuming tab-delimited values
    # `skiprows=1` skips the header line if present
    data = np.loadtxt(filename, delimiter="\t", skiprows=1)

    # Extract x and y values from the specified columns
    x = data[:, column[0]]  # Get the first column specified in `column`
    y = data[:, column[1]]  # Get the second column specified in `column`

    # Create a new figure for the plot
    plt.figure()

    # Plot x vs. y with a green line
    plt.plot(x, y, color="green", label="values")

    # Add labels for x and y axes
    plt.xlabel("x")
    plt.ylabel("f(x)")

    # Add a title to the plot
    plt.title("Some Data")

    # Add a grid to the plot for better visualization
    plt.grid(True)

    # Save the plot as a PNG image file
    plt.savefig("some_data.png")

    # If x-axis limits (xlim) are provided, apply them
    if xlim:
        plt.xlim(xlim)

    # If y-axis limits (ylim) are provided, apply them
    if ylim:
        plt.ylim(ylim)

    # Display the plot to the user
    plt.show()


# Main script block to run the plot function when executed directly
if __name__ == "__main__":
    """
    Main section of the script:
    - Prompts the user for input parameters.
    """
    # Prompt the user to input the filename of the data file
    filename = input("Input your filename: ")

    # Prompt the user to input two column indices (x and y) to plot
    # Expected input format: two integers separated by a space (e.g., "0 1")
    column_value = input("Input two columns to plot (e.g., '0 1'): ")

    # Prompt the user to input x-axis limits if desired
    # Expected input format: two floats separated by a space (e.g., "0 10")
    xlim_value = input("Input 2 numbers for range for x axis (e.g., '0 10'): ")

    # Prompt the user to input y-axis limits if desired
    # Expected input format: two floats separated by a space (e.g., "-5 5")
    ylim_value = input("Input 2 numbers for range for y axis (e.g., '-5 5'): ")

    # Convert the input column indices into a list of integers
    # Example: if column_value = "0 1", this will convert it to [0, 1]
    column = list(map(int, column_value.split()))

    # Parse x-axis limits if provided; otherwise, set to None
    if xlim_value:
        xlim = list(map(float, xlim_value.split()))  # Convert to a list of floats
    else:
        xlim = None  # No limits provided

    # Parse y-axis limits if provided; otherwise, set to None
    if ylim_value:
        ylim = list(map(float, ylim_value.split()))  # Convert to a list of floats
    else:
        ylim = None  # No limits provided

    # Call the plot_func function with the parsed parameters
    plot_func(filename, column=column, xlim=xlim, ylim=ylim)


