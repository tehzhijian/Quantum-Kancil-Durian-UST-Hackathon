import streamlit as st
import pandas as pd
import random
from faker import Faker
import hashlib

# --- PAGE CONFIG ---
st.set_page_config(page_title="Quantum Kancil Durian Dashboard", layout="wide")

# --- CUSTOM CSS (fonts, colors, buttons) ---
st.markdown("""
    <style>
    /* Load Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');

    /* Load FontAwesome */
    @import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css');

    /* Global font */
    body, h1, h2, h3, h4, h5, h6, div {
        font-family: 'Poppins', sans-serif !important;
    }

    /* Set full page background */
    .stApp, body {
        background-color: white !important;
        color: black;
    }

    /* Top Navigation Bar */
    .top-bar {
        display: flex;
        justify-content: space-between;
        align-items: center;
        border-radius: 1em;
        margin-bottom: 2%;
            
    }

    .search-bar input {
        padding: 5%;
        padding-left:15%;
        border: 1px solid #ccc;
        border-radius: 1em;
        width: 500%;
        font-size: 1em;
        background-color: lightgray;
        color: black !important;
        
    }

    .top-icons {
        font-size: 1.5em;
        margin-right:-2%;
        width: 10%;
    }
    .top-icons i {
        cursor: pointer;
        padding-left: 10%;
        margin-left:3%;
    }

    /* Stat Cards */
    .card {
        background: white;
        border-radius: 1em;
        padding: 5%;
        margin-bottom: 5%;
        width:100%;
        border:0.1em solid grey;
    }

    .card-content {
        display: flex;
        align-items: center;
    }

    .card-icon {
        flex: 0 0 20%; /* icon takes 30% width */
        text-align: center;
        margin-right:8%;
    }

    .card-icon i {
        font-size: 2.2em;
        color: #0C1E33;
    }

    .card-text {
        flex: 1;
        text-align: left;
    }

    .card-text h4 {
        margin: 0;
        font-weight: 500;
        font-size: 1.1em;
    }

    /* Streamlit table tweaks */
    .table-container table {
        border-collapse: collapse;
    }

    .activity-table {
        width: 100%;
        border-collapse: collapse;
        table-layout: fixed; /* evenly space columns */
    }

    .activity-table th, 
    .activity-table td {
        border-right: 1px solid #ccc; /* vertical dividers */
        border-left: 1px solid #ccc; /* vertical dividers */ 
        border-bottom: 1px solid #ccc; /* horizontal dividers */
        padding: 1em;
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
        
    }
            
    .activity-table td:last-child {
        text-align: center;      /* horizontal center */
        vertical-align: middle;  /* vertical center */
    }




""", unsafe_allow_html=True)

st.subheader("Welcome Back!")

