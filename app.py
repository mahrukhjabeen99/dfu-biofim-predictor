import streamlit as st
import pandas as pd

# 1. DATA INGESTION
@st.cache_data
def load_data():
    filename = 'Master_Integrated_NanoFormulation_Library_v6 (1).xlsx'
    df = pd.read_excel(filename)
    return {'nano_lib': df}

data_library = load_data()

# 2. EVIDENCE RETRIEVAL ENGINE
def get_evidence_based_result(user_size):
    df = data_library['nano_lib']
    # Filter for matches within a 10nm range (using first column as size)
    matches = df[(df.iloc[:, 0] >= user_size - 10) & (df.iloc[:, 0] <= user_size + 10)]
    
    if not matches.empty:
        # Assuming % Biofilm Reduction is the second column (index 1)
        result = matches.iloc[0, 1] 
        return f"Real Data Match: {result}% reduction."
    else:
        return "No match found in dataset."

# 3. INTERFACE
st.title("DFU Biofilm Modulation Predictor")
size = st.number_input("Mean Diameter (nm):", value=50.0)

if st.button("Generate Report"):
    report = get_evidence_based_result(size)
    st.info(report)
