import streamlit as st

# --- PAGE CONFIG ---
st.set_page_config(page_title="Complete Account Setup As Doctor", layout="wide")

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
    .doctor-icon-circle {
        float: right;
        font-size: 2.5em;
        color: #0C1E33;
        background-color: #f0f0f0;
        border-radius: 50%;
        width: 60px;
        height: 60px;
        display: flex;
        align-items: center;
        justify-content: center;
    }
    
    i {
        font-size:0.8em;    }
            
    </style>
""", unsafe_allow_html=True)

# --- PAGE TITLE + ICON ---
st.markdown("""
<div style="display:flex; justify-content:space-between; align-items:center;">
    <h3>Complete Account Setup As Doctor</h3>
    <div class="doctor-icon-circle"><i class="fa fa-user-doctor"></i></div>
</div>
""", unsafe_allow_html=True)

st.markdown("Please fill in the relevant details.")

st.markdown("---")

# --- DOCTOR DETAILS FORM ---
st.markdown('<h5 style="color:black;">Doctor Information</h5>', unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    nric = st.text_input("NRIC", value="900101011234")
    last_name = st.text_input("Last Name", value="Doe")
    first_name = st.text_input("First Name", value="John")
    gender = st.radio("Gender", ["Male", "Female", "Other"], index=0)
    phone_number = st.text_input("Phone Number", value="012-3456789")
    email = st.text_input("Email Address", value="john.doe@example.com")
with col2:
    residential_address = st.text_area("Residential Address", value="123 Jalan Example, Kuala Lumpur", height=190)
    staff_id = st.text_input("Staff ID", value="S123456")
    mmc_number = st.text_input("Medical Council Registration Number (MMC)", value="MMC123456")
    specialization = st.selectbox("Specialization", ["Cardiology", "Neurology", "Oncology", "Pediatrics", "General Practitioner", "Other"], index=0)
    hospital_name = st.selectbox("Hospital Name", ["Thompson Hospital", "City Medical Centre", "National Hospital", "Other"], index=0)

st.markdown(
    '<div style="margin-top:5%;"></div>',
    unsafe_allow_html=True
)

# --- DOCUMENT UPLOADS ---
st.markdown('<h5 style="color:black;">Upload Required Documents</h5>', unsafe_allow_html=True)

col1, col2 = st.columns([0.45, 0.55])
with col1:
    uploaded_nric = st.file_uploader("Copy of NRIC", type=["pdf"])
    uploaded_degree = st.file_uploader("Medical Degree Certificate", type=["pdf"])
    uploaded_mmc = st.file_uploader("Malaysian Medical Council Annual Practicing Certificate", type=["pdf"])
    uploaded_license = st.file_uploader("Medical License", type=["pdf"])
    uploaded_photo = st.file_uploader("Recent Passport Size Photo", type=["pdf"])

st.markdown(
    '<div style="margin-top:5%;"></div>',
    unsafe_allow_html=True
)

# --- PASSWORD ---
st.markdown('<h5 style="color:black;">Set Your Password</h5>', unsafe_allow_html=True)

# Use a container with a single column taking 50% width
col1, col2 = st.columns([0.40, 0.60])  # left half for password, right half empty
with col1:
    password = st.text_input("Your Password", type="password", value="Password123")
    confirm_password = st.text_input("Confirm Your Password", type="password", value="Password123")

# --- TERMS & CONDITIONS ---
agree = st.checkbox("I agree to the Terms & Conditions")

# --- SUBMIT BUTTON ---
# if st.button("Submit"):
#     missing_files = [
#         name for name, file in [
#             ("NRIC", uploaded_nric),
#             ("Medical Degree Certificate", uploaded_degree),
#             ("MMC Certificate", uploaded_mmc),
#             ("Medical License", uploaded_license),
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
#         st.session_state.staff_id = staff_id
#         st.session_state.specialization = specialization
#         st.session_state.hospital_name = hospital_name
#         st.session_state.username = first_name + ", "+ last_name
#         st.session_state.phone_number = phone_number
#         # st.success("✅ Account setup submitted successfully!")
#         # st.info(
#         #     f"Doctor: {first_name} {last_name} | NRIC: {nric} | Staff ID: {staff_id} | "
#         #     f"Specialization: {specialization} | Hospital: {hospital_name}"
#         # )
#         st.switch_page("pages/99_loginpage.py")
#         # st.write(st.session_state.username)

# --- SUBMIT BUTTON ---
if st.button("Submit"):
    # Save info in session_state
    st.session_state.first_name = first_name
    st.session_state.last_name = last_name
    st.session_state.nric = nric
    st.session_state.staff_id = staff_id
    st.session_state.specialization = specialization
    st.session_state.hospital_name = hospital_name
    st.session_state.username = first_name + ", "+ last_name
    st.session_state.phone_number = phone_number
    st.switch_page("pages/99_loginpage.py")
