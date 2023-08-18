from pathlib import Path
import streamlit as st
import sys
import os

filepath = os.path.join(Path(__file__).parents[1])
print(filepath)

sys.path.insert(0, filepath)

from to_mongo import ToMongo

c = ToMongo()
st.header('Family Size')
st.write('This page will search our database for the size of a family . Spelling currently must be exact.')

answer = st.text_input('Enter family size:', value = 'GT3')
st.write(list(c.student.find({'fam_size': answer})))