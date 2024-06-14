import pandas as pd  
import matplotlib.pyplot as plt
import streamlit as st

st.set_page_config(("Dados da empresa 1")

page_title="Empresa 1", 
)

st.header("Dados da empresa 1")

arquivo = "https://github.com/TWTVtrG/Trabalho-14-06/blob/main/projetos.csv"
dfe = pd.read_csv(arquivo, sep=';') 
st.dataframe(dfe.head(3))

st.write("Gráfico de linha dos indicadores ao longo do tempo")

fig, ax = plt.subplots()
dfe.plot(ax=ax)
st.pyplot(fig)

fig, ax = plt.subplots()
dfe.plot(kind = 'scatter', x = 'EBITDA', y = 'Lucro operacional', ax=ax)
st.pyplot(fig)

fig, ax = plt.subplots()
dfe["Lucro do período"].plot(kind = 'hist', ax=ax)
st.pyplot(fig)


st.write(dfe.groupby('Ano').mean())

