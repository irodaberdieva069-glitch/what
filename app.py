import streamlit as st

# Sahifa uslubini chiroyli qilish uchun
st.markdown("""
    <style>
    .big-font { font-size:24px !important; color: #FF4B4B; font-family: 'cursive'; }
    .msg-font { font-size:20px !important; font-family: 'serif'; text-align: center; }
    </style>
    """, unsafe_allow_html=True)

st.title("✨ Sirli sovg'a")

if 'authenticated' not in st.session_state:
    st.session_state.authenticated = False

if not st.session_state.authenticated:
    st.write("Bu eshik ortida faqat senga atalgan so‘zlar bor...")
    user_input = st.text_input("Maxfiy kodni kiriting:", type="password")
    
    if st.button("Ochish"):
        if user_input == "7777":
            st.session_state.authenticated = True
            st.rerun()
        else:
            st.error("Kod noto‘g‘ri, qayta urinib ko‘r...")
else:
    st.balloons()
    st.markdown('<p class="big-font">Salom...</p>', unsafe_allow_html=True)
    st.markdown('<p class="msg-font">Siz shunchalar go‘zalsizki, nigohim sizdan uzilmaydi. Bu so‘zlar shunchaki e’tirof emas, qalbimning tubidan chiqqan samimiy tuyg‘ularimdir. Sizni chin dildan yaxshi ko‘rib qoldim. ❤️</p>', unsafe_allow_html=True)
