import sys
import time
import matplotlib as plt
import numpy as np
import random
plt.use('Qt5Agg')

from PySide2.QtWidgets import QApplication,QWidget,QLabel,QToolTip,QPushButton,QMessageBox, QDesktopWidget,QMainWindow,QDialog,QHBoxLayout,QVBoxLayout,QGroupBox,QLineEdit,QStatusBar
from PySide2.QtGui import QIcon,QPixmap,QFont
from PySide2.QtCore import QTimer

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure

from helpers.validation import *

class MplCanvas(FigureCanvasQTAgg):
    """class for matplotlib graphs
    """
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)

class MainWindow(QMainWindow):
    def __init__(self, win):
        super().__init__()
        self.setCentralWidget(win)
        self.createStatusBar()
        self.setWindowTitle("Function Plotter")
        self.setGeometry(900,700,900,700)
        self.setIcon()
        self.center()
        # self.StatusBarError('error', 'error')

    def setIcon(self):
        appIcon = QIcon("icon.png")
        self.setWindowIcon(appIcon)
        
    def center(self):
        qRect = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qRect.moveCenter(centerPoint)
        self.move(qRect.topLeft())

    def createStatusBar(self):
        self.myStatus = QStatusBar()
        self.myStatus.setStyleSheet("QStatusBar{padding-left:8px;color:green;font-weight:bold;}")
        self.myStatus.showMessage("✅ Ready", 5000)
        self.setStatusBar(self.myStatus)
    
    def StatusBarError(self, fxerror, minmaxerror):
        message = ""
        if fxerror == "error":
            message += "❗ Invalid, Enter Another Equation "
        if minmaxerror == "error":
            message += "❗ Invalid, Max should be greater than Min "
        QTimer.singleShot(10000, self.myStatus.setStyleSheet("QStatusBar{padding-left:8px;color:red;font-weight:bold;}")); 
        # self.myStatus.setStyleSheet("QStatusBar{padding-left:8px;color:red;font-weight:bold;}")
        self.myStatus.showMessage(message, 10000)

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.min = 1
        self.max = 1
        self.graph = MplCanvas(self, width=5, height=5, dpi=100)
        self.xdata = np.arange(self.min, self.max)
        self.ydata = np.zeros(self.max - self.min)
        self.setWindowTitle("Function Plotter")
        self.setGeometry(1000,800,1000,800)
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
        # self.xdata = self.nxdata
        # self.ydata = self.nydata
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
        button.clicked.connect(self.application)
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

    def make_fx_textbox(self):
        groupBox = QGroupBox()
        hbox = QHBoxLayout()
        self.linefx = QLineEdit(self)
        labelfx = QLabel(self)
        labelfx.setText("Fx: ")
        hbox.addWidget(labelfx)
        hbox.addWidget(self.linefx)
        groupBox.setLayout(hbox)
        return groupBox

    def make_range_boxes(self):
        groupBox = QGroupBox()
        hbox = QHBoxLayout()
        self.linemin = QLineEdit(self)
        labelmin = QLabel(self)
        labelmin.setText("Min: ")
        hbox.addWidget(labelmin)
        hbox.addWidget(self.linemin)

        self.linemax = QLineEdit(self)
        labelmax = QLabel(self)
        labelmax.setText("Max: ")
        hbox.addWidget(labelmax)
        hbox.addWidget(self.linemax)
        groupBox.setLayout(hbox)
        return groupBox


    def read_fx(self):
        return self.linefx.text()
    
    def read_min(self):
        return self.linemin.text()

    def read_max(self):
        return self.linemax.text()

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
        text_box = self.make_fx_textbox()
        range_boxes = self.make_range_boxes()
        canvas = self.plt_graph_widget([0], [0])    
        vbox.addWidget(text_box)
        vbox.addWidget(range_boxes)
        vbox.addWidget(canvas)
        vbox.addWidget(groupBoxHorizontal)
        self.groupBox.setLayout(vbox)

    def error_response(self, fx, minmax):
        """The response of the Invalid Input
        """
        message = ""
        if fx == "error":
            message += "❗ Invalid, Enter Another Equation \n"
        if minmax == "error":
            message += "❗ Invalid, Max should be greater than Min "
        userInfo = QMessageBox.question(self, "❗ Invalid Input", message,
                                        QMessageBox.Cancel)

        if userInfo == QMessageBox.Cancel:
                pass


    def application(self):
        equation = fix_equation(self.read_fx())
        l = int(self.read_min())
        r = int(self.read_max())+1
        fxerror = "valid"
        minmaxerror = "valid"
        if not input_validation(equation):
            fxerror = "error"
        if not validate_min_max(l, r):
            minmaxerror = "error"
        
        if fxerror=='error' or minmaxerror=='error':
            self.error_response(fxerror, minmaxerror)
            return
        
        # arrays to be plotted as x-axis and y-axis
        self.xdata = np.arange(l, r)
        self.ydata = np.zeros(r - l)
        for i in range(l, r):
            self.ydata[i-l] = F(i, equation)
        
        self.update_plot()

# Calling the Program
myApp = QApplication(sys.argv)
window = Window()
window.show()
myApp.exec_()
sys.exit(0)