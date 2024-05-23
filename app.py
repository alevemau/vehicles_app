import pandas as pd
import plotly.express as px
import streamlit as st

vehicle_data = pd.read_csv('vehicles_us.csv')  # leer los datos

df = pd.DataFrame(vehicle_data)

st.title('Vehicle Sales app')

st.dataframe(df)

hist_button = st.button('Construir histograma')  # crear un botón

if hist_button:  # al hacer clic en el botón
    # escribir un mensaje
    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    # crear un histograma
    fig = px.histogram(vehicle_data, x="odometer")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

hist_button_d = st.checkbox(
    'Construir gráfico de dispersión')  # crear un botón

if hist_button_d:  # al hacer clic en el botón
    # escribir un mensaje
    st.write(
        'Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')

    # crear un histograma
    fig_d = px.scatter(vehicle_data, x='odometer', y='price', ylabel='price')

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig_d, use_container_width=True)

st.subheader('Condicion con base en el tipo')

fig_bar = px.bar(vehicle_data, color='type',
                 x='condition')
st.plotly_chart(fig_bar, use_container_width=True)

st.subheader('Condición vs Año del modelo')

fig_hist = px.histogram(vehicle_data, color='condition',
                        x='model_year')
st.plotly_chart(fig_hist, use_container_width=True)
