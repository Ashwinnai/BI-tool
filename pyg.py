from pygwalker.api.streamlit import StreamlitRenderer
import pandas as pd
import streamlit as st

# Custom CSS for better UI/UX
def add_custom_css():
    st.markdown("""
    <style>
    /* Page background */
    body {
        background: linear-gradient(to right, #e0eafc, #cfdef3);
    }

    /* Title styling */
    .stTitle {
        font-size: 3em;
        color: #333;
        text-align: center;
        margin-bottom: 20px;
    }

    /* File upload button */
    .stFileUploader label {
        background-color: #4CAF50;
        color: white;
        padding: 10px 20px;
        border-radius: 8px;
        transition: background-color 0.3s ease;
    }
    .stFileUploader:hover label {
        background-color: #45a049;
    }

    /* Data Preview Table */
    .dataframe {
        margin-top: 20px;
        margin-bottom: 20px;
        border-radius: 8px;
        overflow: hidden;
        box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);
    }

    /* Pygwalker container */
    .pygwalker-container {
        padding-top: 40px;
    }
    </style>
    """, unsafe_allow_html=True)

# Adjust the width of the Streamlit page
st.set_page_config(page_title="The BI Tool", layout="wide")

# Add custom CSS
add_custom_css()

# Title of the Streamlit app
st.title("🚀 The BI Tool - Upload your Data")

# File upload section
uploaded_file = st.file_uploader("Upload your CSV or Excel file", type=["csv", "xlsx"])

if uploaded_file is not None:
    # Check if the uploaded file is CSV or Excel
    if uploaded_file.name.endswith(".csv"):
        df = pd.read_csv(uploaded_file)
    elif uploaded_file.name.endswith(".xlsx"):
        df = pd.read_excel(uploaded_file)

    # Data Preview Section
    st.subheader("🔍 Data Preview:")
    st.dataframe(df.head(10), height=200)  # Show the first 10 rows for preview

    # Render the Pygwalker app with the uploaded data
    st.subheader("📊 Data Explorer:")
    pyg_app = StreamlitRenderer(df)
    pyg_app.explorer()

else:
    st.write("⬆️ Please upload a CSV or Excel file to explore the data.")
