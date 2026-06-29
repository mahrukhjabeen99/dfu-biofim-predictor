import streamlit as st
import pandas as pd

# 1. PERSISTENT DATA LOADING
@st.cache_data
def load_data():
    return {
        'nano_lib': pd.read_csv('Master_Integrated_NanoFormulation_Library_v6.xlsx - Nano Formulation Synthesis.csv'),
        'study_data': pd.read_csv('Nanoparticle_Biofilm_Study_Data_16.xlsx - Study Data.csv'),
        'agg_data': pd.read_csv('Aggregated_Research_Data_v6.xlsx - Research Data Matrix.csv'),
        'bio_v10': pd.read_csv('Biofilm_Nanoparticle_Research_Data_V10.xlsx - Research Data.csv'),
        'bio_final': pd.read_csv('Biofilm_Research_Data_Final_v4.xlsx - Biofilm Data.csv'),
        'cons_data': pd.read_csv('Consolidated_Biofilm_Data_Final.xlsx - Biofilm Data.csv'),
        'peptide': pd.read_csv('DFU_Peptide_Database.xlsx - Sheet1.csv'),
        'bamp': pd.read_csv('experiment (1).csv') # As requested
    }

data = load_data()

# 2. INITIALIZE SESSION STATE
if 'app_data' not in st.session_state:
    st.session_state['app_data'] = {'p1': {}, 'p2': {}, 'p3': {}}

# 3. NAVIGATION
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Phase 1: Metadata", "Phase 2: Characterization", "Phase 3: Assay Results", "Phase 4: Prediction"])

# 4. PERSISTENT INPUTS
if page == "Phase 1: Metadata":
    st.header("Phase 1: Metadata")
    st.session_state['app_data']['nano_id'] = st.text_input("Nano-ID:", value=st.session_state['app_data'].get('nano_id', ''))
    
elif page == "Phase 2: Characterization":
    st.header("Phase 2: Characterization")
    st.session_state['app_data']['size'] = st.number_input("Mean Diameter (nm):", value=st.session_state['app_data'].get('size', 50.0))
    st.session_state['app_data']['zeta'] = st.number_input("Zeta Potential (mV):", value=st.session_state['app_data'].get('zeta', 0.0))

elif page == "Phase 3: Assay Results":
    st.header("Phase 3: Assay Results")
    st.session_state['app_data']['od'] = st.number_input("Biofilm Mass (OD):", value=st.session_state['app_data'].get('od', 0.0))
    st.session_state['app_data']['mic'] = st.number_input("MIC (µg/mL):", value=st.session_state['app_data'].get('mic', 0.0))

elif page == "Phase 4: Prediction":
    st.header("Phase 4: Prediction")
    if st.button("Generate Modulation Efficacy Index"):
        # Example logic: Search in the primary nano_lib
        df = data['nano_lib']
        size = st.session_state['app_data'].get('size', 50.0)
        
        # Simple proximity matching
        matches = df[(df.iloc[:, 0] >= size - 10) & (df.iloc[:, 0] <= size + 10)]
        
        if not matches.empty:
            st.success(f"Match Found: {matches.iloc[0, 1]}% reduction.")
        else:
            st.warning("No direct match in the library.")
            
        st.write("Summary of your input:")
        st.json(st.session_state['app_data'])
