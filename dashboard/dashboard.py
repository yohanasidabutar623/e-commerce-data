import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import streamlit as st
from babel.numbers import format_currency

# Judul
st.title("E-commerce Data Analysis Dashboard")

# Introduction
st.write("""
    Selamat datang di Data Analysis Dashboard! 
    Di sini, kami akan menjelaskan apa itu data analysis dan seberapa pentingnya dalam pengembangan e-commerce.
""")

st.header("Apa Itu Data Analysis?")
st.write("""
    Data analysis adalah proses menganalisis data untuk mendapatkan wawasan, mengidentifikasi tren, 
    dan mengambil keputusan berdasarkan informasi yang ditemukan. Dalam konteks e-commerce, data analysis
    membantu memahami perilaku pelanggan, meningkatkan efisiensi operasional, dan mengoptimalkan strategi pemasaran.
""")

st.header("Pentingnya Data Analysis dalam Pengembangan E-commerce")
st.write("""
    Data analysis memiliki peran krusial dalam pengembangan e-commerce. Berikut adalah beberapa alasan mengapa:
    - Memahami perilaku pelanggan untuk meningkatkan pengalaman belanja.
    - Mengidentifikasi produk atau layanan yang paling diminati.
    - Mengoptimalkan rantai pasokan dan manajemen inventaris.
    - Merancang strategi pemasaran berdasarkan tren dan preferensi pelanggan.
""")

st.header("Contoh Data Analysis: Kepuasan Pembeli")
st.write("""
    Sebagai contoh, kita dapat menganalisis data kepuasan pembeli untuk mendapatkan wawasan tentang layanan pelanggan,
    kualitas produk, dan faktor-faktor lain yang memengaruhi kepuasan pelanggan.
""")

st.image('ilustrasi.png', width=500)
st.write("""
Dari data dan grafik yang ada, terlihat bahwa mayoritas pembeli sangat puas dengan pelayanan yang ada. Namun penilaian tingkat kepuasan paling rendah mendapat review yang cukup banyak, hal ini dapat dievaluasi lebih lanjut untuk perbaikan ke depannya.
""")

df_customers = pd.read_csv('data/customers_dataset.csv')
df_customers = df_customers.rename(columns={'customer_zip_code_prefix':'zipcode'})
top_customer = df_customers['customer_city'].value_counts().head(5)

df_sellers = pd.read_csv('data/sellers_dataset.csv')
df_sellers = df_sellers.rename(columns={'seller_zip_code_prefix':'zipcode'})
top_seller = df_sellers['seller_city'].value_counts().head(5)

all_df = pd.read_csv('dashboard/all_df.csv')

st.subheader('Contoh lain')

st.write(""" Kita bisa melihat dan membaca daerah atau kota mana yang memiliki transaksi paling banyak dan paling sedikit. Hal ini membantu kita untuk membaca peluang bisnis.
""") 
grafik, (customer, seller) = plt.subplots(1, 2, figsize=(15, 8))

import matplotlib.pyplot as plt

# Ukuran grafik
ukuran_grafik = (10, 6)

# Visualisasi Lima Kota dengan Jumlah Pembeli Terbanyak
customer_colors = ['#FFD700' if city == top_customer.values[0] else '#87CEEB' for city in top_customer]
top_customer.plot(kind="bar", color=customer_colors, ax=customer, figsize=ukuran_grafik)
customer.set_title('Lima Kota dengan Pembeli Terbanyak')
customer.set_xlabel('Kota')
customer.set_ylabel('Frekuensi')
customer.set_xticklabels(customer.get_xticklabels(), rotation=0)

# Visualisasi Lima Kota dengan Jumlah Penjual Terbanyak
seller_colors = ['#FFD700' if city == top_seller.values[0] else '#ADD8E6' for city in top_seller]
top_seller.plot(kind="bar", color=seller_colors, ax=seller, figsize=ukuran_grafik)
seller.set_title('Lima Kota dengan Penjual Terbanyak')
seller.set_xlabel('Kota')
seller.set_ylabel('Frekuensi')
seller.set_xticklabels(seller.get_xticklabels(), rotation=0)

st.pyplot(grafik)


st.write(""" Kita dapat juga melihat hasil penjualan dalam kurun waktu tertentu
""")        
def create_daily_orders_df(df):
    daily_orders_df = df.resample(rule='D', on='order_purchase_timestamp').agg({
        "order_id": "nunique",
        "payment_value": "sum"
    })
    daily_orders_df = daily_orders_df.reset_index()
    daily_orders_df.rename(columns={
        "order_id": "order_count",
        "payment_value": "untung"
    }, inplace=True)
    
    return daily_orders_df

datetime_columns = ["order_purchase_timestamp", "order_estimated_delivery_date"]
all_df.sort_values(by="order_purchase_timestamp", inplace=True)
all_df.reset_index(inplace=True)

for column in datetime_columns:
    all_df[column] = pd.to_datetime(all_df[column])

min_date = all_df["order_purchase_timestamp"].min()
max_date = all_df["order_purchase_timestamp"].max()

with st.sidebar:
    # Mengambil start_date & end_date dari date_input
    start_date, end_date = st.date_input(
        label='Periode', min_value=min_date,
        max_value=max_date,
        value=[min_date, max_date]
    )

main_df = all_df[(all_df["order_purchase_timestamp"] >= str(start_date)) & 
                (all_df["order_purchase_timestamp"] <= str(end_date))]
daily_orders_df = create_daily_orders_df(main_df)

col1, col2 = st.columns(2)
with col1:
    total_orders = daily_orders_df.order_count.sum()
    st.metric("Jumlah pesanan", value=total_orders)

with col2:
    total_untung = format_currency(daily_orders_df.untung.sum(), "AUD", locale='es_CO') 
    st.metric("Keuntungan", value=total_untung)

fig, ax = plt.subplots(figsize=(16, 8))
ax.plot(
    daily_orders_df["order_purchase_timestamp"],
    daily_orders_df["order_count"],
    marker='o', 
    linewidth=2,
    color="#FF5733"  
)
ax.tick_params(axis='y', labelsize=20)
ax.tick_params(axis='x', labelsize=15)

st.pyplot(fig)




st.caption('Copyright Yohana Sidabutar 2024')
