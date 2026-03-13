# Autonomous AI Data Analyst

## Project Overview

Autonomous AI Data Analyst is an AI-powered system that automatically analyzes datasets and generates insights.
The system allows users to upload CSV datasets, perform automatic data profiling, run exploratory data analysis (EDA), visualize data, and ask natural language questions about the dataset.

This project demonstrates how Large Language Models (LLMs) can be integrated with data science workflows to build intelligent data analysis tools.

---

App Link : https://autonomous-ai-data-analyst-ep9gqcryezicdm5nrjmiow.streamlit.app/

## Features

* Upload CSV datasets
* Automatic data profiling
* Data cleaning and preprocessing
* Exploratory Data Analysis (EDA)
* Interactive visualizations
* AI-generated insights
* Natural language question answering
* Streamlit web dashboard

---

## Technology Stack

Programming Language

* Python

Libraries

* Pandas
* NumPy
* Matplotlib
* Seaborn
* Plotly

AI / LLM

* Groq API (Llama 3)

Web Framework

* Streamlit

Version Control

* Git & GitHub

---

## Project Structure

```
autonomous_ai_data_analyst/
│
├── app.py
├── agents/
│   ├── data_profiler.py
│   ├── data_cleaning_agent.py
│   ├── eda_agent.py
│   ├── insight_agent.py
│   └── qa_agent.py
│
├── utils/
│   └── llm_client.py
│
├── sample_data/
│   └── sales_data.csv
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Installation

Clone the repository

```
git clone https://github.com/yourusername/autonomous-ai-data-analyst.git
```

Go to the project folder

```
cd autonomous-ai-data-analyst
```

Install dependencies

```
pip install -r requirements.txt
```

---

## Setup API Key

Create a `.env` file in the project root and add your Groq API key:

```
GROQ_API_KEY=your_api_key_here
```

Make sure `.env` is added in `.gitignore`.

---

## Run the Application

Start the Streamlit app:

```
streamlit run app.py
```

The application will open in your browser.

---

## Example Workflow

1. Upload a CSV dataset
2. The system profiles the dataset
3. Data cleaning is performed automatically
4. EDA charts are generated
5. AI generates business insights
6. Users can ask questions about the dataset

---

## Future Improvements

* Automatic chart selection using AI
* Report generation (PDF)
* Advanced anomaly detection
* Multi-dataset comparison
* Deployment on Streamlit Cloud

---

## Author

Ritik Sharma
Computer Science Engineering Student

---

## License

This project is for educational and research purposes.
