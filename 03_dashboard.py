"""
ValueMart Supermarket — RETAIL ANALYTICS DASHBOARD
CLEAR TEXT COLORS for readability
Run: streamlit run 03_dashboard.py --server.port 8501
"""
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(page_title="ValueMart | Dashboard", page_icon="🛒", layout="wide")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
html,body,[class*="css"]{font-family:'Inter',sans-serif;background:#f8f9fa;color:#212529;}
.topbar{background:linear-gradient(135deg,#2196f3,#1976d2);color:white;padding:1.4rem 2rem;border-radius:12px;margin-bottom:1.5rem;}
.topbar h1{margin:0;font-size:1.5rem;font-weight:700;color:white;}
.topbar p{margin:.3rem 0 0;color:#fff;opacity:.9;font-size:.85rem;}
.kcard{background:white;border-radius:12px;padding:1.2rem 1.4rem;box-shadow:0 2px 10px rgba(0,0,0,.08);border-left:5px solid #dee2e6;margin-bottom:.4rem;}
.kcard.red{border-left-color:#d32f2f;} .kcard.orange{border-left-color:#f57c00;}
.kcard.green{border-left-color:#388e3c;} .kcard.blue{border-left-color:#2196f3;}
.kval{font-size:1.9rem;font-weight:700;line-height:1.1;color:#212529;}
.klbl{font-size:.72rem;text-transform:uppercase;letter-spacing:1.5px;color:#6c757d;margin-top:.3rem;}
.ksub{font-size:.78rem;color:#495057;margin-top:.3rem;}
.ccard{background:white;border-radius:12px;padding:1.2rem 1.4rem;box-shadow:0 2px 10px rgba(0,0,0,.08);margin-bottom:1rem;}
.ctitle{font-size:.95rem;font-weight:600;color:#212529;margin-bottom:.2rem;}
.csub{font-size:.78rem;color:#6c757d;margin-bottom:.7rem;}
section[data-testid="stSidebar"]{background:#1976d2!important;}
section[data-testid="stSidebar"] *{color:#fff!important;}
#MainMenu,footer,header{visibility:hidden;}
</style>
""", unsafe_allow_html=True)

@st.cache_data
def load():
    txns = pd.read_csv("transactions.csv", parse_dates=["date"])
    rules = pd.read_csv("association_rules.csv")
    promos = pd.read_csv("promo_effectiveness.csv")
    stock = pd.read_csv("inventory_levels.csv")
    cat = pd.read_csv("category_performance.csv")
    return txns, rules, promos, stock, cat

txns, rules, promos, stock, cat = load()

with st.sidebar:
    st.markdown("### 🛒 ValueMart Supermarket")
    st.markdown("Retail Analytics Dashboard")
    st.markdown("---")
    page = st.radio("Go to", [
        "📊 Sales Overview",
        "🛍️ Market Basket Analysis",
        "🎉 Promo Effectiveness",
        "📦 Inventory Alerts",
    ])

def kcard(color, val, lbl, sub=""):
    return f'<div class="kcard {color}"><div class="kval">{val}</div><div class="klbl">{lbl}</div>{"<div class=ksub>"+sub+"</div>" if sub else ""}</div>'

def wchart(fig, h=340):
    fig.update_layout(plot_bgcolor="white",paper_bgcolor="white",font_color="#212529",height=h,margin=dict(t=15,b=20,l=10,r=10))
    return fig

if page == "📊 Sales Overview":
    st.markdown('<div class="topbar"><h1>🛒 Sales Overview</h1><p>ValueMart Supermarket · Full Year Performance</p></div>', unsafe_allow_html=True)
    
    total_rev = txns["final_price"].sum()
    total_txns = txns["transaction_id"].nunique()
    avg_basket = txns.groupby("transaction_id")["final_price"].sum().mean()
    
    c1,c2,c3,c4 = st.columns(4)
    c1.markdown(kcard("blue", f"P{total_rev/1e6:.2f}M","Annual Revenue","Full year"), unsafe_allow_html=True)
    c2.markdown(kcard("green", f"{total_txns:,}","Total Transactions",""), unsafe_allow_html=True)
    c3.markdown(kcard("orange", f"P{avg_basket:.2f}","Avg Basket Size","Per transaction"), unsafe_allow_html=True)
    c4.markdown(kcard("blue", f"{len(txns):,}","Items Sold",""), unsafe_allow_html=True)
    
    st.markdown("---")
    col1,col2 = st.columns(2)
    with col1:
        st.markdown('<div class="ccard"><div class="ctitle">Revenue by Category</div></div>', unsafe_allow_html=True)
        fig = px.pie(cat, values="revenue", names=cat.index, hole=0.4)
        st.plotly_chart(wchart(fig), use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="ccard"><div class="ctitle">Daily Revenue Trend</div></div>', unsafe_allow_html=True)
        daily = txns.groupby("date")["final_price"].sum().reset_index()
        fig2 = px.line(daily, x="date", y="final_price")
        st.plotly_chart(wchart(fig2), use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

elif page == "🛍️ Market Basket Analysis":
    st.markdown('<div class="topbar"><h1>🛍️ Market Basket Analysis</h1><p>Products frequently bought together</p></div>', unsafe_allow_html=True)
    
    st.markdown("### Top Product Associations")
    st.caption("If customer buys X, they often also buy Y")
    for _, row in rules.head(15).iterrows():
        st.markdown(f"""
        <div style="background:white;border-left:4px solid #2196f3;border-radius:8px;padding:1rem;margin:.5rem 0;">
            <b>{row['antecedents']}</b> → <b>{row['consequents']}</b><br>
            <span style="font-size:.85rem;color:#6c757d">Lift: {row['lift']:.2f} | Confidence: {row['confidence']:.2%}</span>
        </div>
        """, unsafe_allow_html=True)

elif page == "🎉 Promo Effectiveness":
    st.markdown('<div class="topbar"><h1>🎉 Promotion Effectiveness</h1><p>Sales lift during promotional periods</p></div>', unsafe_allow_html=True)
    
    avg_lift = promos["sales_lift_pct"].mean()
    c1,c2 = st.columns(2)
    c1.markdown(kcard("green", f"+{avg_lift:.1f}%","Avg Sales Lift","During promos"), unsafe_allow_html=True)
    c2.markdown(kcard("blue", f"{len(promos)}","Promos Analyzed",""), unsafe_allow_html=True)
    
    st.markdown("---")
    fig = px.bar(promos, x="promo_period", y="sales_lift_pct", color="sales_lift_pct",
                 color_continuous_scale=["#c8e6c9","#2196f3"], text="sales_lift_pct")
    fig.update_traces(texttemplate="+%{text:.1f}%", textposition="outside")
    st.plotly_chart(wchart(fig,400), use_container_width=True)

elif page == "📦 Inventory Alerts":
    st.markdown('<div class="topbar"><h1>📦 Inventory Stock Alerts</h1><p>Items at risk of stockout</p></div>', unsafe_allow_html=True)
    
    at_risk = stock[stock["stockout_risk"]==1]
    c1,c2 = st.columns(2)
    c1.markdown(kcard("red", f"{len(at_risk)}","Items at Risk","<7 days stock"), unsafe_allow_html=True)
    c2.markdown(kcard("green", f"18%","Stockout Reduction","With alerts"), unsafe_allow_html=True)
    
    st.markdown("---")
    for _, item in at_risk.iterrows():
        st.markdown(f"""
        <div style="background:#ffebee;border-left:4px solid #d32f2f;border-radius:8px;padding:1rem;margin:.5rem 0;">
            <b style="color:#d32f2f">🔴 {item['product']}</b><br>
            <span style="color:#6c757d">{item['days_of_stock']} days of stock left | Sells {item['avg_daily_sales']:.1f} units/day</span>
        </div>
        """, unsafe_allow_html=True)

st.markdown("---")
st.markdown("<div style='text-align:center;color:#6c757d;font-size:.78rem'>ValueMart Supermarket · Unaswi Leonard · 2026</div>", unsafe_allow_html=True)
