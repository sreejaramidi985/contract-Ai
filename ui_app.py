import streamlit as st
from backend_mock import analyze_contract
from PyPDF2 import PdfReader
from docx import Document

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Contract Analysis System",
    layout="wide"
)

# ---------------- SESSION STATE ----------------
if "document_history" not in st.session_state:
    st.session_state.document_history = []

if "current_result" not in st.session_state:
    st.session_state.current_result = None

if "current_filename" not in st.session_state:
    st.session_state.current_filename = None

# ---------------- FILE TEXT EXTRACTION ----------------
def extract_text(uploaded_file):
    if uploaded_file.name.lower().endswith(".pdf"):
        reader = PdfReader(uploaded_file)
        return "".join([page.extract_text() or "" for page in reader.pages])

    elif uploaded_file.name.lower().endswith(".docx"):
        doc = Document(uploaded_file)
        return "\n".join([p.text for p in doc.paragraphs])

    return ""

# ---------------- HEADER ----------------
st.title("📄 Contract Analysis System")
st.markdown(
    "Upload a contract to analyze using AI agents "
    "(Compliance, Legal, Finance, Operations)"
)
st.markdown("---")

# ---------------- SIDEBAR: DOCUMENT HISTORY ----------------
st.sidebar.header("📁 Document History")

if st.session_state.document_history:
    for idx, filename in enumerate(st.session_state.document_history, start=1):
        st.sidebar.markdown(f"{idx}. {filename}")
else:
    st.sidebar.info("No documents uploaded yet")

# ---------------- FILE UPLOAD ----------------
uploaded_file = st.file_uploader(
    "Upload Contract (PDF or DOCX)",
    type=["pdf", "docx"]
)

# ---------------- ANALYZE ----------------
if uploaded_file:
    if st.button("Analyze Contract"):
        with st.spinner("Analyzing contract..."):
            text = extract_text(uploaded_file)
            analysis_result = analyze_contract(text)

            # 🔥 HISTORY STORES ONLY FILENAMES
            if uploaded_file.name not in st.session_state.document_history:
                st.session_state.document_history.append(uploaded_file.name)

            # 🔥 CLEAR PREVIOUS CONTENT & SET NEW RESULT
            st.session_state.current_result = analysis_result
            st.session_state.current_filename = uploaded_file.name

        st.success("Analysis completed successfully!")

# ---------------- DISPLAY ONLY LATEST RESULT ----------------
if st.session_state.current_result:
    st.markdown("---")
    st.header("📊 Latest Analysis Result")
    st.subheader(f"📄 {st.session_state.current_filename}")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("🛡 Compliance Analysis")
        issues = st.session_state.current_result["Compliance"]
        if issues:
            for issue in issues:
                st.markdown(f"- {issue}")
        else:
            st.markdown("- No compliance issues detected")

    with col2:
        st.subheader("⚖ Legal Analysis")
        issues = st.session_state.current_result["Legal"]
        if issues:
            for issue in issues:
                st.markdown(f"- {issue}")
        else:
            st.markdown("- No legal issues detected")

    col3, col4 = st.columns(2)

    with col3:
        st.subheader("💰 Financial Analysis")
        issues = st.session_state.current_result["Finance"]
        if issues:
            for issue in issues:
                st.markdown(f"- {issue}")
        else:
            st.markdown("- No financial issues detected")

    with col4:
        st.subheader("⚙ Operational Analysis")
        issues = st.session_state.current_result["Operations"]
        if issues:
            for issue in issues:
                st.markdown(f"- {issue}")
        else:
            st.markdown("- No operational issues detected")

    # ---------------- RAW JSON ----------------
    with st.expander("📂 View Raw JSON Report"):
        st.json(st.session_state.current_result)

# ---------------- FEEDBACK ----------------
st.markdown("---")
st.header("💬 Feedback")

feedback = st.text_area("Provide feedback or request refinement")

if st.button("Submit Feedback"):
    st.success("Thank you! Feedback recorded.")

# ---------------- FOOTER ----------------
st.markdown("---")
st.markdown("© 2026 Contract Analysis System")
