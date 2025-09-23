import streamlit as st
import time
import base64
import os
# from Quantum-Kancil-Durian-.Staff_Portal import QKD_Six_State_Symmetric as QKD
# C:\Users\tiong yong qing\Quantum-Kancil-Durian-\Patient_Portal\pages\11_retrieveprogress_page.py
# C:\Users\tiong yong qing\Quantum-Kancil-Durian-\Staff_Portal\QKD_Six_State_Symmetric.py
from QKD_Six_State_Symmetric import QKD 

st.session_state.nric = "900101011234"
st.session_state.last_name = "Doe"
st.session_state.first_name = "John"
st.session_state.phone_number = "012-3456789"
st.session_state.staff_id = "S123456"
st.session_state.username = "Doe, John"

# --- PAGE CONFIG ---
st.set_page_config(page_title="Operation Progress", layout="wide")
# st.write(st.session_state.username)

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
            
            
    </style>
""", unsafe_allow_html=True)

# --- Display Submitted Info ---
st.subheader("Retrieving Documents...")
st.markdown("Please be Patient")

def get_base64_image(path):
    with open(path, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

img_base64 = get_base64_image("logo.png")

col1, col2, col3 = st.columns([0.05, 0.90, 0.05])
with col2:
    st.markdown(
        f"""
        <div style="text-align:center; margin-top:2%; margin-bottom:2%;">
            <img src="data:image/png;base64,{img_base64}" width="150">
        </div>
        """,
        unsafe_allow_html=True
    )

# --- Steps ---
steps = [
    "Request Submitted",
    "Retrieving Data",
    "Generating Quantum Keys",
    "Transmitting Quantum Keys",
    "Decrypting Quantum Keys",
    "Operation Successful"
]
#################################################################################
# Initialize step columns
step_cols = st.columns(len(steps))

# --- Simulated Progress ---
progress_bar = st.progress(0)
status_text = st.empty()

for i, step in enumerate(steps):
    status_text.info(f"Step {i+1}/{len(steps)}: {step}")

    # Highlight current step
    for j, col in enumerate(step_cols):
        color = "#0C1E33" if j <= i else "#ddd"

    # Update progress bar
    progress_bar.progress(int((i+1)/len(steps)*100))
    time.sleep(0.7)  # simulate delay

st.success("🎉 Operation Completed Successfully!")
st.switch_page("pages/7_downloadpdf.py")

##################################################################################
# SIZE_TX = 1000000
# pdf_path = "MRI BRAIN W_O CONTRAST.pdf"
# noise = 0.0
# simuStart =time.time() # To calculate time
# qkd = QKD(SIZE_TX, pdf_path, noise)
# st.session_state.tem_decrypt_file = qkd.final()
# # print("DEBUG:", st.session_state.tem_decrypt_file)
# simuEnd = time.time()
# print("Execution time:", simuEnd - simuStart, "seconds")

# # Destination path (same folder, new name)
# dst_path = os.path.join(os.path.dirname(st.session_state.tem_decrypt_file), "QKD_decrypt_no_error.pdf")

# # Copy file using read/write
# with open(st.session_state.tem_decrypt_file, "rb") as f_src:
#     with open(dst_path, "wb") as f_dst:
#         f_dst.write(f_src.read())

# st.success("🎉 Operation Completed Successfully!")
# st.switch_page("pages/7_downloadpdf.py")
##################################################################################