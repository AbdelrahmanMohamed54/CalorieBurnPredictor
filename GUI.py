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

        # Gender Selection - QComboBox
        self.genderComboBox = QComboBox()
        self.genderComboBox.addItems(["Male", "Female"])
        gridLayout.addWidget(self.genderComboBox, 0, 0)

        # Weight Input
        self.weightLabel = QLabel("Weight (kg)")
        self.weightSlider = QSlider(Qt.Orientation.Horizontal)
        self.weightSpinBox = QSpinBox()
        self.weightSlider.setMinimum(30)
        self.weightSlider.setMaximum(200)
        self.weightSpinBox.setMinimum(30)
        self.weightSpinBox.setMaximum(200)
        self.weightSlider.valueChanged.connect(self.weightSpinBox.setValue)
        self.weightSpinBox.valueChanged.connect(self.weightSlider.setValue)
        gridLayout.addWidget(self.weightLabel, 1, 0)
        gridLayout.addWidget(self.weightSlider, 1, 1)
        gridLayout.addWidget(self.weightSpinBox, 1, 2)

        # Height Input
        self.heightLabel = QLabel("Height (cm)")
        self.heightSlider = QSlider(Qt.Orientation.Horizontal)
        self.heightSpinBox = QSpinBox()
        self.heightSlider.setMinimum(100)
        self.heightSlider.setMaximum(250)
        self.heightSpinBox.setMinimum(100)
        self.heightSpinBox.setMaximum(250)
        self.heightSlider.valueChanged.connect(self.heightSpinBox.setValue)
        self.heightSpinBox.valueChanged.connect(self.heightSlider.setValue)
        gridLayout.addWidget(self.heightLabel, 2, 0)
        gridLayout.addWidget(self.heightSlider, 2, 1)
        gridLayout.addWidget(self.heightSpinBox, 2, 2)

        # Duration Input
        self.durationLabel = QLabel("Duration (min)")
        self.durationSlider = QSlider(Qt.Orientation.Horizontal)
        self.durationSpinBox = QSpinBox()
        self.durationSlider.setMinimum(0)
        self.durationSlider.setMaximum(30)
        self.durationSpinBox.setMinimum(0)
        self.durationSpinBox.setMaximum(30)
        self.durationSlider.valueChanged.connect(self.durationSpinBox.setValue)
        self.durationSpinBox.valueChanged.connect(self.durationSlider.setValue)
        gridLayout.addWidget(self.durationLabel, 3, 0)
        gridLayout.addWidget(self.durationSlider, 3, 1)
        gridLayout.addWidget(self.durationSpinBox, 3, 2)

        # Heartbeat Input
        self.heartbeatLabel = QLabel("Heartbeat (bpm)")
        self.heartbeatSlider = QSlider(Qt.Orientation.Horizontal)
        self.heartbeatSpinBox = QSpinBox()
        self.heartbeatSlider.setMinimum(40)
        self.heartbeatSlider.setMaximum(200)
        self.heartbeatSpinBox.setMinimum(40)
        self.heartbeatSpinBox.setMaximum(200)
        self.heartbeatSlider.valueChanged.connect(self.heartbeatSpinBox.setValue)
        self.heartbeatSpinBox.valueChanged.connect(self.heartbeatSlider.setValue)
        gridLayout.addWidget(self.heartbeatLabel, 4, 0)
        gridLayout.addWidget(self.heartbeatSlider, 4, 1)
        gridLayout.addWidget(self.heartbeatSpinBox, 4, 2)

        # Predict Button - Custom Animation Needed
        self.predictButton = QPushButton("Predict Calories")
        gridLayout.addWidget(self.predictButton, 5, 0, 1, 3)  # Span across three columns
        self.predictButton.clicked.connect(self.predictCalories)

        # Create a vertical layout for graph and prediction result
        graphAndResultLayout = QVBoxLayout()

        # Graph Area
        self.graphTabs = QTabWidget()
        graphAndResultLayout.addWidget(self.graphTabs)  # Add graph to the vertical layout

        # Label for Displaying Predicted Calories
        self.predictionResultLabel = QLabel("Predicted Calories: ")
        graphAndResultLayout.addWidget(self.predictionResultLabel)  # Add label below the graph
        graphAndResultLayout.setAlignment(self.predictionResultLabel, Qt.AlignmentFlag.AlignCenter)  # Center the label

        # Add the vertical layout to the grid
        gridLayout.addLayout(graphAndResultLayout, 0, 3, 6, 1)  # Span 6 rows and 1 column

        # Theme Selection ComboBox
        self.themeComboBox = QComboBox()
        self.themeComboBox.addItems(["Light Mode", "Dark Mode", "High Contrast"])
        self.themeComboBox.currentTextChanged.connect(self.applyStyles)  # Connect to applyStyles
        gridLayout.addWidget(self.themeComboBox, 7, 0, 1, 4)

    def defineStyleSheets(self):
        self.lightStyleSheet = """

        """

        self.darkStyleSheet = """
            QWidget {
                background-color: #424242;
                color: #E0E0E0;
            }
            QPushButton {
                background-color: #616161;
                border: 1px solid #757575;
            }
            QPushButton:hover {
                background-color: #757575;
            }
        """

        self.highContrastStyleSheet = """
            QWidget {
                background-color: #000000;
                color: #FFFFFF;
            }
            QPushButton {
                background-color: #FFFFFF;
                color: #000000;
                border: 2px solid #FFFFFF;
            }
            QPushButton:hover {
                background-color: #E0E0E0;
                color: #000000;
            }
        """

    def applyStyles(self, theme):
        if theme == "Light Mode":
            self.setStyleSheet(self.lightStyleSheet)
        elif theme == "Dark Mode":
            self.setStyleSheet(self.darkStyleSheet)
        elif theme == "High Contrast":
            self.setStyleSheet(self.highContrastStyleSheet)

    def predictCalories(self):
        # Collect input data
        gender = self.genderComboBox.currentText()
        gender = 0 if gender == 'Male' else 1
        weight = self.weightSpinBox.value()
        height = self.heightSpinBox.value()
        duration = self.durationSpinBox.value()
        Heart_Rate = self.heartbeatSpinBox.value()


        # Prepare input data for the model
        input_data = {'Gender': gender, 'Height': height, 'Weight': weight, 'Duration': duration,
                      'Heart_Rate': Heart_Rate}

        # Predict calories
        duration = self.durationSpinBox.value()  # get duration from the spin box
        predicted_calories = self.model.predict(input_data)

        # Update the label with the prediction
        self.predictionResultLabel.setText(f"Predicted Calories: {predicted_calories:.2f}")

        # Print the prediction in the console
        print(f"Predicted Calories: {predicted_calories}")

        # Update the graph with the prediction
        self.updateGraph(duration, predicted_calories)

    def updateGraph(self, duration, predicted_calories):
            if self.durations is not None and self.Y_test is not None and self.results_df_tuned is not None:
                # Create the matplotlib figure and axes
                fig, ax = plt.subplots(figsize=(10, 6))

                # Scatter plot for actual calories
                ax.scatter(self.durations, self.Y_test, label='Actual Calories', alpha=0.4)

                # Line plot for tuned predictions
                ax.plot(self.results_df_tuned['Duration'], self.results_df_tuned['Predicted Calories'],
                        label='Predicted Calories', color='red', linewidth=1.7)

                # Plot the point for the current prediction
                ax.scatter([duration], [predicted_calories], color='gold', s=150, marker='*',
                           label='Current Prediction')

                # Set labels, title, grid, etc.
                ax.set_title('Actual vs. Predicted Calories Over Duration')
                ax.set_xlabel('Duration')
                ax.set_ylabel('Calories')
                ax.legend()
                ax.grid(True)

                # Create a canvas to display the plot
                canvas = FigureCanvas(fig)

                # Clear the previous graph and add the new one
                self.clearGraphArea()
                self.graphTabs.addTab(canvas, "Calories Plot")

    def clearGraphArea(self):
        # Clear any existing graphs from the graph area
        while self.graphTabs.count() > 0:
            widget = self.graphTabs.widget(0)
            self.graphTabs.removeTab(0)
            widget.deleteLater()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CaloriesPredictor()
    window.show()
    sys.exit(app.exec())
