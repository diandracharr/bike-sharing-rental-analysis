import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency

# Set style seaborn
sns.set(style='dark')

# Load dataset
day_df = pd.read_csv("https://raw.githubusercontent.com/diandracharr/bike-sharing-rental-analysis/main/dashboard/cleaned_bike_share.csv")
day_df.head()

# Menyiapkan daily_rent_df
def create_daily_rent_df(df):
    daily_rent_df = df.groupby(by='dateday').agg({
        'count': 'sum'
    }).reset_index()
    return daily_rent_df

# Menyiapkan daily_casual_rent_df
def create_daily_casual_rent_df(df):
    daily_casual_rent_df = df.groupby(by='dateday').agg({
        'casual': 'sum'
    }).reset_index()
    return daily_casual_rent_df

# Menyiapkan daily_registered_rent_df
def create_daily_registered_rent_df(df):
    daily_registered_rent_df = df.groupby(by='dateday').agg({
        'registered': 'sum'
    }).reset_index()
    return daily_registered_rent_df
    
# Menyiapkan season_rent_df
def create_season_rent_df(df):
    season_rent_df = df.groupby(by='season')[['registered', 'casual']].sum().reset_index()
    return season_rent_df

# Menyiapkan monthly_rent_df
def create_monthly_rent_df(df):
    monthly_rent_df = df.groupby(by='month').agg({
        'count': 'sum'
    })
    ordered_months = [
        'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
        'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'
    ]
    monthly_rent_df = monthly_rent_df.reindex(ordered_months, fill_value=0)
    return monthly_rent_df

# Menyiapkan weekday_rent_df
def create_weekday_rent_df(df):
    weekday_rent_df = df.groupby(by='weekday').agg({
        'count': 'sum'
    }).reset_index()
    return weekday_rent_df

# Menyiapkan workingday_rent_df
def create_workingday_rent_df(df):
    workingday_rent_df = df.groupby(by='workingday').agg({
        'count': 'sum'
    }).reset_index()
    return workingday_rent_df

# Menyiapkan holiday_rent_df
def create_holiday_rent_df(df):
    holiday_rent_df = df.groupby(by='holiday').agg({
        'count': 'sum'
    }).reset_index()
    return holiday_rent_df

# Menyiapkan weather_rent_df
def create_weather_rent_df(df):
    weather_rent_df = df.groupby(by='weathercond').agg({
        'count': 'sum'
    })
    return weather_rent_df

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

    st.write("#### Nama: Diandra Charisa Yefiananda \n #### Email: diandra.charisa@student.ub.ac.id \n #### ID Dicoding: diandracharisa")

    main_df = day_df[(day_df['dateday'] >= str(start_date)) & 
                (day_df['dateday'] <= str(end_date))]

# Menyiapkan berbagai dataframe
daily_rent_df = create_daily_rent_df(main_df)
daily_casual_rent_df = create_daily_casual_rent_df(main_df)
daily_registered_rent_df = create_daily_registered_rent_df(main_df)
season_rent_df = create_season_rent_df(main_df)
monthly_rent_df = create_monthly_rent_df(main_df)
weekday_rent_df = create_weekday_rent_df(main_df)
workingday_rent_df = create_workingday_rent_df(main_df)
holiday_rent_df = create_holiday_rent_df(main_df)
weather_rent_df = create_weather_rent_df(main_df)

# Melengkapi judul dashboard
st.header(':bar_chart: Bike Shared Rental Dashboard')

# Membuat jumlah penyewaan harian
# st.subheader('Daily Rentals')
col1, col2, col3 = st.columns(3)

with col1:
    daily_rent_casual = daily_casual_rent_df['casual'].sum()
    st.metric('Casual User', value= daily_rent_casual)

with col2:
    daily_rent_registered = daily_registered_rent_df['registered'].sum()
    st.metric('Registered User', value= daily_rent_registered)
 
with col3:
    daily_rent_total = daily_rent_df['count'].sum()
    st.metric('Total User', value= daily_rent_total)

# Membuah jumlah peminjaman berdasarkan kondisi cuaca
st.subheader('Weatherly Rentals')

fig, ax = plt.subplots(figsize=(16, 8))

colors=["tab:red", "tab:green", "tab:blue"]

sns.barplot(
    x=weather_rent_df.index,
    y=weather_rent_df['count'],
    palette=colors,
    ax=ax
)

for index, row in enumerate(weather_rent_df['count']):
    ax.text(index, row + 1, str(row), ha='center', va='bottom', fontsize=12)

ax.set_xlabel(None)
ax.set_ylabel(None)
ax.tick_params(axis='x', labelsize=20)
ax.tick_params(axis='y', labelsize=15)
st.pyplot(fig)

# Tulisan
st.write("Berdasarkan diagram diatas dapat disimpulkan terdapat hubungan antara jumlah peminjam dan kondisi cuaca. Peminjam sepeda tampaknya lebih menyukai cuaca yang cerah atau sedikit mendung, dengan jumlah melebihi 2 juta peminjam. Pentingnya variabel cuaca dalam menentukan tingkat penyewaan sepeda menandakan perlunya strategi yang responsif terhadap prakiraan cuaca.")

# Membuat jumlah penyewaan berdasarkan weekday, working dan holiday
st.subheader('Weekday, Workingday, and Holiday Rentals')

fig, axes = plt.subplots(nrows=3, ncols=1, figsize=(15,10))

colors1=["tab:blue", "tab:orange"]
colors2=["tab:blue", "tab:orange"]
colors3=["tab:blue", "tab:orange", "tab:green", "tab:red", "tab:purple", "tab:brown", "tab:pink"]

# Berdasarkan workingday
sns.barplot(
    x='workingday',
    y='count',
    data=workingday_rent_df,
    palette=colors1,
    ax=axes[0])

for index, row in enumerate(workingday_rent_df['count']):
    axes[0].text(index, row + 1, str(row), ha='center', va='bottom', fontsize=12)

axes[0].set_title('Number of Rents based on Working Day')
axes[0].set_ylabel(None)
axes[0].tick_params(axis='x', labelsize=15)
axes[0].tick_params(axis='y', labelsize=10)

# Berdasarkan holiday
sns.barplot(
  x='holiday',
  y='count',
  data=holiday_rent_df,
  palette=colors2,
  ax=axes[1])

for index, row in enumerate(holiday_rent_df['count']):
    axes[1].text(index, row + 1, str(row), ha='center', va='bottom', fontsize=12)

axes[1].set_title('Number of Rents based on Holiday')
axes[1].set_ylabel(None)
axes[1].tick_params(axis='x', labelsize=15)
axes[1].tick_params(axis='y', labelsize=10)

# Berdasarkan weekday
sns.barplot(
  x='weekday',
  y='count',
  data=weekday_rent_df,
  palette=colors3,
  ax=axes[2])

for index, row in enumerate(weekday_rent_df['count']):
    axes[2].text(index, row + 1, str(row), ha='center', va='bottom', fontsize=12)

axes[2].set_title('Number of Rents based on Weekday')
axes[2].set_ylabel(None)
axes[2].tick_params(axis='x', labelsize=15)
axes[2].tick_params(axis='y', labelsize=10)

plt.tight_layout()
st.pyplot(fig)

st.write("Berdasarkan diagram diatas dapat disimpulkan jumlah peminjam sepeda pada hari kerja (working day) lebih unggul daripada hari libur (holiday) dengan jumlah melebihi 3 juta peminjam. Meskipun selisih yang terlihat tidak terlalu signifikan, tetap terdapat perbedaan yang jelas.")