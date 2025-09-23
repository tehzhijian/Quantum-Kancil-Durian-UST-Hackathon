import streamlit as st
import random
from faker import Faker
import pandas as pd

# --- PAGE CONFIG ---
st.set_page_config(page_title="Patient Dashboard", layout="wide")

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

    /* Top Navigation Bar */
    .top-bar {
        display: flex;
        justify-content: space-between;
        align-items: center;
        border-radius: 1em;
        margin-bottom: 5%;
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
        flex: 0 0 20%;
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


    /* Table styles */
    .activity-table {
        width: 100%;
        border-collapse: collapse;
        table-layout: fixed;
    }
    .activity-table th, 
    .activity-table td {
        border-right: 1px solid #ccc;
        border-left: 1px solid #ccc;
        border-bottom: 1px solid #ccc;
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
        cursor:pointer;
    }
    .activity-table td:last-child {
        text-align: center;
        vertical-align: middle;
    }
</style>
""", unsafe_allow_html=True)

# --- TOP NAV BAR ---
st.markdown("""
<div class="top-bar">
    <div class="search-bar">
        <input type="text" placeholder="Search...">
    </div>
    <div class="top-icons">
        <i class="fa fa-bell"></i>
        <i class="fa fa-user-circle"></i>
    </div>
</div>
""", unsafe_allow_html=True)

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
            <h4>My Appointments</h4>
            3
        </div>
        </div>
        </div>
    """, unsafe_allow_html=True)

    st.markdown(f""" 
        <div class="card">
            <div class="card-content">
                <div class="card-icon">
                    <i class="fa fa-file-medical"></i>
                </div>
                <div class="card-text">
                    <h4>New Document</h4>
                    4
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
            <i class="fa fa-pills"></i>
        </div>
        <div class="card-text">
            <h4>Active Prescriptions</h4>
            5
        </div>
        </div>
        </div>
    """, unsafe_allow_html=True)

    st.markdown(f""" 
    <div class="card">
    <div class="card-content">
    <div class="card-icon">
        <i class="fa fa-credit-card"></i>
    </div>
    <div class="card-text">
        <h4>Outstanding Balance</h4>
        $350
    </div>
    </div>
    </div>
    </a>
""", unsafe_allow_html=True)

with col3:
    st.markdown(f"""
        <a href="/consentform" target="_self" style="text-decoration:none; color:inherit;">
        <div class="card">
        <div class="card-content">
        <div class="card-icon">
            <i class="fa fa-user-check"></i>
        </div>
        <div class="card-text">
            <h4>Consent Requests</h4>
            2
        </div>
        </div>
        </div>
    """, unsafe_allow_html=True)

    st.markdown(f"""
        <div class="card">
        <div class="card-content">
        <div class="card-icon">
            <i class="fa fa-envelope"></i>
        </div>
        <div class="card-text">
            <h4>Unread Messages</h4>
            1
        </div>
        </div>
        </div>
    """, unsafe_allow_html=True)

st.markdown("---")  # horizontal line

# --- PATIENT APPOINTMENT DETAILS TABLE ---
st.markdown('<h5 style="color:black;">Appointment Details</h5>', unsafe_allow_html=True)

fake = Faker()
appointments = []
for _ in range(3):
    hour = random.randint(8, 16)
    period = "AM" if hour < 12 else "PM"
    display_hour = hour if hour <= 12 else hour - 12  # convert 13-16 to 1-4 PM

    appointments.append({
        "Date": fake.date_this_month(),
        "Time": f"{display_hour}:00 {period}",
        "Doctor": fake.name(),
        "Department": random.choice(["Cardiology", "General", "Orthopedics"]),
        "Location": "Thompson Hospital",
        "Status": random.choice(["Confirmed", "Pending", "Cancelled"]),
        "Edit": '<i class="fa fa-edit"></i>'
    })

df_appointments = pd.DataFrame(appointments)

# Render the table with existing CSS
st.write(
    df_appointments.to_html(
        escape=False, index=False, classes="activity-table"
    ),
    unsafe_allow_html=True
)

fake = Faker()

# Map document types to realistic titles
document_titles_map = {
    "Medical Report": ["MRI Brain Scan", "Electrocardiogram Report", "Chest X-Ray Report", "Ultrasound Abdomen Report", "ECG Report"],
    "Lab Test": ["Complete Blood Count", "Blood Glucose Test", "Lipid Profile", "Liver Function Test", "Kidney Function Test"],
    "Prescription": ["Hypertension Medication Prescription", "Diabetes Medication Prescription", "Antibiotics Prescription", "Pain Relief Prescription", "Vitamin Supplements Prescription"],
    "Other": ["Vaccination Record", "Annual Health Check Summary", "Medical Referral Letter", "Follow-Up Report", "Patient History Summary"]
}

# Map document types to sensible notes
notes_map = {
    "Medical Report": [
        "Patient shows normal heart rhythm on ECG.",
        "Chest X-ray indicates clear lungs.",
        "MRI scan shows no abnormalities.",
        "Ultrasound confirms healthy organs.",
        "ECG results within normal range."
    ],
    "Lab Test": [
        "Blood glucose level within normal range.",
        "Lipid profile indicates low cholesterol.",
        "CBC results are normal.",
        "Kidney function within healthy limits.",
        "Liver enzymes slightly elevated."
    ],
    "Prescription": [
        "Prescribed medication for hypertension.",
        "Antibiotics prescribed for infection.",
        "Pain relief medication prescribed.",
        "Vitamin supplements recommended.",
        "Diabetes medication dosage updated."
    ],
    "Other": [
        "Patient received vaccination as scheduled.",
        "Annual health check completed successfully.",
        "Referral letter sent to specialist.",
        "Follow-up appointment scheduled.",
        "Patient history documented."
    ]
}

departments = ["Cardiology", "Neurology", "Oncology", "Pediatrics", "Other"]

def generate_documents(num_docs=5):
    data = []
    for _ in range(num_docs):
        doc_type = random.choice(list(document_titles_map.keys()))
        # Replace Details column with a clickable link to 10_retrieveprogress_page.py
        details_link = f'<a href="/retrieveprogress_page" target="_self"><i class="fa fa-eye" style="color:#0C1E33;"></i></a>'
        data.append({
            "Document Title": random.choice(document_titles_map[doc_type]),
            "Document Type": doc_type,
            "Doctor": fake.name(),
            "Department": random.choice(departments),
            "Report Date": fake.date_this_year(),
            "Notes": random.choice(notes_map[doc_type]),
            "Details": details_link
        })
    return pd.DataFrame(data)
st.markdown('<div style="margin-top:3%"></div>', unsafe_allow_html=True)

st.markdown('<h5 style="color:black;">New Documents</h5>', unsafe_allow_html=True)
df_current = generate_documents(2)
st.write(df_current.to_html(escape=False, index=False, classes="activity-table"), unsafe_allow_html=True)

st.markdown('<div style="margin-top:3%"></div>', unsafe_allow_html=True)

st.markdown('<h5 style="color:black;">Past Documents</h5>', unsafe_allow_html=True)
df_past = generate_documents(3)
st.write(df_past.to_html(escape=False, index=False, classes="activity-table"), unsafe_allow_html=True)
