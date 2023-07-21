# Function Plotter

The Function Plotter is a simple PyQt application that allows users to input a mathematical function and plot its graph within a specified range. The application provides a graphical user interface (GUI) for users to interact with.

## Features

- Input a mathematical function (e.g., `x^2 + 2*x + 1`).
- Set the range of x-values (Min and Max) to be plotted.
- Plot the graph of the function within the specified range.
- Interactive GUI with buttons to Evaluate and Quit the application.
- Status bar to show messages to the user.

## Dependencies

- Python 3.x
- PySide2: `pip install PySide2`
- NumPy: `pip install numpy`
- Matplotlib: `pip install matplotlib`

## How to Run

1. Install the required dependencies using the provided `requirements.txt` or manually using the commands mentioned above.
2. Execute the application by running the `main.py` script.
3. The Function Plotter GUI will appear, allowing you to input the function and range for plotting.
4. Click the "Evaluate" button to plot the graph of the function within the specified range.
5. Click the "Quit" button to exit the application.

## How to Use

1. Enter a valid mathematical function in the Fx textbox (e.g., `x**2 + 2*x + 1`).
2. Specify the Min and Max values for the x-axis range.
3. Click the "Evaluate" button to plot the graph of the function within the specified range.
4. The graph will be displayed below the input fields, and you can interact with the plot using the provided Matplotlib toolbar.
5. If there are any errors in the input (invalid function or Min-Max range), an error message will be displayed in the status bar.

## Testing

Automated tests have been provided using `pytest` and `pytest-qt` to cover the main features of the application. To run the tests, use the following command:

```bash
pytest test_function_plotter.py