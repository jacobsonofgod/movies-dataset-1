import altair as alt
import pandas as pd
import streamlit as st
from langchain_community.tools import DuckDuckGoSearchResults

prompt = st.chat_input("Say something")


if not prompt:
 st.title("👋 Welcome!")
 st.write("Type something in the chat below to search the web using DuckDuckGo.")
else:
    st.write(f"User has sent the following prompt: {prompt}")

search = DuckDuckGoSearchResults()

result= search.invoke(prompt)

st.write(result)
# Show the page title and description.
