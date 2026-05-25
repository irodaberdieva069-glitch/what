import streamlit as st

# CSS orqali chiroyli dizayn beramiz
st.markdown("""
    <style>
    .message-box {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
        padding: 25px;
        border-radius: 15px;
        border-left: 5px solid #4B8BBE;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        font-family: 'Arial', sans-serif;
    }
    .message-text {
        font-size: 18px;
        color: #333;
        line-height: 1.6;
    }
    .name-title {
        color: #4B8BBE;
        font-weight: bold;
        font-size: 24px;
        margin-bottom: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# Matnni chiqarish funksiyasi
def show_madina_message():
    st.markdown("""
    <div class="message-box">
        <div class="name-title">Madina</div>
        <p class="message-text">
            Har bir insonning hayotida shunday nomlar borki, ular shunchaki so‘z emas, 
            balki qalbga iliqlik bag‘ishlaydigan xotiralardir. 
            <br><br>
            Madina – bu ismning o‘zida qandaydir yorug‘lik va poklik bor. 
            U bilan suhbatlashganda dunyo tashvishlari bir zumga chekinib, 
            barcha narsa o‘z o‘rniga tushgandek tuyuladi.
        </p>
    </div>
    """, unsafe_allow_html=True)

# Sahifada ko'rsatish
show_madina_message()
