import streamlit as st
from PyPDF2 import PdfReader, PdfWriter
from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import base64
st.session_state.nric = "900101011234"
st.session_state.last_name = "Doe"
st.session_state.first_name = "John"
st.session_state.phone_number = "012-3456789"
st.session_state.staff_id = "S123456"
st.session_state.username = "Doe, John"

# --- PAGE CONFIG ---
st.set_page_config(page_title="View & Download PDF", layout="wide")

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

    div[data-baseweb="input"],
    div[data-baseweb="textarea"],
    div[data-baseweb="select"],
    div[data-baseweb="datepicker"] {
        border: 0.1em solid grey !important;
        border-radius: 0.3em !important;
        padding: 0 !important;
        background-color: white !important;
        width: 40%;
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

                  
            
    </style>
""", unsafe_allow_html=True)

# --- DISPLAY PDF ---
st.subheader("Sample PDF Document")

# --- SAMPLE PDF (can replace with any file) ---
sample_pdf_path = "QKD_decrypt_no_error.pdf"

# --- USERNAME (for watermark) ---
username = st.session_state.first_name + ", " + st.session_state.last_name

# --- FUNCTION TO CREATE WATERMARKED PDF ---
def add_watermark(input_pdf_path, watermark_text):
    # Create watermark PDF in memory
    packet = BytesIO()
    can = canvas.Canvas(packet, pagesize=letter)
    can.setFont("Helvetica", 40)
    can.setFillColorRGB(0.7, 0.7, 0.7, alpha=0.3)  # light gray, semi-transparent
    can.saveState()
    can.translate(300, 500)
    can.rotate(45)
    can.drawCentredString(0, 0, watermark_text)
    can.restoreState()
    can.save()
    packet.seek(0)

    # Read original PDF
    reader = PdfReader(input_pdf_path)
    watermark_reader = PdfReader(packet)
    writer = PdfWriter()

    # Merge watermark onto each page
    for page in reader.pages:
        page.merge_page(watermark_reader.pages[0])
        writer.add_page(page)

    output_stream = BytesIO()
    writer.write(output_stream)
    output_stream.seek(0)
    return output_stream

# --- CREATE WATERMARKED PDF ---
watermarked_pdf = add_watermark(sample_pdf_path, f"Downloaded by {username}")


pdf_bytes = watermarked_pdf.getvalue()
pdf_base64 = base64.b64encode(pdf_bytes).decode('utf-8')

st.markdown(f"""
<div style="position: relative;">
    <iframe src="data:application/pdf;base64,{pdf_base64}" width="100%" height="500" style="border:1px solid #ddd;"></iframe>
</div>
""", unsafe_allow_html=True)

# # --- DOWNLOAD BUTTON ---
# st.download_button(
#     label="Download PDF",
#     data=watermarked_pdf,
#     file_name="sample_watermarked.pdf",
#     mime="application/pdf",
#     help="Click to download the PDF with your watermark"
# )

st.markdown("""
<style>
.black-button {{
    display: inline-block;
    width: 20%;
    margin-top: 2%;
    padding-top: 0.8%;
    padding-bottom: 0.8%;
    background-color: black;
    border-radius: 8px;
    font-weight: 400;
    color: white !important;
    text-decoration: none !important;
    font-size: 1em !important;
    text-align: center;
}}
.black-button:hover {{
    background-color: white;
    color: black !important;
    border: 0.1em solid grey !important;
}}
</style>
<a href="data:application/pdf;base64,{pdf_base64}" download="sample_watermarked.pdf" class="black-button">Download PDF</a>
""".format(pdf_base64=pdf_base64), unsafe_allow_html=True)

if st.button("If Interupt"):
    st.switch_page("pages/13_retrieveERROR.py")
if st.button("🏠 Go to Home Page"):
    st.switch_page("pages/2_staffhomepage.py")