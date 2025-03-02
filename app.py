import streamlit as st
from PIL import Image
import streamlit as st


st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+Thai:wght@300;400;600&display=swap');

    html, body, input, button, select, div {
        font-family: 'Noto Sans Thai', sans-serif !important;
    }

    /* โลโก้ตรงกลาง */
    .logo-container {
        display: flex;
        justify-content: center;
        align-items: center;
        margin-top: -10px;
    }

    .logo {
        width: 100px;
        max-width: 100%;
    }

    /* ข้อความหลัก "ไปไหนดี" */
    .main-title {
        text-align: center;
        font-size: 36px;
        font-weight: bold;
        margin-top: -5px;
    }

    /* เมนูตัวเลือก */
    .menu-container {
        display: flex;
        justify-content: center;
        gap: 20px;
        margin-top: 10px;
    }

    .menu-item {
        display: flex;
        align-items: center;
        font-size: 18px;
        font-weight: 500;
        cursor: pointer;
        color: #333;
        padding-bottom: 5px;
    }

    .menu-item.active {
        font-weight: bold;
        border-bottom: 3px solid black;
    }

    /* ช่องค้นหา */
    .search-container {
        display: flex;
        align-items: center;
        background: white;
        padding: 12px;
        border-radius: 50px;
        box-shadow: 0 3px 6px rgba(0,0,0,0.1);
        max-width: 600px;
        width: 100%;
        margin: 20px auto;
        border: 1px solid #ddd;
    }

    .search-icon {
        margin-left: 10px;
        font-size: 20px;
        color: #777;
    }

    .search-input {
        flex: 1;
        background: transparent;
        border: none;
        outline: none;
        font-size: 18px;
        padding: 10px;
    }

    .search-button {
        background: #00af87;
        color: white;
        padding: 10px 24px;
        border-radius: 25px;
        border: none;
        cursor: pointer;
        font-size: 18px;
        font-weight: bold;
        box-shadow: 0px 2px 5px rgba(0, 0, 0, 0.2);
    }

    .search-button:hover {
        background: #008a6e;
    }

    </style>
    """,
    unsafe_allow_html=True
)

col1, col2, col3 = st.columns((1, 0.5, 1))
with col2:
    st.image(Image.open("logo.png"))

# 📌 เมนูตัวเลือก
st.markdown(
    """
    <div class="menu-container">
        <div class="menu-item active">🏠 ค้นหาทั้งหมด</div>
        <div class="menu-item">🛏️ โรงแรม</div>
        <div class="menu-item">📷 กิจกรรมน่าสนใจ</div>
        <div class="menu-item">🍽️ ร้านอาหาร</div>
        <div class="menu-item">✈️ เที่ยวบิน</div>
    </div>
    """,
    unsafe_allow_html=True
)

# 📌 ช่องค้นหา
st.markdown(
    """
    <div class="search-container">
        <span class="search-icon">🔍</span>
        <input type="text" class="search-input" placeholder="ที่เที่ยว กิจกรรมน่าสนใจ โรงแรม...">
        <button class="search-button">ค้นหา</button>
    </div>
    """,
    unsafe_allow_html=True
)
