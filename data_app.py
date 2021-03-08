import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import base64

dataset_loc="data/train.csv"
img_net="img/predict.jpeg"


def load_data(dataset1):
    df = pd.read_csv(dataset1)
    return df


def load_sidebar():
    st.sidebar.subheader("Lets predict")
    st.sidebar.success("YOU will get output as 1 which means yes and 0 means NO")


def load_description(df):
        st.header("Data Preview")
        preview = st.radio("Choose Head/Tail?", ("Top", "Bottom"))
        if(preview == "Top"):
            st.write(df.head())
        if(preview == "Bottom"):
            st.write(df.tail())

        #display the whole dataset
        if(st.checkbox("Show complete Dataset")):
             st.write(df)
        # Show shape
        if(st.checkbox("Display the shape")):
            st.write(df.shape)
            dim = st.radio("Rows/Columns?", ("Rows", "Columns"))
            if(dim == "Rows"):
                st.write("Number of Rows", df.shape[0])
            if(dim == "Columns"):
                st.write("Number of Columns", df.shape[1])

        # show columns
        if(st.checkbox("Show the Columns")):
            st.write(df.columns)


def main():

    # sidebar
    load_sidebar()
    # Title/ text
    st.title('LETS PREDICT')
    st.image(img_net, use_columnwidth = True)
    # display description
    df =load_data(dataset_loc)
    load_description(df)

if(__name__ == '__main__'):
    main()
