import pandas as pd

def clean_data(df):
    df = df.copy()

    # Remove duplicates
    df = df.drop_duplicates()

    # Detect column types
    num_cols = df.select_dtypes(include=['number']).columns
    cat_cols = df.select_dtypes(include=['object', 'string', 'category']).columns

    # Clean numeric columns
    for col in num_cols:
        df[col] = pd.to_numeric(df[col], errors='coerce')
        df[col] = df[col].fillna(df[col].median())

    # Clean categorical columns
    for col in cat_cols:
        if df[col].mode().empty:
            df[col] = df[col].fillna("Unknown")
        else:
            df[col] = df[col].fillna(df[col].mode()[0])

    return df