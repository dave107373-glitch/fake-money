# create a streamlit app for the model
#import the libraries
import streamlit as st
import pandas as pd
import numpy as np
import pickle

# load the model
with open("mondel.pkl", "rb") as file:
    model = pickle.load(file)

# create a function for the prediction
def predict_fakemoney(features):
    prediction = model.predict([features])
    return prediction

# create the app
def main():
    st.title("Fake Money Detection Web App")
    st.write("Enter the features of the money to check if it is fake or not")
    
    st.subheader("Input Features")
    variance = st.number_input("Variance", format="%.4f", step=0.01, help="Enter the variance value")
    skewness = st.number_input("Skewness", format="%.4f", step=0.01, help="Enter the skewness value")
    kurtosis = st.number_input("Kurtosis", format="%.4f", step=0.01, help="Enter the kurtosis value")
    entropy = st.number_input("Entropy", format="%.4f", step=0.01, help="Enter the entropy value")
    
    if st.button("Predict"):
        features = [variance, skewness, kurtosis, entropy]
        prediction = predict_fakemoney(features)
        if prediction[0] == 0:
            st.success("Your Money is Original")
        else:
            st.error("It Is Counterfeit Money")

if __name__ == "__main__":
    main()