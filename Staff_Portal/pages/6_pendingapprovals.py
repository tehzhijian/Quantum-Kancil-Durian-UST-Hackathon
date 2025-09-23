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
st.set_page_config(page_title="Documents Dashboard", layout="wide")

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
        font-size:1em;
        cursor:pointer;
    }
    
    .activity-table td:last-child {
        text-align: center;
    }

    /* Status styles with lighter backgrounds */
    .status-wait-patient {
        background-color: #fef9c3; /* lighter amber */
        color: black;
        padding: 1%;
        border-radius: 6px;
        display: inline-block;
        margin: 5%;
        text-align: center;
    }
    .status-wait-doctor {
        background-color: #dbeafe; /* lighter blue */
        color: black;
        padding: 1%;
        border-radius: 6px;
        display: inline-block;
        margin: 5%;
        text-align: center;
    }
    .status-rejected {
        background-color: #fee2e2; /* lighter red */
        color: black;
        padding: 8%;
        border-radius: 6px;
        display: inline-block;
        margin: 5%;
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
        <h3 style="margin:0;">Your Submitted Requests</h3>
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

st.markdown("Track the status of your pending requests and view all approved requests in the tables below.")

st.markdown("---")

# --- DATA GENERATION ---
fake = Faker()
departments = ["Cardiology", "Neurology", "Oncology", "Pediatrics", "Orthopedics", "Other"]
doc_types = ["Medical Report", "Lab Test", "Prescription", "Other"]
doc_names = [
    "MRI Brain Scan", "Electrocardiogram Report", "Chest X-Ray", "Ultrasound Abdomen",
    "CBC Test", "Glucose Test", "Lipid Profile", "Prescription for Antibiotics",
    "Health Summary", "Referral Letter"
]
statuses = ["Waiting Patient Consent", "Waiting Doctor's Consent"]

def generate_pending(num=5):
    rows = []
    for _ in range(num):
        status = random.choice(statuses)
        if status == "Waiting Patient Consent":
            status_html = '<span class="status-wait-patient">Waiting Patient Consent</span>'
        elif status == "Waiting Doctor's Consent":
            status_html = '<span class="status-wait-doctor">Waiting Doctor\'s Consent</span>'
        else:
            status_html = '<span class="status-rejected">Rejected</span>'

        # Generate NRIC in format ######-##-####
        nric = f"{random.randint(100000,999999)}-{random.randint(10,99)}-{random.randint(1000,9999)}"

        rows.append({
            "First Name": fake.first_name(),
            "Last Name": fake.last_name(),
            "NRIC": nric,
            "Gender": random.choice(["Male", "Female"]),
            "Document Name": random.choice(doc_names),
            "Document Type": random.choice(doc_types),
            "From": fake.name(),
            "Department": random.choice(departments),
            "Status": status_html
        })
    return pd.DataFrame(rows)


def generate_approved(num=5):
    rows = []
    for _ in range(num):
        # Generate NRIC in format ######-##-####
        nric = f"{random.randint(100000,999999)}-{random.randint(10,99)}-{random.randint(1000,9999)}"

        details_link = f'<a href="/retrieveprogress_page" target="_self"><i class="fa fa-eye" style="color:#0C1E33;"></i></a>'
        # details_link = f'<a><i class="fa fa-eye" style="color:#0C1E33;"></i></a>'
        rows.append({
            "First Name": fake.first_name(),
            "Last Name": fake.last_name(),
            "NRIC": nric,
            "Gender": random.choice(["Male", "Female"]),
            "Document Name": random.choice(doc_names),
            "Document Type": random.choice(doc_types),
            "From": fake.name(),
            "Department": random.choice(departments),
            "Details": details_link
        })
    return pd.DataFrame(rows)


# --- TABLES ---
st.markdown('<div style="margin-top:2%"></div>', unsafe_allow_html=True)

st.markdown('<h5 style="color:black;">Pending Approvals</h5>', unsafe_allow_html=True)

df_pending = generate_pending(4)
st.write(df_pending.to_html(escape=False, index=False, classes="activity-table"), unsafe_allow_html=True)

st.markdown('<div style="margin-top:4%"></div>', unsafe_allow_html=True)

st.markdown('<h5 style="color:black;">Approved Requests</h5>', unsafe_allow_html=True)

df_approved = generate_approved(3)
st.write(df_approved.to_html(escape=False, index=False, classes="activity-table"), unsafe_allow_html=True)
# st.write(st.session_state.username)
# st.write(st.session_state.username1)
if st.button("🏠 Go to Home Page"):
    st.switch_page("pages/2_staffhomepage.py")