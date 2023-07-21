# test_function_plotter.py
import sys
import time
import matplotlib as plt
import numpy as np
import pytest
# import pytestqt
plt.use('Qt5Agg')

from PySide2.QtWidgets import QApplication,QWidget,QLabel,QToolTip,QPushButton,QMessageBox, QDesktopWidget,QMainWindow,QDialog,QHBoxLayout,QVBoxLayout,QGroupBox,QLineEdit,QStatusBar
from PySide2.QtGui import QIcon,QPixmap,QFont
from PySide2.QtCore import Qt

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure

from helpers.validation import *

# Import the main application code (you might need to change the import path based on your project structure)
from maingui import MainWindow, Window

# Test the GUI elements and their interactions
@pytest.fixture
def app(qtbot):
    test_app = QApplication(sys.argv)
    main_window = MainWindow(Window())
    qtbot.addWidget(main_window)
    yield qtbot, test_app, main_window
    test_app.quit()

def test_initial_gui_elements(app):
    qtbot, test_app, main_window = app

    # Check if the window is shown
    assert main_window.isVisible()

    # Check if the Evaluate button is present
    evaluate_button = main_window.findChild(QPushButton, "Evaluate")
    assert evaluate_button is not None

    # Check if the Quit button is present
    quit_button = main_window.findChild(QPushButton, "Quit")
    assert quit_button is not None

    # Check if the Fx textbox is present
    fx_textbox = main_window.findChild(QLineEdit)
    assert fx_textbox is not None

    # Check if the Min and Max range boxes are present
    min_range_box = main_window.findChild(QLineEdit, "Min")
    max_range_box = main_window.findChild(QLineEdit, "Max")
    assert min_range_box is not None
    assert max_range_box is not None

def test_invalid_input_error_message(app):
    qtbot, test_app, main_window = app

    fx_textbox = main_window.findChild(QLineEdit)
    min_range_box = main_window.findChild(QLineEdit, "Min")
    max_range_box = main_window.findChild(QLineEdit, "Max")
    evaluate_button = main_window.findChild(QPushButton, "Evaluate")

    # Enter an invalid equation in the Fx textbox and trigger the Evaluate button
    invalid_equation = "invalid equation"
    fx_textbox.setText(invalid_equation)
    min_range_box.setText("1")
    max_range_box.setText("10")
    qtbot.mouseClick(evaluate_button, Qt.LeftButton)

    # Check if the error message is displayed in the status bar
    status_bar = main_window.myStatus
    assert "❗ Invalid, Enter Another Equation" in status_bar.currentMessage()

    # Enter a valid equation and an invalid Min-Max range, then trigger the Evaluate button
    valid_equation = "x**2"
    fx_textbox.setText(valid_equation)
    min_range_box.setText("20")
    max_range_box.setText("10")
    qtbot.mouseClick(evaluate_button, Qt.LeftButton)

    # Check if the error message is displayed in the status bar
    assert "❗ Invalid, Max should be greater than Min" in status_bar.currentMessage()

def test_valid_input(app):
    qtbot, test_app, main_window = app

    fx_textbox = main_window.findChild(QLineEdit)
    min_range_box = main_window.findChild(QLineEdit, "Min")
    max_range_box = main_window.findChild(QLineEdit, "Max")
    evaluate_button = main_window.findChild(QPushButton, "Evaluate")

    # Enter a valid equation and valid Min-Max range, then trigger the Evaluate button
    valid_equation = "x**2"
    fx_textbox.setText(valid_equation)
    min_range_box.setText("1")
    max_range_box.setText("10")
    qtbot.mouseClick(evaluate_button, Qt.LeftButton)

    # Wait for the plot to be updated (you can adjust this sleep time based on your application)
    time.sleep(1)

    # Check if the plot is displayed correctly (you might need to modify this based on your application)
    graph = main_window.graph
    assert graph.xdata.tolist() == list(range(1, 11))
    assert graph.ydata.tolist() == [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# Add more test cases as needed to cover other features and scenarios
