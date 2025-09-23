import streamlit as st
import pandas as pd
import random
from faker import Faker

# --- PAGE CONFIG ---
st.set_page_config(page_title="Consent Requests", layout="wide")

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
    .activity-table td:last-child {
        text-align: center;
    }

    .approve-btn {
        color: #065f46;
        font-size: 1.2em;
        cursor: pointer;
        text-decoration: none;
    }

    .approve-btn:hover {
        color: #10b981;
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
</style>
""", unsafe_allow_html=True)

# --- HEADER WITH ICON ---
st.markdown("""
    <div style="display:flex; justify-content:space-between; align-items:center;">
        <h3 style="margin:0;">Consent Requests</h3>
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

# --- PAGE DESCRIPTION ---
st.markdown(
    "These are requests from doctors asking for your medical reports. "
    "You can review each request and approve it by clicking the tick icon."
)
st.markdown("---")
st.markdown('<div style="margin-top:3%;"></div>', unsafe_allow_html=True)

# --- DATA GENERATION ---
fake = Faker()
departments = ["Cardiology", "Neurology", "Oncology", "Pediatrics", "Orthopedics", "General Medicine"]
doc_types = ["Medical Report", "Lab Test", "Prescription", "Imaging Report"]
doc_names = [
    "MRI Brain Scan", "Electrocardiogram Report", "Chest X-Ray", "Ultrasound Abdomen",
    "CBC Test", "Blood Glucose Test", "Lipid Profile", "Prescription for Antibiotics",
    "Health Summary"
]
reasons = [
    "To review previous diagnoses",
    "To check past lab results or imaging",
    "To coordinate care with other doctors",
    "To avoid duplicate tests",
    "For pre-surgical planning"
]


def generate_consent_requests(num=6):
    rows = []
    for i in range(num):
        approve_link = f'<a href="#" class="approve-btn" id="approve_{i}" title="Approve"><i class="fa fa-check"></i></a>'
        rows.append({
            "Document Name": random.choice(doc_names),
            "Document Type": random.choice(doc_types),
            "From Which Doctor": fake.name(),
            "Department": random.choice(departments),
            "Reason": random.choice(reasons),
            "Approved": approve_link
        })
    return pd.DataFrame(rows)

# --- TABLE ---
df_requests = generate_consent_requests(6)

st.write(df_requests.to_html(escape=False, index=False, classes="activity-table"), unsafe_allow_html=True)
if st.button("🏠 Go to Home Page"):
    st.switch_page("pages/4_patienthomepage.py")