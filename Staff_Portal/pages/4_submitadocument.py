import streamlit as st
from datetime import date
import os

# --- PAGE CONFIG ---
st.set_page_config(page_title="Submit A Document", layout="wide")

# --- CUSTOM CSS ---
st.markdown("""
    <style>
    /* Load Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');

    /* Load FontAwesome */
    @import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css');

    /* Global font */
    body, h1, h2, h3, h4, h5, h6, div {
        font-family: 'Poppins', sans-serif !important;
        font-size: 1em;
        color: black;
    }

    /* Page background */
    .stApp, body {
        background-color: white !important;
    }

    /* Staff Details Card */
    .staff-card {
        display: flex;
        background: #F2F4F5;
        border-radius: 1em;
        padding: 2%;
        margin-bottom: 3%;
        width: 49%;
        align-items: center;
    }

    .staff-icon {
        flex: 0 0 30%;
        text-align: center;
    }

    .staff-icon i {
        font-size: 4em;
        color: #0C1E33;
    }

    .staff-info {
        padding-left: 2%;
    }

    /* Input fields and dropdowns */
    div[data-baseweb="input"],
    div[data-baseweb="textarea"],
    div[data-baseweb="select"],
    div[data-baseweb="datepicker"] {
        border: 0.1em solid grey !important;
        border-radius: 0.3em !important;
        padding: 0 !important;
        background-color: white !important;
        width: 90%;
        margin-bottom: 1%; /* adds spacing between input fields */
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
    
    /* Submit button spacing */
    div.stButton > button {
        margin-top: 30% !important; /* adds space above the submit button */
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
            
    </style>
""", unsafe_allow_html=True)

# --- HEADER WITH ICON ---
st.markdown("""
    <div style="display:flex; justify-content:space-between; align-items:center;">
        <h3 style="margin:0;">Submit A Document</h3>
        <div style="
            background-color: #f0f0f0; 
            border-radius: 50%; 
            width: 50px; 
            height: 50px; 
            display: flex; 
            align-items: center; 
            justify-content: center;">
            <i class="fa fa-file-alt" style="color:#0C1E33; font-size:1.5em;"></i>
        </div>
    </div>
""", unsafe_allow_html=True)

st.markdown("Please ensure the files are clear and in **PDF format only**.")

# # --- STAFF DETAILS SECTION ---
# st.markdown("""
# <div class="staff-card">
#     <div class="staff-icon">
#         <i class="fa fa-user-tie"></i>
#     </div>
#     <div class="staff-info">
#         <h4>Jane Smith</h4>
#         <div style="margin:0;">Staff ID: S123456</div>
#         <div style="margin:0;">Staff Name: Adam Blake</div>
#         <div style="margin:0;">Role: Doctor</div>
#         <div style="margin:0;">Department: Cardiology</div>
#         <div style="margin:0;">Hospital Name: Thompson Hospital</div>
#     </div>
# </div>
# """, unsafe_allow_html=True)

st.markdown("---")  # horizontal line

# --- PATIENT DETAILS FORM ---
st.subheader("Patient Details")

col1, col2 = st.columns(2)

with col1:
    patient_id = st.text_input("NRIC / Passport Number", value="900101011234")
    patient_last = st.text_input("Patient Last Name", value="Quantum")
    patient_first = st.text_input("Patient First Name", value="Kancil Durian")
    gender = st.radio("Gender", ["Male", "Female", "Other"], index=0)
    document_type = st.selectbox("Document Type", ["Medical Report", "Lab Test", "Prescription", "Other"], index=0)
    

with col2:
    document_title = st.text_input("Document Title", value="Annual Health Check Report")
    department = st.selectbox("Department", ["Cardiology", "Neurology", "Oncology", "Pediatrics", "Other"], index=0)
    document_date = st.date_input("Date of Document / Test", value=date.today())
    notes = st.text_area("Notes / Description", value="Patient is in good health.", height=190)



st.markdown("<div style='margin-top: 3%;'></div>", unsafe_allow_html=True)

# --- FILE UPLOAD ---
col1, col2 = st.columns([0.45, 0.55])

with col1:
    uploaded_file = st.file_uploader("Upload Document (PDF only)", type=["pdf"])
    
# --- SUBMIT BUTTON ---
if st.button("Submit"):
    if uploaded_file is not None:
        # Dynamic filename
        file_name = f"{document_title}_{patient_id}.pdf"
        
        # Save in the same folder as this script
        with open(file_name, "wb") as f:
            f.write(uploaded_file.getbuffer())
        
        st.success(f"File saved as {file_name}")
    if uploaded_file:
        st.success("Document submitted successfully!")
        st.info(f"Patient: {patient_first} {patient_last} | Uploaded file: {uploaded_file.name}")
        st.session_state.patient_first = patient_first
        st.session_state.patient_last = patient_last
        st.session_state.uploaded_filename = uploaded_file.name
        st.session_state.tem_nric = patient_id
        st.session_state.tem_name = patient_last + ', ' + patient_first
        st.session_state.tem_document = document_type
        st.session_state.tem_doc_title = document_title
        st.session_state.tem_department = department
        st.session_state.tem_data_submitted = document_date
        st.session_state.tem_notes = notes

        st.switch_page("pages/5_progresspage.py")
    else:
        st.error("Please upload a PDF document before submitting.")

if st.button("🏠 Go to Home Page"):
    st.switch_page("pages/2_staffhomepage.py")