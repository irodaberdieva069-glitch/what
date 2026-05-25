import streamlit as st

# Sahifa uslubini chiroyli qilish
st.markdown("""
    <style>
    .title-style { font-size: 32px; color: #FF4B4B; text-align: center; font-family: 'Georgia', serif; }
    .text-style { font-size: 20px; font-family: 'Georgia', serif; line-height: 1.8; color: #333; text-align: justify; }
    </style>
    """, unsafe_allow_html=True)

# Kodni saqlash uchun state
if 'authenticated' not in st.session_state:
    st.session_state.authenticated = False

if not st.session_state.authenticated:
    st.title("✨ Maxfiy sahifa")
    user_input = st.text_input("Kod kiritish:", type="password")
    
    if st.button("Ochish"):
        if user_input == "7777":
            st.session_state.authenticated = True
            st.rerun()
        else:
            st.error("Kod noto‘g‘ri!")
else:
    st.balloons()
    st.markdown('<p class="title-style">Qalbimdan bir parcha...</p>', unsafe_allow_html=True)
    st.markdown("""
    <p class="text-style">
    Har bir insonning hayotida shunday nomlar borki, ular shunchaki so‘z emas, balki qalbga iliqlik bag‘ishlaydigan xotiralardir. <b>Madina</b> – bu ismning o‘zida qandaydir yorug‘lik va poklik bor. U bilan suhbatlashganda dunyo tashvishlari bir zumga chekinib, barcha narsa o‘z o‘rniga tushgandek tuyuladi.<br><br>
    Inson ba’zida o‘zining ichki dunyosini, orzu-maqsadlarini tushunadigan, har doim qo‘llab-quvvatlaydigan va ishonch bilan qaraydigan do‘stga ehtiyoj sezadi. Madina esa ana shunday qalbi go‘zal, har bir so‘zida haqiqat va samimiyatni jo etgan insonlardan. U bilan birga har bir daqiqa, har bir kichik suhbat ham qadrli. Hayotda bunday insonlar bilan yo‘l kesishishi – chinakam omad. ❤️
    </p>
    """, unsafe_allow_html=True)
