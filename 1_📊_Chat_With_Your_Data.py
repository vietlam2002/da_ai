import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from dotenv import load_dotenv

from langchain_experimental.agents.agent_toolkits.pandas.base import create_pandas_dataframe_agent
from langchain_openai import ChatOpenAI

from src.logger.base import BaseLogger

load_dotenv()
logger = BaseLogger()
MODEL_NAME = "gpt-3.5-turbo"


def main():
    
    #Setup streamlit interface
    st.set_page_config(page_title="📊 Smart Data Analysis Tool", page_icon="📊", layout="centered")
    st.header("📊 Smart Data Analysis Tool")
    st.write(
        "### Welcome to our data analysis tool. This tools can assist your daily data analysis tasks. Please enjoy !"
    )

    # Load llms model

    # Upload csv file
    with st.sidebar:
        uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])

    # Initial chat history

    # Read csv file

    # Create data analysis agent to query with our data

    # Input query and process query

    # Display chat history

if __name__ == "__main__":
    main()