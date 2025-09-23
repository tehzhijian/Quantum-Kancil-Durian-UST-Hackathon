import streamlit as st
st.session_state.phone_number = "012-3456789"

# --- PAGE CONFIG ---
st.set_page_config(page_title="OTP Verification", layout="wide")
# st.write(st.session_state.phone_number[:3])

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
        margin-top: 12% !important;
        padding: 0.6em 2em;
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
    .otp-input {
        width: 15%;
        height: 4em;
        text-align: center;
        font-size: 1.2em;
        border-radius: 0.5em;
        border: 1px solid #ccc;
        background-color: #f5f5f5;
        margin-bottom: 3%;
    }
    .otp-container {
        display: flex;
        justify-content: space-between;
        margin-bottom: 0.5em;
        padding:0em;
    }
    .otp-info {
        display: flex;
        justify-content: space-between;
        font-size: 0.85em;
        color: #555;
        margin-bottom: 1em;
    }

    </style>
""", unsafe_allow_html=True)

# --- CREATE 3 COLUMNS ---
col1, col2, col3 = st.columns([1, 1.5, 1])  # middle column wider
with col2:
    # --- CENTER ICON ---
    st.markdown('<div class="center-icon"><i class="fa fa-user"></i></div>', unsafe_allow_html=True)

    # --- PAGE TITLE ---
    st.markdown('<h4 style="text-align:center;">Complete Account Login</h4>', unsafe_allow_html=True)

    st.markdown('<div style="margin-top:2%;"></div>', unsafe_allow_html=True)

    # --- HALF WAY PROGRESS BAR WITH STEP TEXT ---
    st.markdown("""
    <div style="width: 100%;">
        <div style="text-align: right; font-size: 0.9em; color: #555; margin-bottom: 0.2em;">
            Step 2/2
        </div>
        <progress value="100" max="100" style="width:100%; height:1.2em;"></progress>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div style="margin-top:2%;"></div>', unsafe_allow_html=True)

    # --- PRIVACY INFO BOX ---
    st.markdown("""
    <div class="privacy-box">
        <i class="fa fa-lock"></i>
        <span>We take privacy issues seriously. You can be sure that your personal data is securely protected.</span>
    </div>
    """, unsafe_allow_html=True)

    # --- OTP INFO TEXT ---
    st.markdown(f'<p style="text-align:left;">Enter 6-Digit Code Sent To +{st.session_state.phone_number[:3] + '-XXX' + st.session_state.phone_number[-4:]}.</p>', unsafe_allow_html=True)

    # --- OTP INPUT BOXES ---
    st.markdown("""
    <div class="otp-container">
        <input class="otp-input" maxlength="1">
        <input class="otp-input" maxlength="1">
        <input class="otp-input" maxlength="1">
        <input class="otp-input" maxlength="1">
        <input class="otp-input" maxlength="1">
        <input class="otp-input" maxlength="1">
    </div>
    """, unsafe_allow_html=True)

    # --- OTP INFO / SEND AGAIN ---
    st.markdown("""
    <div class="otp-info">
        <div>Code Expires in 30s.</div>
        <div><a href="#" style="color:#0C1E33;">Send Again</a></div>
    </div>
    """, unsafe_allow_html=True)

    # --- VERIFY & CONTINUE BUTTON ---
    col1, col2, col3 = st.columns([1, 1.5, 1])
    with col2:
        if st.button("Verify & Continue"):
            st.success("✅ OTP Verified! You may proceed.")
            # Example: st.switch_page("next_page_name")  # Replace with your next page
            st.switch_page("pages/4_patienthomepage.py")
