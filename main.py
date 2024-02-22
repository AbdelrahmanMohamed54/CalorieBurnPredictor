# -*- coding: utf-8 -*-
"""Calrories.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1kf3mmuPMVcjaqZ1dB_KPGVZBfZFY-5Gu

Install all the required dependencies
"""

"""Data Collection"""

#loading the data -> pandas DataFrame
calories_data= pd.read_csv('datafull.csv')

#print the data after the combination
calories_data.head()

#some information about the dataset
calories_data.info()

#Check if we have missing values
calories_data.isnull().sum()

correlation = calories_data.corr(numeric_only=True)

#Convert the Text data to numerical values
calories_data.replace({"Gender":{'male':0,'female':1}} , inplace=True)

calories_data.head()

"""Separating features and target"""

# Interaction term: Weight * Duration
calories_data['Weight_Duration_Interaction'] = calories_data['Weight'] * calories_data['Duration']

features_to_use = ['Gender', 'Height', 'Weight', 'Duration', 'Heart_Rate', 'Weight_Duration_Interaction']
X = calories_data[features_to_use]
Y = calories_data['Calories']

print(X)

print(Y)

