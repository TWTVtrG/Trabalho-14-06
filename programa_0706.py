import pandas as pd  
import matplotlib.pyplot as plt
import streamlit as st
import ipeadatapy as ip


st.set_page_config(
  page_title="Empresa 1", 
page_icon="👋",
)

st.header("Dados da empresa 1")

arquivo = "https://raw.githubusercontent.com/TWTVtrG/Trabalho-14-06/main/projetos.csv"
df = pd.read_csv(arquivo, sep=';') 
st.dataframe(df.head(23))

st.write("Gráfico de linha dos indicadores ao longo do tempo")

fig, ax = plt.subplots()
df.plot(ax=ax)
st.pyplot(fig)

fig, ax = plt.subplots()
df.plot(kind = 'scatter', x = 'Projeto1', y = 'Projeto2', ax=ax)
st.pyplot(fig)

fig, ax = plt.subplots()
df["Projeto1"].plot(kind = 'hist', ax=ax)
df["Projeto4"].plot(kind = 'hist', ax=ax)
st.pyplot(fig)

dados = ip.list_series('Selic')
dados
selic = ip.timeseries('BM12_TJOVER12', yearGreaterThan=2021, yearSmallerThan=2024)
selic
fig, ax = plt.subplots()
ip.timeseries('BM12_TJOVER12', year=2021).plot("MONTH", "VALUE ((% a.m.))", ax=ax)
ip.timeseries('BM12_TJOVER12', year=2022).plot("MONTH", "VALUE ((% a.m.))", ax=ax)
st.pyplot(fig)

