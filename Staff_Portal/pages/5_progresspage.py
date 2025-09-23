import streamlit as st
import time
import base64


# --- PAGE CONFIG ---
st.set_page_config(page_title="Operation Progress", layout="wide")

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
st.subheader("Submitting Documents...")
st.info(f"Patient: {st.session_state.patient_first} {st.session_state.patient_last} | Uploaded file: {st.session_state.uploaded_filename}")

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
    "Form Submitted",
    "Generating Quantum Keys",
    "Transmitting Quantum Keys",
    "Decrypting Quantum Keys",
    "Storing Documents into Database",
    "Operation Successful"
]

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
st.switch_page("pages/2_staffhomepage.py")