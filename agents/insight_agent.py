from utils.llm_client import generate_text

def generate_insights(df):

    summary = df.describe().to_string()

    prompt = f"""
    Analyze the dataset summary below and generate
    5 useful business insights.

    Dataset summary:
    {summary}
    """

    insights = generate_text(prompt)

    return insights.split("\n")