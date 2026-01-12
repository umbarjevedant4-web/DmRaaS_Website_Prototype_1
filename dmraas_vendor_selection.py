import streamlit as st

# ---------- APP CONFIG ----------
st.set_page_config(
    page_title="DMRaaS – Vendor Selection",
    layout="centered"
)

# ---------- HEADER ----------
st.title("🧠 DMRaaS")
st.subheader("AI-Assisted Vendor Selection")
st.caption("Decision Memory as a Service – Demo")
st.divider()

# ---------- PROJECT INFO ----------
project = st.text_input(
    "Project Name",
    "ERP Modernization – Phase 1"
)

st.write("### Decision Criteria (Fixed Weights)")
st.write("""
- Cost (30%)
- Security & Compliance (25%)
- Scalability (20%)
- Vendor Lock-in Risk (15%)
- Support Quality (10%)
""")

# ---------- VENDOR INPUT ----------
st.divider()
st.header("Vendor Evaluation")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Vendor A")
    a_cost = st.slider("Cost", 0, 10, 7)
    a_sec = st.slider("Security & Compliance", 0, 10, 9)
    a_scale = st.slider("Scalability", 0, 10, 8)
    a_lock = st.slider("Lock-in Risk", 0, 10, 6)
    a_support = st.slider("Support Quality", 0, 10, 8)

with col2:
    st.subheader("Vendor B")
    b_cost = st.slider("Cost ", 0, 10, 9)
    b_sec = st.slider("Security & Compliance ", 0, 10, 6)
    b_scale = st.slider("Scalability ", 0, 10, 7)
    b_lock = st.slider("Lock-in Risk ", 0, 10, 8)
    b_support = st.slider("Support Quality ", 0, 10, 6)

# ---------- SCORING FUNCTION ----------
def calculate_score(cost, sec, scale, lock, support):
    return (
        cost * 0.30 +
        sec * 0.25 +
        scale * 0.20 +
        lock * 0.15 +
        support * 0.10
    )

# ---------- DECISION ----------
st.divider()

if st.button("🧮 Make Decision"):
    score_a = calculate_score(
        a_cost, a_sec, a_scale, a_lock, a_support
    )
    score_b = calculate_score(
        b_cost, b_sec, b_scale, b_lock, b_support
    )

    st.header("Decision Outcome")

    st.write(f"**Vendor A Score:** {score_a:.2f}")
    st.write(f"**Vendor B Score:** {score_b:.2f}")

    if score_a >= score_b:
        selected = "Vendor A"
        explanation = f"""
Vendor A was selected for **{project}** because:

• Security & Compliance had high priority  
• Vendor A scored significantly better in risk-sensitive areas  
• Higher cost was consciously accepted to reduce long-term
  operational and regulatory risk  

This decision reflects a **risk-minimization strategy**.
"""
    else:
        selected = "Vendor B"
        explanation = f"""
Vendor B was selected for **{project}** because:

• Cost efficiency and flexibility were prioritized  
• Lower vendor lock-in risk supported faster execution  
• Compliance risk was considered acceptable for this phase  

This decision reflects a **cost-optimization strategy**.
"""

    st.success(f"✅ Selected Vendor: {selected}")

    st.subheader("🤖 AI Decision Explanation")
    st.info(explanation)

    st.caption(
        "Decision stored in organizational memory for audits, onboarding, and future review."
    )
