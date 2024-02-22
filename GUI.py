import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QGridLayout,
                             QSlider, QSpinBox, QPushButton, QLabel, QTabWidget,
                             QVBoxLayout, QComboBox)
from PyQt6.QtCore import Qt
import matplotlib
matplotlib.use('QtAgg')
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from main import CaloriePredictorModel


class CaloriesPredictor(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.defineStyleSheets()
        self.model = CaloriePredictorModel()
        self.durations, self.Y_test, self.results_df_tuned = self.model.get_plotting_data()

    def initUI(self):
        # Main Window Setup
        self.setWindowTitle("Calculate Calories")
        self.setGeometry(100, 100, 1200, 600)  # x, y, width, height

        # Central Widget and Layout
        centralWidget = QWidget()
        self.setCentralWidget(centralWidget)
        gridLayout = QGridLayout(centralWidget)

