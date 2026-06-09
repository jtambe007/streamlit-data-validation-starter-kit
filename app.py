import streamlit as st
import pandas as pd

st.set_page_config(page_title="Data Validation Starter Kit", layout="wide")

GUMROAD_URL = "https://clearlineanalytics.gumroad.com/l/datastarterkit"

with st.sidebar:
    st.markdown("## Data Validation Starter Kit")
    st.info("Preview version. Upload any CSV to see the interface.")
    st.markdown("---")
    st.markdown("### Get the Full Validation Engine")
    st.markdown(
        "This preview shows the interface. The full kit includes the complete "
        "validation engine, PDF export, industry configs, and setup guide."
    )
    st.markdown(
        f'<a href="{GUMROAD_URL}" target="_blank" style="text-decoration: none;">'
        '<div style="background-color: #C2694F; color: white; text-align: center; '
        'padding: 12px; border-radius: 8px; font-weight: bold; font-size: 16px;">'
        'Download Full Kit ($97)</div></a>',
        unsafe_allow_html=True
    )
    st.markdown("*MIT Licensed. Personal & commercial use allowed.*")
    st.markdown("---")
    st.markdown("**Full kit includes:**")
    st.markdown("""
- Complete validation engine (5 checks)
- PDF report export
- Industry configs (Retail, Healthcare, Finance)
- 30-min setup & extension guide
    """)

st.title("Data Health Validator")
st.caption("Preview Version. The full validation engine is available in the Starter Kit")

industry = st.selectbox(
    "Select an industry profile",
    options=["Default", "Retail", "Healthcare", "Finance"]
)

uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])
reference_file = st.file_uploader("Upload reference schema CSV (optional)", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.success(f"Loaded {len(df):,} rows × {len(df.columns)} columns")
    st.dataframe(df.head(10), use_container_width=True)

    st.markdown("---")
    st.markdown("### Validation Results")

    try:
        from validator.checks import run_all_checks
        results = run_all_checks(df, {})
    except NotImplementedError:
        col1, col2, col3, col4 = st.columns(4)
        col1.metric("Health Score", "— /100")
        col2.metric("Grade", "—")
        col3.metric("Checks Passed", "—/—")
        col4.metric("Errors", "—")

        st.warning(
            "The validation engine is not included in the preview. "
            "Purchase the full kit to run all five checks on your data."
        )

        st.markdown(
            f'<a href="{GUMROAD_URL}" target="_blank" style="text-decoration: none;">'
            '<div style="background-color: #C2694F; color: white; text-align: center; '
            'padding: 14px; border-radius: 8px; font-weight: bold; font-size: 18px; '
            'max-width: 420px; margin: 20px auto;">'
            'Unlock the Full Validation Engine — $97</div></a>',
            unsafe_allow_html=True
        )

        col_a, col_b = st.columns(2)
        with col_a:
            st.markdown("""
**Checks unlocked:**
- Null rate per column
- Duplicate & key-column detection
- Type mismatch detection
            """)
        with col_b:
            st.markdown("""
**Also included:**
- Outlier detection (IQR + z-score)
- Schema drift vs reference CSV
- One-click PDF report export
            """)
