import streamlit as st
import base64

# --- PAGE CONFIG ---
st.set_page_config(page_title="Register As Staff", layout="wide")

# --- LOAD EXTERNAL CSS ---
with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

def get_base64_image(path):
    with open(path, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

img_base64 = get_base64_image("logo.png")

col1, col2, col3 = st.columns([0.05, 0.90, 0.05])
with col2:
    st.markdown(
        f"""
        <div style="text-align:center; margin-top:2%; margin-bottom:-5%;">
            <img src="data:image/png;base64,{img_base64}" width="150">
        </div>
        """,
        unsafe_allow_html=True
    )

# --- FIRST CONTAINER ---
st.markdown(
    """
    <div class="dark-container">
        <h2>Register As Staff</h2>
        Choose How You'd Like To Get Started
    </div>
    """, 
    unsafe_allow_html=True
)


# --- SECOND CONTAINER WITH 4 BOXES ---
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
        <div class="box">
            <div style="font-size:50px; color:#0C1E33;">
                <i class="fa-solid fa-user-doctor"></i>
            </div>
            <div class = "logintext"> Register As Doctor </div>
            <a class="black-button" href="/registerdoctor" target="_self">Get Started</a>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
        <div class="box">
            <div style="font-size:50px; color:#0C1E33;">
                <i class="fa-solid fa-user-nurse"></i>
            </div>
            <div class = "logintext"> Register As Nurse </div>
            <a class="black-button" href="#">Get Started</a>
        </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
        <div class="box">
            <div style="font-size:50px; color:#0C1E33;">
                <i class="fa-solid fa-prescription-bottle-medical"></i>
            </div>
            <div class = "logintext"> Register As Pharmacist </div>
            <a class="black-button" href="#">Get Started</a>
        </div>
    """, unsafe_allow_html=True)

