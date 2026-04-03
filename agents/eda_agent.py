import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

def run_eda(df):
    numeric_cols = df.select_dtypes(include=['number']).columns

    st.write("Distribution Plots")

    for col in numeric_cols:
        fig, ax = plt.subplots()
        sns.histplot(df[col], kde=True, ax=ax)
        ax.set_title(f"Distribution of {col}")
        st.pyplot(fig)

    st.write("Correlation Heatmap")

    fig2, ax2 = plt.subplots()
    sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm", ax=ax2)
    st.pyplot(fig2)