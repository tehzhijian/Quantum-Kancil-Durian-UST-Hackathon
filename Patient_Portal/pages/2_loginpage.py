import streamlit as st

# --- PAGE CONFIG ---
st.set_page_config(page_title="Complete Account Login", layout="wide")

# --- CUSTOM CSS ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');
    @import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css');

    body, h1, h2, h3, h4, h5, h6, div {
        font-family: 'Poppins', sans-serif !important;
        font-size: 1em;
        color: black;
    }
    .stApp, body {
        background-color: white !important;
    }
    div.stButton > button {
        margin-top: 1.5em !important;
        padding: 0.6em 4em;
        background-color: #0C1E33;
        color: white !important;
        border-radius: 0.5em;
        border: none;
        font-size: 1em;
        cursor: pointer;
        width: 150%;
    }
    div.stButton > button:hover {
        background-color: white;
        color: black !important;
        border: 0.1em solid grey !important;
    }
    .center-icon {
        display: flex;
        justify-content: center;
        align-items: center;
        font-size: 2em;
        color: #0C1E33;
        background-color: #f0f0f0;
        border-radius: 50%;
        width: 80px;
        height: 80px;
        margin: auto;
        margin-bottom:4%;
    }
    .privacy-box {
        background-color: #f9f9f9;
        border-radius: 0.5em;
        padding: 1em;
        display: flex;
        align-items: center;
        margin-bottom: 2em;
        font-size: 0.9em;
        color: #555;
    }
    .privacy-box i {
        margin-right: 1em;
        font-size: 1.5em;
        color: #0C1E33;
    }

    </style>
""", unsafe_allow_html=True)

# --- CREATE 3 COLUMNS ---
col1, col2, col3 = st.columns([1, 1.5, 1])  # middle column wider
with col2:  # center column
    # --- CENTER ICON ---
    st.markdown('<div class="center-icon"><i class="fa fa-user"></i></div>', unsafe_allow_html=True)

    # --- PAGE TITLE ---
    st.markdown('<h4 style="text-align:center;">Complete Account Login</h4>', unsafe_allow_html=True)

    st.markdown(
    '<div style="margin-top:2%;"></div>',
    unsafe_allow_html=True
    )

    # --- HALF WAY PROGRESS BAR WITH STEP TEXT ---
    st.markdown("""
    <div style="width: 100%;">
        <div style="text-align: right; font-size: 0.9em; color: #555; margin-bottom: 0.2em;">
            Step 1/2
        </div>
        <progress value="50" max="100" style="width:100%; height:1.2em;"></progress>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(
    '<div style="margin-top:2%;"></div>',
    unsafe_allow_html=True
    )

    # --- PRIVACY INFO BOX ---
    st.markdown("""
    <div class="privacy-box">
        <i class="fa fa-lock"></i>
        <span>We take privacy issues seriously. You can be sure that your personal data is securely protected.</span>
    </div>
    """, unsafe_allow_html=True)

    # --- LOGIN FORM ---
    email = st.text_input("Email Address", value="QuantumKancilDurian@Testing.com")
    password = st.text_input("Password", type="password", value="Password123")

    # --- FORGOT PASSWORD LINK ---
    st.markdown('<p style="text-align:right; font-size:0.8em;"><a href="#" style="color:#0C1E33;">Forgot your password?</a></p>', unsafe_allow_html=True)

    # --- LOGIN BUTTON CENTERED ---
    col1, col2, col3 = st.columns([1, 1.5, 1])  # Middle column twice as wide as side columns
    with col2:
        if st.button("Login"):
            if not email or not password:
                st.error("⚠️ Please enter your email and password.")
            else:
                st.session_state.email = email
                st.session_state.password = password
                st.success("✅ Login successful!")
                # Example: st.switch_page("next_page_name")  # Replace with your next page
                st.switch_page("pages/3_smsauthenticate.py")

