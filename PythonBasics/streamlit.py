''' Intro to Streamlit\n",
    "Open source app framework for ML and DS proects. 
    allows you to create beautiful web applications for your machine learning and data science projects 
    with simple python scripts"
'''

import streamlit as st
import pandas as pd
import numpy as np

st.title("Hello Streamlit")
'''
to run the streamlit app 
pass command streamlit run app.py 
'''
name = st.text_input("Enter name")
age = st.slider("Select your age",0,100,25)
if age:
    st.write(f"Your age is {age}")
if name: 
    st.write(f"Helloasdfasdf {name}" )
options=['Python','Java','C++','JavaScript']
choice = st.selectbox("Choose your favourite language:", options)
st.write(f"You selected {choice}.")
data = {
    "Name":["John","Jane","Jake","Jill"],
    "Age":[28,24,25,22],
    "City":["New york", "Los Angeles", "Chicago", "Houston"]
}
df = pd.DataFrame(data)
df.to_csv("Sampledata.csv")

uploadedfile = st.file_uploader("Choose a csv file", type='csv')
if uploadedfile is not None:
    df = pd.read_csv(uploadedfile)
    st.write(df)
## Display a simple text
st.write("This is a simple text")

## create a simple data frame
df = pd.DataFrame({
     'first column':[1,2,3,4],
     'second column':[10,20,30,40]
})

## display the data frame
st.write("Here is the data frame")
st.write(df)

## Create a line chart
chart_data = pd.DataFrame(
    np.random.randn(20,3), columns=['a','b','c']
)
st.write(chart_data)
st.line_chart(chart_data)