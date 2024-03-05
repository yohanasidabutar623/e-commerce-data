import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency

# Set page title
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

st.caption('Copyright Yohana Sidabutar 2024')