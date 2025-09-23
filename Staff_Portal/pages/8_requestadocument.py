import streamlit as st
from datetime import date
import time

# --- PAGE CONFIG ---
st.set_page_config(page_title="Request A Document", layout="wide")

# --- CUSTOM CSS ---
st.markdown("""
    <style>
    @import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css');

    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');
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
        margin-top: 0em !important;
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
        <h3 style="margin:0;">Submit A Request</h3>
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

st.markdown("Please ensure the information is correct before submitting.")

st.markdown("---")  # horizontal line

# --- PATIENT DETAILS ---
st.markdown('<h5 style="color:black;">Requesting Patient Details</h5>', unsafe_allow_html=True)


col1, col2 = st.columns(2)
with col1:
    patient_id = st.text_input("NRIC / Passport Number", value="900101011234")
    patient_last = st.text_input("Patient Last Name", value="Doe")
    
with col2:
    patient_first = st.text_input("Patient First Name", value="John")
    gender = st.radio("Gender", ["Male", "Female", "Other"], index=0)

# --- REQUESTING INFORMATION ---
st.markdown('<h5 style="color:black;">Requesting Information</h5>', unsafe_allow_html=True)

col3, col4 = st.columns(2)
with col3:
    department = st.selectbox("Department", ["Cardiology", "Neurology", "Oncology", "Pediatrics", "Other"], index=0)
    staff_name = st.text_input("Staff Name", value="Adam Blake")
    staff_id = st.text_input("Staff ID", value="S123456")
with col4:
    document_type = st.selectbox("Document Type", ["Medical Report", "Lab Test", "Prescription", "Other"], index=0)
    document_title = st.text_input("Document Title / Name", value="Annual Health Check Report")
    reason = st.text_area("Reason for Request", value="Requesting report for review.", height=100)

# # --- FILE UPLOAD ---
# st.markdown('<h5 style="color:black;">Upload Patient Consent Form</h5>', unsafe_allow_html=True)

# col1, col2 = st.columns([0.45, 0.55])  # left half for uploader, right half empty
# with col1:
#     uploaded_file = st.file_uploader("Upload Document (PDF only)", type=["pdf"])


# --- SUBMIT BUTTON ---
if st.button("Submit"):
    # st.success("✅ Request submitted successfully!")
    placeholder = st.empty()
    with placeholder.container():
        st.success("Upload successful! Redirecting...")
        progress = st.progress(0)
        for i in range(1, 101):
            time.sleep(0.01)
            progress.progress(i)

    time.sleep(0.5)
    st.switch_page("pages/6_pendingapprovals.py")
# if st.button("Submit"):
#     # Show dialog
#     dialog = st.dialog("Upload Successful!")  # no 'with'
#     dialog.success("✅ Request submitted successfully!")
#     dialog.write("Click below to go to Pending Approvals page.")
    
#     if dialog.button("Go to Pending Approvals"):
#         st.switch_page("pages/6_pendingapprovals.py")

# if st.button("Submit"):
#     if uploaded_file:
#         st.success("✅ Request submitted successfully!")
#         st.info(
#             f"Patient: {patient_first} {patient_last} | Staff: {staff_name} ({staff_id}) | "
#             f"Department: {department} | Document: {document_title} | File: {uploaded_file.name}"
#         )
#         # st.switch_page("pages/9_requestsubmitted.py")
#         st.success("🎉 Operation Completed Successfully!")
#         st.switch_page("pages/6_pendingapprovals.py")
#         # if st.button("🏠 Go to Home Page"):
#         #     st.switch_page("pages/2_staffhomepage.py")
#     else:
#         st.error("⚠️ Please upload a PDF document before submitting.")

if st.button("🏠 Go to Home Page"):
    st.switch_page("pages/2_staffhomepage.py")
