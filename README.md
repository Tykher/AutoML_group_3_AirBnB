

# Airbnb Price Prediction

## Overview

This project focuses on predicting Airbnb prices using machine learning models. The codebase includes data merging, cleaning, and the application of various regression models for accurate price predictions.

## Contents

1. [Introduction](#1-introduction)
2. [Data Merging](#2-data-merging)
3. [Data Cleaning](#3-data-cleaning)
4. [Applying Machine Learning Model](#4-applying-machine-learning-model)
5. [Optional: Tuning The Random Forest Model](#5-optional-tuning-the-random-forest-model)
6. [Results](#6-results)
7. [How to Use](#7-how-to-use)
8. [Dependencies](#8-dependencies)
9. [Saving the Model Locally](#9-saving-the-model-locally)
10. [UI using Streamlit](#10-ui-using-streamlit)
11. [License](#11-license)

## 1. Introduction

This project aims to predict Airbnb prices by merging datasets from multiple cities, cleaning the data, and applying various machine learning models. It includes an optional section for tuning the Random Forest model to enhance predictive accuracy.

## 2. Data Merging

- Merges datasets for weekdays and weekends across multiple cities.
- Concatenates datasets to create comprehensive DataFrames.
- Saves the combined dataset as 'airbnb_full_data.csv'.

## 3. Data Cleaning

- Encodes categorical variables and standardizes numerical data types.
- Removes irrelevant columns and handles missing values.
- Identifies and filters outliers using the Interquartile Range (IQR) method.
- Maps city names to numerical codes.
- Saves the cleaned dataset as 'airbnb_cleaned_data.csv'.

## 4. Applying Machine Learning Model

- Applies various regression models, including Linear Regression, Random Forest Regression, Decision Tree Regression, SVR, and Gradient Boosting Regression.
- Evaluates models using Mean Absolute Error (MAE), Root Mean Squared Log Error (RMSLE), and R-squared (R^2).
- Visualizes model predictions with scatter plots.

## 5. Optional: Tuning The Random Forest Model

- Conducts hyperparameter tuning for the Random Forest model.
- Compares the performance of the tuned model with the default Random Forest model.

## 6. Results

- Summarizes the outcomes of data merging, cleaning, and machine learning modeling stages.
- Presents evaluation metrics and visualizations.
- Describes optional tuning results for the Random Forest model.

## 7. How to Use

1. Clone the repository.
2. Install required dependencies.
3. Run the provided code in a Python environment.

## 8. Dependencies

- **pandas**: A powerful data manipulation and analysis library for Python. [Link to pandas](https://pandas.pydata.org/)
- **scikit-learn**: A machine learning library that provides simple and efficient tools for data analysis and modeling. [Link to scikit-learn](https://scikit-learn.org/)
- **matplotlib**: A comprehensive library for creating static, animated, and interactive visualizations in Python. [Link to matplotlib](https://matplotlib.org/)
- **numpy**: A fundamental package for scientific computing with Python. [Link to numpy](https://numpy.org/)

Install dependencies using:

```bash
pip install -r requirements.txt
```

## 9. Saving the Model Locally

To run the model and save it locally:

1. Open the 'data' folder.
2. Run the provided IPython notebook (`model_save.ipynb`) to generate and save the model locally.
3. Move the saved model file to the root repository.

Please note that the model file is large (5GB) and cannot be pushed to the repository. Running the notebook locally is necessary to obtain the model for UI functionality.

## 10. UI using Streamlit

The user interface (UI) for this project is implemented using Streamlit, a Python library for creating web applications. To launch the UI, run the following command in your terminal:

```bash
streamlit run app.py
```

Visit [Streamlit's website](https://streamlit.io/) for more information on using and customizing Streamlit applications.

## 11. License

This project is licensed under the [PJATK License](LICENSE).
