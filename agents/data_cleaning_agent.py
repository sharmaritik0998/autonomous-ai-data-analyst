def clean_data(df):

    df = df.drop_duplicates()

    for col in df.columns:

        if df[col].dtype != "object":
            df[col] = df[col].fillna(df[col].median())

        else:
            df[col] = df[col].fillna(df[col].mode()[0])

    return df