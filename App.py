import streamlit as st
from transformers import pipeline

#Load the summarization model
@st.cache_resource
def load_summarizer():
  return pipeline("summarization",model="sshleifer/distilbart-cnn-12-6")

summarizer = load_summarizer()

#Streamlit UI
st.title("AI Text Summarizer")
st.write("Enter a long text below,and get a concise summary!")

#Text Input
long_text = st.text_area("Enter text to summarize:", height=200)
