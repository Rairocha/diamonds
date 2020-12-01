import streamlit as st
import pandas as pd
import seaborn as sns

st.set_option('deprecation.showPyplotGlobalUse', False)

st.title('Site de Exploração de dados')

st.write('Isso é um site de exploração de dados')

in_file=st.file_uploader('Coloque aqui o seu arquivo csv')

try:
    df=pd.read_csv(in_file)
except:
    st.write('Por favor coloque um arquivo csv abestado')
else:
    if st.checkbox("Resumo DataFrame"):
        n_lines=int(st.number_input('Quantas linhas você quer ver?',min_value=1,max_value=len(df),step=1))
        if st.button("Head"):        
            st.write(df.head(n_lines))
        if st.button("Tail"):
            st.write(df.tail(n_lines))
    if st.checkbox('Linha especifica'):
        selected_column = st.multiselect('Quais colunas você quer',df.columns)
        number_line=int(st.number_input('Qual linha você quer ver?',min_value=1,max_value=len(df),step=1))
        st.write(df.loc[number_line,selected_column])
    if st.checkbox('Colunas'):
        st.write(df.columns)
    if st.checkbox('Describe'):
        st.write(df.describe())
    if st.checkbox('Grafico de correlação'):
        st.write(sns.heatmap(df.corr(),annot=True))
        st.pyplot()
