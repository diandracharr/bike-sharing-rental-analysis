import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import plotly.express as px
import seaborn as sns
import streamlit as st

# Set style seaborn
sns.set(style='dark')

# Load dataset
day_df = pd.read_csv("https://raw.githubusercontent.com/diandracharr/bike-sharing-rental-analysis/main/dashboard/cleaned_bike_share.csv")
day_df.head()

# Membuat komponen filter
min_date = pd.to_datetime(day_df['dateday']).dt.date.min()
max_date = pd.to_datetime(day_df['dateday']).dt.date.max()

# Sidebar title
with st.sidebar:
    # Adding logo
    st.image("https://raw.githubusercontent.com/diandracharr/bike-sharing-rental-analysis/main/bike_logo.png")
    st.sidebar.header("Filter:")
    start_date, end_date = st.date_input(
        label='Date Filter',
        min_value= min_date,
        max_value= max_date,
        value=[min_date, max_date]
    )

    st.write(
        "#### Nama: Diandra Charisa Yefiananda \n  Email: diandra.charisa@student.ub.ac.id \n #### ID Dicoding: diandracharisa")

    main_df = day_df[(day_df['dateday'] >= str(start_date)) & 
                (day_df['dateday'] <= str(end_date))]
    
    # Melengkapi judul dashboard
st.header(':bar_chart: Bike Shared Rental Dashboard')

# Weatherly data
st.markdown(
    """
    # Weather Data
    Jumlah Peminjam Sepeda Berdasarkan Kondisi Cuaca
    """
)
weather_data = pd.DataFrame({
    'Weathercond': ['Clear/Few clouds', 'Light snow/Rain', 'Mist/Cloudy'],
    'Casual': [446346, 3895, 169776],
    'Registered': [1811606, 33974, 827082],
    'Count': [2257952, 37869, 996858]
})
st.write(weather_data)

# Grafik line
weather_data = {
    'weathercond': ['Clear/Few clouds', 'Light snow/Rain', 'Mist/Cloudy'],
    'casual': [446346, 3895, 169776],
    'registered': [1811606, 33974, 827082],
    'cnt': [2257952, 37869, 996858]
}
st.markdown(
    """
    Grafik Peminjam Sepeda Berdasarkan Kondisi Cuaca
    """
)
weather_sum = pd.DataFrame(weather_data)
weather_sum_melted = pd.melt(weather_sum, id_vars='weathercond', var_name='user_type', value_name='count')

fig = px.line(weather_sum_melted, x='weathercond', y='count', color='user_type', markers=True,
              labels={'count': 'Jumlah Peminjam', 'weathercond': 'Kondisi Cuaca'},
              title='Trend Peminjam Sepeda Berdasarkan Kondisi Cuaca')
fig.update_xaxes(type='category', tickmode='array', tickvals=weather_sum['weathercond'],
                 ticktext=['Clear/Few clouds', 'Light snow/Rain', 'Mist/Cloudy'])
st.plotly_chart(fig)

# Analisis
st.markdown(
    """
    ## Presentase Peminjaman Sepeda Berdasarkan Kondisi Cuaca
    """
)
weather_sum = day_df.groupby('weathercond').sum().reset_index()
weather_sum.index = ['Clear/Few clouds', 'Light snow/Rain', 'Mist/Cloudy']

total_rentals = weather_sum['count'].sum()
proportions = weather_sum['count'] / total_rentals * 100

colors = ['lightgreen', 'blue', 'orange']

fig = px.pie(weather_sum, values='count', names='weathercond', hole=0.3, color_discrete_sequence=colors)
fig.update_layout(title='Persentase Peminjaman Sepeda Berdasaarkan Kondisi Cuaca')

st.plotly_chart(fig)

st.markdown(
    """ 
    **Apakah kondisi cuaca mempengaruhi jumlah peminjaman sepeda?**\n
    Berdasarkan diagram diatas dapat disimpulkan hubungan antara keduanya jelas diamati. 
    Peminjam sepeda tampaknya memiliki preferensi tertentu terhadap kondisi cuaca terutama 
    menyukai cuaca yang cerah atau sedikit mendung dengan puncaknya yang mencapai 
    presentase 68.6% dengan jumlah peminjam lebih dari 2 juta orang.

    """
)

# Yearly data
st.markdown(
    """
    # Yearly Data
    Jumlah Peminjam Sepeda Berdasarkan Tahun
    """
)
yearly_trends = pd.DataFrame({
    'Yearly': ['2011', '2012'],
    'Count': [1243103, 2049576]
})
st.write(yearly_trends)

# Grafik bar
st.markdown(
    """
    Grafik Peminjaman Sepeda Berdasarkan Tahun
    """
)
yearly_trends = pd.DataFrame({
    'year': ['2011', '2012'],
    'count': [1243103, 2049576]
})
st.bar_chart(yearly_trends.set_index('year'))

# Analisis
st.markdown(
    """
    Presentase Peminjaman Sepeda Per Tahun
   """
)
yearly_trends = day_df.groupby('year')['count'].sum().reset_index()
total_rentals = yearly_trends['count'].sum()
proportions = yearly_trends['count'] / total_rentals

fig = px.pie(yearly_trends, values='count', names='year', hole=0.3, color_discrete_sequence=colors)
fig.update_layout(title='Trend Peminjaman Sepeda Per Tahun')

st.plotly_chart(fig)

st.markdown(
    """ 
    **Bagaimana perkembangan penggunaan sepeda dalam satu tahun, apakah tahun 2011 atau 2012 yang menonjol lebih baik?**\n
    Berdasarkan diagram di atas dapat disimpulkan antara tahun 2011 hingga 2012 (selama 1 tahun), terjadi peningkatan 
    jumlah peminjam sepeda. Peminjam tersebut sudah termasuk kategori peminjam casual dan registered. Oleh karena itu, 
    dari ilustrasi tersebut didapatkan informasi bahwa terjadi kenaikan sebanyak 62.2% peminjaman sepeda dalam kurun satu tahun. 
    Dengan peningkatan ini mencerminkan adanya trend positif dalam pertumbuhan bisnis peminjaman sepeda.
    """
)

st.caption('Copyright (c) Diandra 2024')