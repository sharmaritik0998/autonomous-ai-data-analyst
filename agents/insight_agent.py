from utils.llm_client import generate_text

def generate_insights(df):
    summary = df.describe(include='all').to_string()

    prompt = f"""
    Analyze the dataset summary below and generate
    5 meaningful business insights.

    Dataset summary:
    {summary}
    """

    insights = generate_text(prompt)

    return insights.split("\n")