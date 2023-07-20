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

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.min = 1
        self.max = 1
        self.graph = MplCanvas(self, width=5, height=5, dpi=100)
        self.xdata = np.arange(self.min, self.max)
        self.ydata = np.zeros(self.max - self.min)
        self.nmin = 1
        self.nmax = 10
        self.nxdata = np.arange(self.nmin, self.nmax)
        self.nydata = np.zeros(self.nmax - self.nmin)
        self.setWindowTitle("Function Plotter")
        self.setGeometry(800,600,800,600)
        self.setIcon()
        self.center()
        self.createLayout()

        vbox = QVBoxLayout()
        vbox.addWidget(self.groupBox)
        self.setLayout(vbox)



    def setIcon(self):
        """Sets the Gui Icon to the calculator image
        """
        appIcon = QIcon("icons/icon.png")
        self.setWindowIcon(appIcon)


    def quiteApp(self):
        """The response of the quit button, exits program
        """
        userInfo = QMessageBox.question(self, "Confirmation", "Do you want to quit ?",
                                        QMessageBox.Yes | QMessageBox.No)

        if userInfo == QMessageBox.Yes:
                myApp.quit()
        elif userInfo == QMessageBox.No:
                pass
    
    def center(self):
        """Lets the gui start exactly in the middle of the screen
        """
        qRect = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qRect.moveCenter(centerPoint)
        self.move(qRect.topLeft())
 
    def plt_graph_widget(self, xaxis, yaxis):
        """plots the arguments in using matplotlib + it's toolbar

        Args:
            xaxis (_type_): _description_
            yaxis (_type_): _description_

        Returns:
            QWidget: with a QVBoxLayout, matplotlib toolbar at the top and the graph beneath 
        """
        gw = self.graph
        gw.axes.plot(xaxis, yaxis)

        # Create a Tool bar and add the tool bar and the graph vertically
        toolbar = NavigationToolbar(gw, self)
        layout = QVBoxLayout()
        layout.addWidget(toolbar)
        layout.addWidget(gw)

        # Create widget to hold our toolbar and graph.
        widget = QWidget()
        widget.setLayout(layout)

        return widget


    def update_plot(self):
        """Response to the evaluate button, updates xaxis and yaxis data
        """
        self.graph.axes.cla()  # Clear the graph.
        self.xdata = self.nxdata
        self.ydata = self.nydata
        self.graph.axes.plot(self.xdata, self.ydata, 'r')
        # Trigger the graph to update and redraw.
        self.graph.draw()


    def make_evaluate_button(self):
        """Makes the evaluation button and connects it with the signal

        Returns:
            QPushButton: Button with specific Configurations
        """
        button = QPushButton("Evaluate")
        button.setIcon(QIcon("icons/calc.png"))
        button.setMinimumHeight(40)
        button.setToolTip("Plots your function 🙄")
        button.clicked.connect(self.update_plot)
        return button


    def make_quit_button(self):
        """Makes the quit button and connects it with the signal

        Returns:
            QPushButton: Button with specific Configurations
        """
        quitbutton = QPushButton("Quit", self)
        quitbutton.setIcon(QIcon("icons/quit2.png"))
        quitbutton.setToolTip("Unfortunately quits the program 😞")
        quitbutton.clicked.connect(self.quiteApp)
        return quitbutton

    def createLayout(self):
        """Makes the main layout of the Window

        Long Description:
            Puts buttons in an hbox
            puts graph and the hbox in a vbox layout

        Returns:
            QPushButton: Button with specific Configurations
        """
        self.groupBox = QGroupBox("Enter Your Equation: ")
        self.groupBox.setFont(QFont("Decorative", 15))
        groupBoxHorizontal = QGroupBox()
        hbox = QHBoxLayout()
        vbox = QVBoxLayout()

        # H box 
        button = self.make_evaluate_button()
        hbox.addWidget(button)
        quitbutton = self.make_quit_button()
        hbox.addWidget(quitbutton) 
        groupBoxHorizontal.setLayout(hbox)

        # V box
        canvas = self.plt_graph_widget([0], [0])    
        vbox.addWidget(canvas)
        vbox.addWidget(groupBoxHorizontal)
        self.groupBox.setLayout(vbox)

# Calling the Program
myApp = QApplication(sys.argv)
window = Window()
window.show()
myApp.exec_()
sys.exit(0)