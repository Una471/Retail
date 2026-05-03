"""
CHOPPIES — RETAIL MANAGEMENT SYSTEM
Reorder alerts + shelf placement recommendations
"""
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Choppies | System", page_icon="🛒", layout="wide")

st.markdown("""<style>
html,body{font-family:Inter,sans-serif;background:#f8f9fa;color:#212529;}
.topbar{background:#2196f3;color:white;padding:1.2rem;border-radius:12px;margin-bottom:1rem;}
section[data-testid="stSidebar"]{background:#1976d2!important;}
section[data-testid="stSidebar"] *{color:#fff!important;}
</style>""", unsafe_allow_html=True)

@st.cache_data
def load():
    stock = pd.read_csv("inventory_levels.csv")
    rules = pd.read_csv("association_rules.csv")
    return stock, rules

stock, rules = load()

nav = st.sidebar.radio("Menu", ["📦 Reorder Alerts","🛍️ Shelf Placement"])

if nav == "📦 Reorder Alerts":
    st.markdown('<div class="topbar"><h1>📦 Automated Reorder Alerts</h1></div>', unsafe_allow_html=True)
    at_risk = stock[stock["stockout_risk"]==1]
    for _, item in at_risk.iterrows():
        st.error(f"🔴 **{item['product']}** | {item['days_of_stock']} days left | Reorder: {item['reorder_point']} units")

else:
    st.markdown('<div class="topbar"><h1>🛍️ Shelf Placement Recommendations</h1></div>', unsafe_allow_html=True)
    st.info("Place these items near each other to increase basket size:")
    for _, row in rules.head(10).iterrows():
        st.success(f"✅ {row['antecedents']} ← near → {row['consequents']}")
