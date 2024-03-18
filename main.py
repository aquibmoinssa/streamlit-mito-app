from datetime import datetime, timedelta

import pandas as pd
import streamlit as st
from mitosheet.streamlit.v1 import spreadsheet
from mitosheet.streamlit.v1.spreadsheet import _get_mito_backend

with st.sidebar:
    
    "[View the source code](https://github.com/aquibmoinssa/streamlit-mito-app)"
    st.subheader("Based on Mito-for-Streamlit Examples")
    st.subheader("")
    st.subheader("Aquib Moin @ AIvigorate")
    st.subheader("")
    "[Back to AIvigorate.ai](http://www.aivigorate.ai/)"

#st.set_page_config(layout="wide")
st.header("AIvigorate")
st.subheader("Mito AI Implementation on Streamlit")
#uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])

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


