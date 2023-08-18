from pathlib import Path
import streamlit as st
import sys
import os

filepath = os.path.join(Path(__file__).parents[1])
print(filepath)

sys.path.insert(0, filepath)

from to_mongo import ToMongo

c = ToMongo()
st.header('School Page')
st.write('This page will search our database for any student from a given school you input. Spelling currently must be exact.')

answer = st.text_input('Enter a student school:', value = 'GP')
st.write(list(c.student.find({'school': answer})))