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
```

## Picture Examples

### Valid Examples
![Screenshot (654)](https://github.com/MohamedAmrF/Python-Function-Plotter/assets/78857431/419ad077-1832-4f30-bc32-5da49c584add)
![Screenshot (655)](https://github.com/MohamedAmrF/Python-Function-Plotter/assets/78857431/5e7c24b3-c907-4729-ad23-ed738db9d954)
![Screenshot (656)](https://github.com/MohamedAmrF/Python-Function-Plotter/assets/78857431/8a24df7c-8dc8-41c0-97bd-ebbf457773be)
![Screenshot (657)](https://github.com/MohamedAmrF/Python-Function-Plotter/assets/78857431/17d3eafc-5c43-4557-8e83-b663916920da)

![Screenshot (660)](https://github.com/MohamedAmrF/Python-Function-Plotter/assets/78857431/1b516ab3-1e2f-48fc-836c-9a8e36c0d9ea)

![Screenshot (659)](https://github.com/MohamedAmrF/Python-Function-Plotter/assets/78857431/a144160a-697a-4664-bd94-aecaaa8d5a5b)

![Screenshot (658)](https://github.com/MohamedAmrF/Python-Function-Plotter/assets/78857431/2e3b265d-0647-4174-9af0-12ceda7842ca)


## Invalid Examples:

![Screenshot (665)](https://github.com/MohamedAmrF/Python-Function-Plotter/assets/78857431/5ff23b1d-b038-4091-9eac-88362c04a151)
![Screenshot (664)](https://github.com/MohamedAmrF/Python-Function-Plotter/assets/78857431/80c129f0-e9d7-4193-bd1a-cc1a8c9a87cb)
![Screenshot (663)](https://github.com/MohamedAmrF/Python-Function-Plotter/assets/78857431/7741fc78-e7f2-484e-ad4f-f8f39b614389)

![Screenshot (662)](https://github.com/MohamedAmrF/Python-Function-Plotter/assets/78857431/109ec1cd-f9f8-4637-9ede-32d2cee16b81)

![Screenshot (661)](https://github.com/MohamedAmrF/Python-Function-Plotter/assets/78857431/bd9e9516-79bb-46fa-9b7b-e46d48a4b7a6)
