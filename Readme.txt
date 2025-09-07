# Fake Money Detection Web App

This is a Streamlit web application that predicts whether money is original or counterfeit based on input features using a trained machine learning model.

## Features

- User-friendly web interface
- Input fields for Variance, Skewness, Kurtosis, and Entropy
- Instant prediction of money authenticity

## Setup

1. **Clone the repository or download the files.**
2. **Install the required packages:**
    ```
    pip install -r requirements.txt
    ```
3. **Ensure `mondel.pkl` (your trained model) is in the project directory.**
4. **Run the app:**
    ```
    streamlit run app.py
    ```

## Usage

- Enter the values for Variance, Skewness, Kurtosis, and Entropy.
- Click the **Predict** button to see if the money is original or counterfeit.

## Requirements

See `requirements.txt` for dependencies.

## Notes

- Make sure your model file is named `mondel.pkl` or update the code if the filename is different.