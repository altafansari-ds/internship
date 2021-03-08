import streamlit as st
import base64
import data_app
import ml_app
def main():
    # EDA
    data_app.main()

    st.header("Lets Predict:sunglasses:")

    # Predictor
    ml_app.main()



if(__name__ == '__main__'):
  main()
