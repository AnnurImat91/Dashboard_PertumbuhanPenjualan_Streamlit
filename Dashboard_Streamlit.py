import streamlit as st
from PIL import Image
import os

st.set_page_config(
    page_title="E-Commerce Data Analysis",
    page_icon="📊",
)

st.title("DASHBOARD E-COMMERCE KAMI YO BROO AWKWKWKWK")

path = os.path.dirname(__file__)
my_file = path+'/images/poto1.avif'
st.image(my_file, caption='E-Comerce Analysis Dashboard')

st.write("Dataset yang Kami gunakan adalah E-Commerce Public Dataset.")
st.write("Dataset ini mencakup informasi yang dikumpulkan dari transaksi e-commerce di Brazil dalam rentang waktu tertentu. Dataset tersebut terdiri dari beberapa file yang terkait satu sama lain dan memberikan wawasan yang komprehensif tentang e-commerce.")
st.write("Beberapa file utama dalam dataset ini termasuk:")
st.write("- Orders: File ini berisi informasi tentang pesanan, seperti ID pesanan, status pesanan, waktu pembelian, waktu persetujuan, dan waktu pengiriman pesanan.")
st.write("- Order Items: File ini berisi informasi terperinci tentang setiap item yang dibeli dalam pesanan, seperti ID produk, harga produk, jumlah yang dibeli, dan biaya pengiriman.")
st.write("- Products: File ini berisi informasi tentang produk, termasuk ID produk, kategori produk, dan nama produk.")
st.write("- Sellers: File ini berisi informasi tent ang penjual, seperti ID penjual, nama penjual, dan lokasi penjual (kota dan negara bagian).")
st.write("- Customers: File ini berisi informasi tentang pelanggan, seperti ID pelanggan, nama pelanggan, dan lokasi pelanggan (kota dan negara bagian).")
st.write("- Geolocation: File ini menyediakan informasi geografis tentang kota dan negara bagian di Brazil. Ini membantu dalam analisis berdasarkan lokasi geografis.")
st.write("Dataset ini memungkinkan analisis yang luas tentang berbagai aspek e-commerce. Kita dapat menganalisis tren penjualan berdasarkan waktu, kategori produk yang paling populer, preferensi pembelian pelanggan di berbagai wilayah, serta karakteristik dan lokasi penjual.")
st.write("Dengan memanfaatkan dataset ini, Kita dapat menghasilkan pemahaman yang lebih dalam tentang pasar e-commerce, memperoleh wawasan tentang perilaku pembelian, dan mengidentifikasi peluang atau tantangan di industri ini.")