# --- TOP NAV BAR ---
st.markdown("""
<div class="top-bar">
    <div class="search-bar">
        <input type="text" placeholder="Search">
    </div>
    <div class="top-icons">
        <i class="fa fa-bell"></i>
        <i class="fa fa-user-circle"></i>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("---")  # horizontal line

# --- SECOND CONTAINER WITH 4 BOXES ---
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(f"""
        <div class="card">
        <div class="card-content">
        <div class="card-icon">
            <i class="fa fa-calendar-check"></i>
        </div>
        <div class="card-text">
            <h4>Appointments</h4>
            42
        </div>
        </div>
        </div>
    """, unsafe_allow_html=True)

    st.markdown(f""" 
    <a href="/pendingapprovals" target="_self" style="text-decoration:none; color:inherit;">
        <div class="card">
            <div class="card-content">
                <div class="card-icon">
                    <i class="fa-solid fa-clock"></i>
                </div>
                <div class="card-text">
                    <h4>Pending Approvals</h4>
                    7
                </div>
            </div>
        </div>
    </a>
""", unsafe_allow_html=True)

with col2:
    st.markdown(f"""
        <div class="card">
        <div class="card-content">
        <div class="card-icon">
            <i class="fa fa-user-plus"></i>
        </div>
        <div class="card-text">
            <h4>New Patients</h4>
            15
        </div>
        </div>
        </div>
    """, unsafe_allow_html=True)

    st.markdown(f""" 
    <a href="/pendingapprovals" target="_self" style="text-decoration:none; color:inherit;">
    <div class="card">
    <div class="card-content">
    <div class="card-icon">
        <i class="fa fa-check-circle"></i>
    </div>
    <div class="card-text">
        <h4>Approved Requests</h4>
        5
    </div>
    </div>
    </div>
    </a>
""", unsafe_allow_html=True)

with col3:
    st.markdown(f"""
        <div class="card">
        <div class="card-content">
        <div class="card-icon">
            <i class="fa fa-heartbeat"></i>
        </div>
        <div class="card-text">
            <h4>Operations</h4>
            8
        </div>
        </div>
        </div>
    """, unsafe_allow_html=True)

    st.markdown(f"""
        <a href="/pendingrequests" target="_self" style="text-decoration:none; color:inherit;">
        <div class="card">
        <div class="card-content">
        <div class="card-icon">
            <i class="fa fa-file"></i>
        </div>
        <div class="card-text">
            <h4>Pending Requests</h4>
            12
        </div>
        </div>
        </div>
    """, unsafe_allow_html=True)

st.markdown("---")  # horizontal line

st.markdown("""
    <h4>Actions</h4>
""", unsafe_allow_html=True)

# --- Custom CSS for buttons ---
st.markdown("""
    <style>
    /* Target the button container */
    div.stButton {
        display: flex;
        justify-content: center;
        width: 150% !important;
    }

    /* Target the button itself */
    div.stButton > button:first-child {
        background-color: #0C1E33;  /* dark blue */
        color: white;
        border: none;
        padding: 5%;
        width: 100% !important;  /* full width inside the column */
        border-radius: 0.5em;
        font-weight: 500;
    }

    div.stButton > button:first-child:hover {
        background-color: white;
        color: black !important;
        border: 0.1em solid grey !important;
    }
    </style>
""", unsafe_allow_html=True)


col1, col2 = st.columns([2, 8])  # 3:7 ratio = 30% : 70%

with col1:
    if st.button("Submit A Document"):
        st.switch_page("pages/4_submitadocument.py")

with col2:
    if st.button("Request A Document"):
        st.switch_page("pages/8_requestadocument.py")


st.markdown("---")  # horizontal line

# --- APPOINTMENT ACTIVITY TABLE ---
st.markdown("""
    <h4>Appointment Activity</h4>
""", unsafe_allow_html=True)

# Generate random fake data
fake = Faker()
data = []
for _ in range(2):
    hour = random.randint(8, 16)
    period = "AM" if hour < 12 else "PM"
    display_hour = hour if hour <= 12 else hour - 12  # convert 13-16 to 1-4 PM
    data.append({
        "Name": fake.name(),
        "Email": fake.email(),
        "Date": fake.date_this_month(),
        "Visit Time": f"{display_hour}:00 {period}",
        # "Doctor": fake.name(),
        "Conditions": random.choice(["Flu", "Checkup", "Surgery", "Follow-up"]),
        "Delete": '<i class="fa fa-trash" style="color:red; cursor:pointer;"></i>'
    })

df = pd.DataFrame(data)

# Render dataframe with HTML (to keep delete icon)
st.write(df.to_html(escape=False, index=False, classes="activity-table"), unsafe_allow_html=True)

st.markdown("---")  # horizontal line

# --- SUBMITTED ---
st.markdown("""
    <h4>Submitted Document</h4>
""", unsafe_allow_html=True)

df = pd.read_csv("record.csv", dtype={'patient_id': str})

# Merge Last Name + First Name into a new column
df["Name"] = df["patient_last"] + ", " + df["patient_first"]

# Select the columns you want
subset = df[[
    "patient_id", "Name", "document_type", "document_title",
    "department", "date_of_document", "notes"
]].rename(
    columns={
        "patient_id": "NRIC",
        "Name": "Name",
        "document_type": "Document",
        "document_title": "Doc Title",
        "department": "Department",
        "date_of_document": "Date Submitted",
        "notes": "Notes"
    }
)
if "tem_nric" in st.session_state:
    new_row = {
        "NRIC": st.session_state.tem_nric,
        "Name": st.session_state.tem_name,
        "Document": st.session_state.tem_document,
        "Doc Title": st.session_state.tem_doc_title,
        "Department": st.session_state.tem_department,
        "Date Submitted": st.session_state.tem_data_submitted,
        "Notes": st.session_state.tem_notes
    }
    subset = pd.concat([pd.DataFrame([new_row]), subset], ignore_index=True)

    # ✅ remove the temp values so they won’t be added again
    del st.session_state["tem_nric"]
    del st.session_state["tem_name"]
    del st.session_state["tem_document"]
    del st.session_state["tem_doc_title"]
    del st.session_state["tem_department"]
    del st.session_state["tem_data_submitted"]
    del st.session_state["tem_notes"]

# Convert to HTML with custom classes
html_table = subset.to_html(
    escape=False,      # keep formatting if needed
    index=False,       # hide the index column
    classes="activity-table"  # apply your custom CSS class
)

# Render in Streamlit
st.write(html_table, unsafe_allow_html=True)
# st.write(st.session_state.username)
# st.session_state.username1 = st.session_state.username
# st.write(st.session_state.username1)
# st.write(st.session_state.username1)