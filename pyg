from pygwalker.api.streamlit import StreamlitRenderer
import pandas as pd
import streamlit as st

# Adjust the width of the Streamlit page
st.set_page_config(
    page_title="The BI Tool",
    layout="wide"
)

# Title of the Streamlit app
st.title("The BI Tool - Upload your Data")

# File upload section
uploaded_file = st.file_uploader("Upload your CSV or Excel file", type=["csv", "xlsx"])

if uploaded_file is not None:
    # Check if the uploaded file is CSV or Excel
    if uploaded_file.name.endswith(".csv"):
        df = pd.read_csv(uploaded_file)
    elif uploaded_file.name.endswith(".xlsx"):
        df = pd.read_excel(uploaded_file)

    # Render the Pygwalker app with the uploaded data
    pyg_app = StreamlitRenderer(df)
    pyg_app.explorer()
else:
    st.write("Please upload a CSV or Excel file to explore the data.")
