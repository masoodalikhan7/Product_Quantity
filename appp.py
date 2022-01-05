
import streamlit as st
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OrdinalEncoder
from sklearn.ensemble import RandomForestRegressor
import pickle


from model_methods import predict

st.title("Quantity of Product")
st.markdown('**Objective** : Given details the model predicts the Quantity.')
st.markdown('The model predicts the Quantity by taking input from a particular : **Material, month, Vendor and Product** ')


def predict_class():
    data = ([Material,month,Vendor, Product])
    result = predict(data)
    st.write("The predicted Quantity in Kilograms(KG) is ",result)

st.markdown("**Please enter the details **")
    
Material = st.text_input('Enter Material', '')
month = st.text_input('Enter month', '')
Vendor = st.text_input('Enter Vendor', '')
Product = st.text_input('Enter Product', '')

if st.button("Make Prediction"):
    predict_class()