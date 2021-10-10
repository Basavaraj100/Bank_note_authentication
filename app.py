# importing libraries
import numpy as np
import pickle
import pandas as pd
import streamlit as st 
from PIL import Image


#  loading the model
pickle_in = open("classifier.pkl","rb")
classifier=pickle.load(pickle_in)

# Defining main function

def main():
    st.title("Bank Authenticator")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit Bank Authenticator ML App </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    variance = st.number_input('Enter variance')
    skewness = st.number_input("Enter skewness")
    curtosis = st.number_input("Enter curtosis")
    entropy = st.number_input("Enter entropy")
    inp=[[variance,skewness,curtosis,entropy]]
    if st.button("Predict"):
        result=classifier.predict(inp)
        st.success(f'The output is {result}')
    

if __name__=='__main__':
    main()
    
    
    