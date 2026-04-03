from utils.llm_client import generate_text

def answer_question(df, question):
    data_sample = df.sample(min(20, len(df))).to_string()

    prompt = f"""
    Dataset sample:
    {data_sample}

    Question:
    {question}

    Answer clearly based on the dataset.
    """

    return generate_text(prompt)