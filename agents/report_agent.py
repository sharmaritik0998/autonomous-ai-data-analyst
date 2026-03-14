from fpdf import FPDF
from utils.llm_client import generate_text

def generate_report(df):

    summary = df.describe().to_string()

    prompt = f"""
    You are a professional data analyst.

    Analyze the dataset summary and generate insights.

    Dataset summary:
    {summary}

    Write a short data analysis report including:
    - dataset overview
    - key insights
    - recommendations
    """

    insights = generate_text(prompt)

    pdf = FPDF()
    pdf.add_page()

    pdf.set_font("Arial", size=12)

    for line in insights.split("\n"):
        pdf.multi_cell(0, 8, line)

    file_name = "data_analysis_report.pdf"

    pdf.output(file_name)

    return file_name