import streamlit as st
import base64

st.set_page_config(layout="wide")

@st.cache_data
def display_pdf(file):
    # with open(file,"rb") as f:
    base64_pdf = base64.b64encode(file.read()).decode("utf-8")
    
    display = f"<iframe src='data:application/pdf;base64,{base64_pdf}' width = '100%' height = '600' type = 'application/pdf'></iframe>"

    st.markdown(display, unsafe_allow_html=True)


def main():
    st.title("All in 1 Document summarizer")

    file = st.file_uploader("Upload file",type=['pdf'])
    if file != None:
        if st.button("Summarize"):
            col1,col2 = st.columns(2)
            with col1:
                display_pdf(file)
            with col2:
                pass




main()
    