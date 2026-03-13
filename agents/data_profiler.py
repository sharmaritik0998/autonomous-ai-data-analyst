import streamlit as st

def profile_data(df):

    st.write("Dataset Shape")
    st.write(df.shape)

    st.write("Column Types")
    st.write(df.dtypes)

    st.write("Missing Values")
    st.write(df.isnull().sum())

    st.write("Duplicate Rows")
    st.write(df.duplicated().sum())