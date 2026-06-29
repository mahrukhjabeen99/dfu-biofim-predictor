import streamlit as st
import pandas as pd

# 1. DATA INGESTION
@st.cache_data
def load_data():
    # Matches the exact name from your GitHub screenshot
    filename = 'Master_Integrated_NanoFormulation_Library_v6 (1).xlsx'
    # Use read_excel for .xlsx files
    df = pd.read_excel(filename)
    return {'nano_lib': df}

data_library = load_data()

# 2. EVIDENCE RETRIEVAL ENGINE
def get_evidence_based_result(user_size):
    df = data_library['nano_lib']
    # Filter for matches within a 10nm range
    # Ensure column name matches your Excel header exactly
    matches = df
