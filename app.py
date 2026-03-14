import streamlit as st
import pandas as pd

from agents.report_agent import generate_report #changes 
from agents.data_profiler import profile_data
from agents.data_cleaning_agent import clean_data
from agents.eda_agent import run_eda
from agents.insight_agent import generate_insights
from agents.qa_agent import answer_question


st.title("Autonomous AI Data Analyst")


uploaded_file = st.file_uploader("Upload CSV Dataset", type=["csv"])


if uploaded_file:

    df = pd.read_csv(uploaded_file)

    st.subheader("Dataset Preview")
    st.write(df.head())


    st.subheader("Data Profiling")
    profile_data(df)


    st.subheader("Data Cleaning")
    clean_df = clean_data(df)

    st.write(clean_df.head())


    st.subheader("Exploratory Data Analysis")
    run_eda(clean_df)


    st.subheader("AI Generated Business Insights")

    insights = generate_insights(clean_df)

    for i in insights:
        st.write(i)


    st.subheader("Ask Questions About Dataset")

    question = st.text_input("Enter your question")

    if question:

        answer = answer_question(clean_df, question)

        st.write(answer)

st.subheader("Generate AI Data Report")

if st.button("Generate PDF Report"):

    report_path = generate_report(df)

    with open(report_path, "rb") as file:
        st.download_button(
            label="Download Report",
            data=file,
            file_name="data_analysis_report.pdf",
            mime="application/pdf"
        )