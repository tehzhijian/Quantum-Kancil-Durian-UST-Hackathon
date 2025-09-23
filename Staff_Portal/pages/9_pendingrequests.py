import streamlit as st
import pandas as pd
import random
from faker import Faker
st.session_state.nric = "900101011234"
st.session_state.last_name = "Doe"
st.session_state.first_name = "John"
st.session_state.phone_number = "012-3456789"
st.session_state.staff_id = "S123456"
st.session_state.username = "Doe, John"

# --- PAGE CONFIG ---
st.set_page_config(page_title="Pending Requests", layout="wide")

# --- CUSTOM CSS ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');
    @import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css');

    body, h1, h2, h3, h4, h5, h6, div {
        font-family: 'Poppins', sans-serif !important;
    }

    .stApp, body {
        background-color: white !important;
        color: black;
    }

    .activity-table {
        width: 100%;
        border-collapse: collapse;
        table-layout: fixed;
    }
    .activity-table th, .activity-table td {
        border: 1px solid #ccc;
        padding: 0.8em;
        text-align: left;
        word-wrap: break-word;
    }
    .activity-table th {
        background-color: #0C1E33;
        color: white;
        text-align: center;
    }
    .activity-table td {
        background-color: white;
    }
    .activity-table i {
        font-size:1.2em;
        cursor:pointer;
    }

    /* Review cell style */
    .review-cell {
        background-color: #f3f4f6; /* light grey */
        color: black;
        padding: 4px 8px;
        border-radius: 6px;
        font-weight: 400;
        display: inline-block;
        text-align: center;
        cursor: pointer;
    }
            
    /* Center align the last column (Details) */
    .activity-table td:last-child {
        text-align: center;
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
        <h3 style="margin:0;">Requests Pending Your Approval</h3>
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

# --- DATA GENERATION ---
fake = Faker()
departments = ["Cardiology", "Neurology", "Oncology", "Pediatrics", "Orthopedics", "Other"]
doc_types = ["Medical Report", "Lab Test", "Prescription", "Other"]
doc_names = [
    "MRI Brain Scan", "Electrocardiogram Report", "Chest X-Ray", "Ultrasound Abdomen",
    "CBC Test", "Glucose Test", "Lipid Profile", "Prescription for Antibiotics",
    "Health Summary", "Referral Letter"
]

def generate_pending_requests(num=6):
    rows = []
    for _ in range(num):
        # Generate NRIC in format ######-##-####
        nric = f"{random.randint(100000,999999)}-{random.randint(10,99)}-{random.randint(1000,9999)}"

        # Last column: Review text with light grey background
        review_text = '<span class="review-cell">Review</span>'
        
        rows.append({
            "First Name": fake.first_name(),
            "Last Name": fake.last_name(),
            "NRIC": nric,
            "Gender": random.choice(["Male", "Female"]),
            "Document Name": random.choice(doc_names),
            "Document Type": random.choice(doc_types),
            "From": fake.name(),
            "Department": random.choice(departments),
            "Details": review_text
        })
    return pd.DataFrame(rows)

# --- PAGE DESCRIPTION ---
st.markdown("These are document requests submitted by other departments that require your review and approval.")
st.markdown("---")
st.markdown('<div style="margin-top:3%;"></div>', unsafe_allow_html=True)

# --- TABLE ---
df_pending_requests = generate_pending_requests(6)
st.write(df_pending_requests.to_html(escape=False, index=False, classes="activity-table"), unsafe_allow_html=True)
# st.write(st.session_state.username1)
if st.button("🏠 Go to Home Page"):
    st.switch_page("pages/2_staffhomepage.py")