
## Calories Burnt Prediction System

## Project Description

The Calories Burnt Prediction System is an interactive application designed to estimate the number of calories burnt during exercises based on user inputs like height, weight, duration of training, and heart rate. This project integrates machine learning with a user-friendly GUI, providing users with instant predictions to assist in fitness and health planning.


## Installation

#### Prerequisites

- Python 3.10
- numpy==1.26.2
- matplotlib==3.8.2
- pandas==2.1.4
- PyQt6==6.6.1
- scikit-learn==1.3.2


#### Installation Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/AbdelrahmanMohamed54/CalorieBurnPredictor.git
   ```
2. Navigate to the project directory:
   ```bash
   cd CalorieBurnPredictor
   ```
3. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

## Basic Usage

### Starting the Project

1. Open a terminal in the project directory.
2. Run the application:
   ```bash
   python GUI.py
   ```
3. The GUI will launch, allowing you to input the required data and get calorie burn predictions.

## Implementation of the Requests

In this project, we implemented a machine learning model for predicting calories burnt. Below is a breakdown of the key components:

### Machine Learning Model (`main.py`)

- **Data Processing**: Loads and preprocesses the dataset.
- **Model Training**: Trains a Decision Tree Regressor model with hyperparameter tuning.
- **Prediction**: Predicts calories burnt based on user input.

### Graphical User Interface (`GUI.py`)

- **Input Fields**: Allows users to enter data such as height, weight, duration, and heart rate.
- **Prediction Button**: Triggers the prediction process when clicked.
- **Graph Area**: Displays a graphical representation of the prediction in relation to historical data.

### Dataset

- **File**: `datafull.csv`
- **Description**: Contains historical data on users' physical attributes and their corresponding calories burnt during exercises.

---
## Work Done 

- Graphical User Interface (Graphical User Interface (GUI) with PyQt)
- Pandas with Numpy (Data analysis with pandas and numpy)
- Visualization (with pandas and matplotlib)
- Scikit-Learn
- General Python Programming.

## Project Status

This project is currently in its final stages, with the primary objectives achieved. Future work may include enhancing the model's accuracy and expanding the GUI functionality.
