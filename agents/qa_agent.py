from utils.llm_client import generate_text

def answer_question(df, question):

    data_sample = df.head(10).to_string()

    prompt = f"""
    Dataset sample:
    {data_sample}

    Question:
    {question}

    Answer clearly based on the dataset.
    """

    answer = generate_text(prompt)

    return answer