import streamlit as st
import pandas as pd

# 1. DATA LOADING
@st.cache_data
def load_data():
    return {
        'nano_lib': pd.read_csv('Master_Integrated_NanoFormulation_Library_v6.xlsx - Nano Formulation Synthesis.csv'),
        'bamp': pd.read_csv('experiment (1).csv') 
    }

data = load_data()

# 2. PERSISTENCE SETUP
if 'app_data' not in st.session_state:
    st.session_state['app_data'] = {'nano_id': '', 'size': 50.0}

# 3. INTERFACE
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Phase 1: Metadata", "Phase 2: Characterization", "Phase 4: Prediction"])

if page == "Phase 1: Metadata":
    st.header("Phase 1: Metadata")
    st.session_state['app_data']['nano_id'] = st.text_input("Nano-ID:", value=st.session_state['app_data']['nano_id'])
    
elif page == "Phase 2: Characterization":
    st.header("Phase 2: Characterization")
    st.session_state['app_data']['size'] = st.number_input("Mean Diameter (nm):", value=st.session_state['app_data']['size'])

elif page == "Phase 4: Prediction":
    st.header("Phase 4: Prediction")
    if st.button("Generate Index"):
        df = data['nano_lib']
        size = st.session_state['app_data']['size']
        
        # Match using the column named 'particle size (nm, mean ± SD)'
        # Adjust the string below if your column name is different
        col_name = 'particle size (nm, mean ± SD)'
        matches = df[(df[col_name] >= size - 10) & (df[col_name] <= size + 10)]
        
        if not matches.empty:
            st.success(f"Result for {st.session_state['app_data']['nano_id']}: Match found.")
            st.dataframe(matches.head())
        else:
            st.warning(f"No match for {size}nm in library.")
