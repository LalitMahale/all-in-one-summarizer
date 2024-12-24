import streamlit as st


st.markdown("<h2 style = 'text align:center'>All in one Summarizer</h2>")

file = st.file_uploader("upload files")
if file != None:
    with open(file,'rb') as f:
        data = f.read()
    st.write(data)