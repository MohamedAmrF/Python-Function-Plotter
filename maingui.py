import sys
import time
import matplotlib as plt
import numpy as np
import random
plt.use('Qt5Agg')

from PySide2.QtWidgets import QApplication,QWidget,QLabel,QToolTip,QPushButton,QMessageBox, QDesktopWidget,QMainWindow,QDialog,QHBoxLayout,QVBoxLayout,QGroupBox
from PySide2.QtGui import QIcon,QPixmap,QFont
from PySide2.QtCore import QTimer

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure


class MplCanvas(FigureCanvasQTAgg):
    """class for matplotlib graphs
    """
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)