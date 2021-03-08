import streamlit as st
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pickle import load

def predict(arr):
  # standardizer = load(open('pickle/Pickle.pkl', 'rb'))
  classifier = load(open('pickle/dump.pkl', 'rb'))
  # cleaned_input= standardizer.fit_transform(arr)
  prediction= classifier.predict(arr)

  return prediction


def main():
    st.image("img/future.jpeg", use_column_width = True)
    col1=st.number_input('Enter value for column1')
    col2=st.number_input('Enter value for column2')
    arr = np.array([col1,col2]).reshape(1,-1)
    arr = arr.astype('float64')
    prediction = predict(arr)
    click = st.button('SUBMIT')
    if click:
        if prediction==0:
            st.write('NO')
        else:
            st.write('YES')



if(__name__ == '__main__'):
    main()
