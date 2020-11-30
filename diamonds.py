import streamlit as st
import pandas as pd
from sklearn.metrics import mean_squared_error
import numpy as np

st.image('data/rick_crew.jpeg',use_column_width =True)
in_file=st.file_uploader('Coloque aqui o seu arquivo csv')
correct_diamonds= pd.read_csv('data/rick_diamonds_gabarito.csv')
try:
    test_diamonds=pd.read_csv(in_file)
except:
    st.write('Por favor coloque um arquivo csv abestado')
else:
    t=test_diamonds[0:4000]
    c=correct_diamonds[0:4000]
    m=np.sqrt(mean_squared_error(c['price'], t['price_predicted']))
    st.write(f'Your mean squared error is {m}')
    if m <900:
        st.balloons()