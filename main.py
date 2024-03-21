from datetime import datetime, timedelta

import pandas as pd
import streamlit as st
from mitosheet.streamlit.v1 import spreadsheet
from mitosheet.streamlit.v1.spreadsheet import _get_mito_backend

st.set_page_config(layout="wide")
with st.sidebar:
    st.title("Mito AI on Streamlit")
    st.subheader("")
    st.subheader("Based on Mito-for-Streamlit Examples")
    st.subheader("")
    "[Back to AIvigorate.ai](http://www.aivigorate.ai/)"


#st.header("AIvigorate")
st.header("Mito AI-powered Spreadsheet")
#uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])

st.markdown("""

Provide a direct download link to a .csv file hosted on a data storage platform (e.g. Google Drive, Dropbox) and work on your data using AI-powered spreadsheet by Mito AI implemented on Streamlit.

Mito AI will automatically generate the python code for whatever operations your instruct AI to perform.

""")

def get_data():
    filepath = st.text_input('Enter your csv file path')
    if filepath:
        try:
            df = pd.read_csv(filepath)
            return df
        except FileNotFoundError:
            st.error(f"File '{filepath}' not found.")
    return None

#def get_data():
 #   filepath = st.text_input('Enter your csv file path')
    #csv_url = 'https://drive.google.com/uc?export=download&id=1J_Qa5gpgq0qlT8lg37XDOKp6RJQJZ647'
  #  df = pd.read_csv(filepath)
    
    #df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/tesla-stock-price.csv')
    #df = df.drop(0)
    #df['volume'] = df['volume'].astype(float)
   # return df

test_data = get_data()

new_dfs, code = spreadsheet(test_data)
code = code if code else "# Edit the spreadsheet above to generate code"
st.code(code)


