### app.py
import streamlit as st
import pandas as pd
from app_logic import evaluate_parameters, save_to_log

st.set_page_config(page_title="Predictive Maintenance - VMC", layout="wide")
st.title("Predictive Maintenance Dashboard")

st.markdown("""
#### Intelligent Evaluation for Machine Health and Product Quality
Use rule-based thresholds to assess part status, machine condition, and identify probable defects based on real-time inputs.
""")

# Create tabs
tab1, tab2 = st.tabs(["Manual Evaluation", "Batch Upload"])

# -----------------------------
# Manual Evaluation
# -----------------------------
with tab1:
    st.sidebar.header("Input Parameters")
    inputs = {
        'Cycle Time (s)': st.sidebar.slider("Cycle Time (s)", 20, 300, 90),
        'Job Count': st.sidebar.slider("Job Count", 0, 100, 10),
        'Machine Utilization (%)': st.sidebar.slider("Machine Utilization (%)", 0, 100, 75),
        'Spindle Speed (RPM)': st.sidebar.slider("Spindle Speed (RPM)", 500, 8000, 3000),
        'Feed Rate (mm/min)': st.sidebar.slider("Feed Rate (mm/min)", 50, 2000, 800),
        'Tool Wear (%)': st.sidebar.slider("Tool Wear (%)", 0, 100, 30),
        'Vibration Level (mm/s)': st.sidebar.slider("Vibration Level (mm/s)", 0, 30, 10),
        'Spindle Temperature (°C)': st.sidebar.slider("Spindle Temperature (°C)", 10, 100, 45),
        'Power Consumption (kWh)': st.sidebar.slider("Power Consumption (kWh)", 0, 600, 150),
    }

    if st.button("Run Evaluation"):
        result = evaluate_parameters(inputs)
        save_to_log(inputs, result, mode="manual")

        col1, col2 = st.columns(2)
        with col1:
            st.metric(label="Part Status", value=result['Part Status'])
            st.metric(label="Machine Status", value=result['Machine Status'])
        with col2:
            st.markdown("**🧠 Confidence Level**")
            st.progress(result['Confidence'] / 100)
            st.write(f"{result['Confidence']}%")

        st.markdown("---")
        st.subheader("Defect Diagnosis")
        for defect in result['Defect Types']:
            st.markdown(f"- {defect}")

        st.markdown("---")
        st.subheader("Parameter Analysis")
        detailed_df = pd.DataFrame(result['Detailed Results'])
        styled = detailed_df.style.applymap(
            lambda v: 'color: red; font-weight: bold' if v == "❌ Out of Range" else '',
            subset=['status']
        )
        st.dataframe(styled, use_container_width=True)

# -----------------------------
# Batch Upload
# -----------------------------
with tab2:
    st.subheader("Upload CSV File")
    uploaded_file = st.file_uploader("Choose a CSV file with input parameters", type="csv")

    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.success("File uploaded successfully.")
        st.write("Preview of uploaded data:")
        st.dataframe(df.head(), use_container_width=True)

        if st.button("Run Batch Evaluation"):
            results = []
            for _, row in df.iterrows():
                inputs = {
                    'Cycle Time (s)': row.get('Cycle Time (s)', 0),
                    'Job Count': row.get('Job Count', 0),
                    'Machine Utilization (%)': row.get('Machine Utilization (%)', 0),
                    'Spindle Speed (RPM)': row.get('Spindle Speed (RPM)', 0),
                    'Feed Rate (mm/min)': row.get('Feed Rate (mm/min)', 0),
                    'Tool Wear (%)': row.get('Tool Wear (%)', 0),
                    'Vibration Level (mm/s)': row.get('Vibration Level (mm/s)', 0),
                    'Spindle Temperature (°C)': row.get('Spindle Temperature (°C)', 0),
                    'Power Consumption (kWh)': row.get('Power Consumption (kWh)', 0),
                }
                res = evaluate_parameters(inputs)
                save_to_log(inputs, res, mode="batch")
                results.append({
                    **inputs,
                    "Part Status": res['Part Status'],
                    "Machine Status": res['Machine Status'],
                    "Confidence": res['Confidence'],
                    "Defect Types": ", ".join(res['Defect Types'])
                })

            result_df = pd.DataFrame(results)
            st.success("Batch evaluation completed.")
            st.dataframe(result_df, use_container_width=True)

            csv_output = result_df.to_csv(index=False).encode('utf-8')
            st.download_button(
                label="Download Results as CSV",
                data=csv_output,
                file_name="evaluated_results.csv",
                mime='text/csv'
            )

st.markdown("---")
st.caption("Developed for VMC-based industrial monitoring • Rule-based logic • Ready for integration with dashboards and smart systems.")
