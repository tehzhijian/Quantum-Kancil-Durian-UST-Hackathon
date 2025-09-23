import streamlit as st

# --- PAGE CONFIG ---
st.set_page_config(page_title="Complete Account Setup As Patient", layout="wide")

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
    div[data-baseweb="input"],
    div[data-baseweb="textarea"],
    div[data-baseweb="select"],
    div[data-baseweb="datepicker"] {
        border: 0.1em solid grey !important;
        border-radius: 0.3em !important;
        padding: 0 !important;
        background-color: white !important;
        width: 90%;
        margin-bottom: 1%;
    }
    div[data-baseweb="input"] input,
    div[data-baseweb="textarea"] textarea,
    div[data-baseweb="select"] > div > div,
    div[data-baseweb="datepicker"] input {
        border: none !important;
        background-color: white !important;
        color: black !important;
        font-family: 'Poppins';
        padding: 0.5em !important;
    }
    div.stButton > button {
        margin-top: 2em !important;
        padding: 0.6em 1.2em;
        background-color: #0C1E33;
        color: white !important;
        border-radius: 0.5em;
        border: none;
        font-size: 1em;
        cursor: pointer;
    }
    div.stButton > button:hover {
        background-color: white;
        color: black !important;
        border: 0.1em solid grey !important;
    }
    .patient-icon-circle {
        float: right;
        font-size: 1.4em;
        color: #0C1E33;
        background-color: #f0f0f0;
        border-radius: 50%;
        width: 60px;
        height: 60px;
        display: flex;
        align-items: center;
        justify-content: center;
    }
    </style>
""", unsafe_allow_html=True)

# --- PAGE TITLE + ICON ---
st.markdown("""
<div style="display:flex; justify-content:space-between; align-items:center;">
    <h3>Complete Account Setup As Patient</h3>
    <div class="patient-icon-circle"><i class="fa-solid fa-hospital-user"></i></div>
</div>
""", unsafe_allow_html=True)

st.markdown("Please fill in the relevant details.")


st.markdown("---")

# --- PATIENT DETAILS FORM ---
st.markdown('<h5 style="color:black;">Patient Information</h5>', unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    nric = st.text_input("NRIC", value="900101011234")
    last_name = st.text_input("Last Name", value="Doe")
    first_name = st.text_input("First Name", value="Jane")
    gender = st.radio("Gender", ["Male", "Female", "Other"], index=1)
    phone_number = st.text_input("Phone Number", value="012-3456789")
    email = st.text_input("Email Address", value="jane.doe@example.com")
with col2:
    residential_address = st.text_area("Residential Address", value="123 Jalan Example, Kuala Lumpur", height=190)
    insurance_provider = st.selectbox("Insurance Provider", ["AIA", "Allianz", "Prudential", "Other"], index=0)
    insurance_number = st.text_input("Insurance/Policy Number", value="INS123456")
    hospital_name = st.selectbox("Hospital Name", ["Thompson Hospital", "City Medical Centre", "National Hospital", "Other"], index=0)

st.markdown('<div style="margin-top:5%;"></div>', unsafe_allow_html=True)

# --- DOCUMENT UPLOADS ---
st.markdown('<h5 style="color:black;">Upload Required Documents</h5>', unsafe_allow_html=True)

col1, col2 = st.columns([0.45, 0.55])
with col1:
    uploaded_nric = st.file_uploader("Copy of NRIC", type=["pdf"])
    uploaded_insurance = st.file_uploader("Insurance Card / Policy Document", type=["pdf"])
    uploaded_medical_records = st.file_uploader("Previous Medical Records (if any)", type=["pdf"])
    uploaded_photo = st.file_uploader("Recent Passport Size Photo", type=["pdf"])

st.markdown('<div style="margin-top:5%;"></div>', unsafe_allow_html=True)

# --- PASSWORD ---
st.markdown('<h5 style="color:black;">Set Your Password</h5>', unsafe_allow_html=True)

col1, col2 = st.columns([0.40, 0.60])
with col1:
    password = st.text_input("Your Password", type="password",value="Password123")
    confirm_password = st.text_input("Confirm Your Password", type="password",value="Password123")

# --- TERMS & CONDITIONS ---
agree = st.checkbox("I agree to the Terms & Conditions")

# --- SUBMIT BUTTON ---
if st.button("Submit"):
    st.session_state.first_name = first_name
    st.session_state.last_name = last_name
    st.session_state.nric = nric
    st.session_state.insurance_provider = insurance_provider
    st.session_state.insurance_number = insurance_number
    st.session_state.hospital_name = hospital_name
    st.session_state.phone_number = phone_number
    # Redirect to next page
    st.success("✅ Account setup completed! You can now proceed.")
    # Example: st.switch_page("next_page_name")  # Replace with your next page
    st.switch_page("pages/2_loginpage.py")

# # --- SUBMIT BUTTON ---
# if st.button("Submit"):
#     missing_files = [
#         name for name, file in [
#             ("NRIC", uploaded_nric),
#             ("Insurance Document", uploaded_insurance),
#             ("Passport Photo", uploaded_photo)
#         ] if not file
#     ]
    
#     if not agree:
#         st.error("⚠️ You must agree to the Terms & Conditions before submitting.")
#     elif missing_files:
#         st.error(f"⚠️ Please upload the following files: {', '.join(missing_files)}")
#     elif password != confirm_password:
#         st.error("⚠️ Password and Confirm Password do not match.")
#     else:
#         # Save info in session_state
#         st.session_state.first_name = first_name
#         st.session_state.last_name = last_name
#         st.session_state.nric = nric
#         st.session_state.insurance_provider = insurance_provider
#         st.session_state.insurance_number = insurance_number
#         st.session_state.hospital_name = hospital_name
#         st.session_state.phone_number = phone_number

#         # Redirect to next page
#         st.success("✅ Account setup completed! You can now proceed.")
#         # Example: st.switch_page("next_page_name")  # Replace with your next page
#         st.switch_page("pages/2_loginpage.py")
