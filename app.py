import streamlit as st
import pandas as pd

# 1. DATA INGESTION
@st.cache_data
def load_data():
    # Ensure all your CSV filenames match these exactly
    file_mapping = {
        'nano_lib': 'Master_Integrated_NanoFormulation_Library_v6.xlsx - Nano Formulation Synthesis.csv',
        'study_data': 'Nanoparticle_Biofilm_Study_Data_16.xlsx - Study Data.csv'
    }
    return {key: pd.read_csv(filename) for key, filename in file_mapping.items()}

data_library = load_data()

# 2. EVIDENCE RETRIEVAL ENGINE
def get_evidence_based_result(user_size):
    df = data_library['nano_lib']
    # Searches for a match within a 10nm range
    matches = df[(df['particle size (nm, mean ± SD)'] >= user_size - 10) & 
                 (df['particle size (nm, mean ± SD)'] <= user_size + 10)]
    
    if not matches.empty:
        result = matches.iloc[0]['% Biofilm Reduction']
        doi = matches.iloc[0]['Paper DOI']
        return f"Real Data Match: {result}% reduction. Source: {doi}"
    return "No match found in dataset."

# 3. INTERFACE PHASES
def main():
    st.title("DFU Biofilm Modulation Predictor")
    page = st.sidebar.selectbox("Phase", ["1: Metadata", "2: Characterization", "3: Assay Results", "4: Prediction"])

    if page == "1: Metadata":
        st.header("Metadata Input")
        st.selectbox("Select Pathogen:", ["S. aureus + P. aeruginosa", "S. aureus", "P. aeruginosa"])
        
    elif page == "2: Characterization":
        st.header("Characterization")
        size = st.number_input("Mean Diameter (nm):", value=50.0)
        st.session_state['size'] = size
        
    elif page == "3: Assay Results":
        st.header("Assay Results")
        mic = st.number_input("MIC (µg/mL):")
        
    elif page == "4: Prediction":
        st.header("Evidence-Based Prediction")
        if st.button("Generate Report"):
            report = get_evidence_based_result(st.session_state.get('size', 50))
            st.info(report)

if __name__ == "__main__":
    main()
