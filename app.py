import streamlit as st
import pandas as pd

# Initialize data storage
if 'app_data' not in st.session_state:
    st.session_state['app_data'] = {'p1': {}, 'p2': {}, 'p3': {}}

st.title("DFU Biofilm Modulation Predictor")

# Navigation Sidebar
page = st.sidebar.radio("Navigation", ["Phase 1: Metadata", "Phase 2: Characterization", "Phase 3: Assay Results", "Phase 4: Prediction"])

# --- PHASE 1 ---
if page == "Phase 1: Metadata":
    st.header("Phase 1: Metadata Input")
    st.session_state['app_data']['p1']['Wound'] = st.selectbox("Wound Type:", ["Diabetic Foot Ulcer"])
    st.session_state['app_data']['p1']['Bacteria'] = st.selectbox("Bacteria:", ["S. aureus + P. aeruginosa"])
    st.session_state['app_data']['p1']['Nano_ID'] = st.text_input("Nano-ID:")

# --- PHASE 2 ---
elif page == "Phase 2: Characterization":
    st.header("Phase 2: Physicochemical Characterization")
    st.session_state['app_data']['p2']['Size'] = st.number_input("Mean Diameter (nm):")
    st.session_state['app_data']['p2']['Zeta'] = st.number_input("Zeta Potential (mV):")

# --- PHASE 3 ---
elif page == "Phase 3: Assay Results":
    st.header("Phase 3: Assay Results")
    st.session_state['app_data']['p3']['OD'] = st.number_input("Biofilm Mass (OD value):")
    st.session_state['app_data']['p3']['MIC'] = st.number_input("MIC (µg/mL):")

# --- PHASE 4 ---
elif page == "Phase 4: Prediction":
    st.header("Phase 4: Synergy & Prediction")
    if st.button("Generate Modulation Efficacy Index"):
        # Logic to calculate result based on stored session data
        size = st.session_state['app_data']['p2'].get('Size', 0)
        # Placeholder for your correlation logic
        st.write(f"Calculating for Particle Size: {size}nm...")
        st.metric(label="Modulation Efficacy Index (MEI)", value="82 (High Efficacy)")
