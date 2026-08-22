import streamlit as st

st.set_page_config(
    page_title="MediLens AI",
    page_icon="🩺",
    layout="wide"
)

st.title("🩺 MediLens AI")

st.subheader(
    "Multimodal Medical Understanding & Patient Education Assistant"
)

st.write(
    "Upload a medical document to understand its contents "
    "in simple, patient-friendly language."
)

uploaded_file = st.file_uploader(
    "Upload medical document",
    type=["pdf", "png", "jpg", "jpeg"]
)

if uploaded_file:
    st.success(f"Uploaded: {uploaded_file.name}")

    st.write("File type:", uploaded_file.type)
    st.write("File size:", f"{uploaded_file.size / 1024:.2f} KB")

    if st.button("Analyze"):
        st.info("Analysis pipeline will run here.")