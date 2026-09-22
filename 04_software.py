"""ValueMart retail operations: reorder alerts and shelf recommendations."""
import base64
from pathlib import Path
from datetime import datetime
import pandas as pd
import streamlit as st

# Respect report links even when Streamlit Cloud starts this file directly.
if st.query_params.get("view") == "dashboard":
    import runpy
    from pathlib import Path
    runpy.run_path(str(Path(__file__).resolve().parent / "03_dashboard.py"), run_name="__main__")
    st.stop()
with st.columns([5, 1])[1]:
    st.link_button("Dashboard", "?view=dashboard", use_container_width=True)

BASE_DIR = Path(__file__).resolve().parent

st.markdown("""<style>
@import url('https://fonts.googleapis.com/css2?family=Momo+Trust+Display&family=Red+Hat+Display:wght@500;600;700;800&family=Stack+Sans+Text:wght@400;500;600;700&display=swap');
:root{--forest:#143d1b;--leaf:#587b38;--sage:#e6eadb;--cream:#f7f5ed;--paper:#fffefb;--ink:#1d251d;--muted:#596258;--line:#d9ded2;--danger:#8d3027}
html,body,[class*="css"],input,button,select{font-family:'Archivo',Arial,sans-serif!important;color:var(--ink)}.stApp{background:var(--paper)}.block-container{max-width:1180px;padding:0 2.3rem 3rem}h1,h2,h3{font-family:'Archivo',Arial,sans-serif!important;color:var(--ink);letter-spacing:-.04em}
.notice{background:var(--forest);color:#fff;text-align:center;padding:.52rem;font-size:.64rem;letter-spacing:.08em;text-transform:uppercase;margin:0 -2.3rem}.site-header{display:flex;align-items:center;justify-content:space-between;padding:1.25rem 0;border-bottom:1px solid var(--line)}.wordmark{position:relative;text-align:center;line-height:.8}.wordmark:before,.wordmark:after{content:"";position:absolute;width:11px;height:19px;background:var(--leaf);border-radius:100% 0 100% 0;top:-14px}.wordmark:before{left:47%;transform:rotate(-28deg)}.wordmark:after{left:54%;transform:scaleX(-1) rotate(-28deg)}.wordmark strong{font-family:'Cormorant Garamond',serif;color:#172619;font-size:1.7rem;letter-spacing:.14em}.wordmark small{display:block;margin-top:.55rem;font-size:.49rem;letter-spacing:.24em;color:#596258}.header-meta{font-size:.61rem;letter-spacing:.14em;text-transform:uppercase;color:#626b61;font-weight:600}.header-meta span{color:var(--forest);margin-left:1rem}
.retail-hero{height:410px;background-size:cover;background-position:center;display:flex;align-items:center;padding:3.2rem;margin-bottom:1.2rem}.hero-copy{max-width:430px}.eyebrow{font-size:.67rem;letter-spacing:.12em;text-transform:uppercase;color:var(--forest);font-weight:700}.hero-copy h1{font-family:'DM Sans',sans-serif!important;font-size:3rem;line-height:1.02;letter-spacing:-.055em;margin:.65rem 0 1rem;color:#17301c;font-weight:600}.hero-copy h1 span{color:#486f35}.hero-copy p{font-size:.82rem;line-height:1.7;color:#3f4c41;max-width:360px}.hero-cta{display:inline-block;background:var(--forest);color:#fff!important;padding:.72rem 1.25rem;font-size:.61rem;text-transform:uppercase;letter-spacing:.12em;font-weight:700;margin-top:.65rem}
.benefits{display:grid;grid-template-columns:repeat(4,1fr);gap:1rem;padding:1rem 1.2rem;background:#f8f8f1;margin-bottom:1.5rem}.benefit{display:flex;gap:.7rem;align-items:center}.benefit i{width:34px;height:34px;border:1px solid #afc0a3;border-radius:50%;display:grid;place-items:center;color:var(--forest);font-style:normal;font-size:.63rem;font-weight:700}.benefit b{display:block;font-size:.67rem}.benefit span{font-size:.58rem;color:var(--muted)}
.category-panel{text-align:center;margin:1.8rem 0 1.6rem}.category-panel h2{font-size:2rem;margin:0 0 .8rem}.category-photo{height:245px;background-size:cover;background-position:center}.category-names{display:grid;grid-template-columns:repeat(5,1fr);background:#fff;border:1px solid var(--line);border-top:0}.category-names span{padding:.7rem;border-right:1px solid var(--line);font-size:.59rem;letter-spacing:.08em;text-transform:uppercase;font-weight:700}.category-names span:last-child{border-right:0}
.nav-label{text-align:center;font-size:.57rem;letter-spacing:.16em;text-transform:uppercase;color:#697267;font-weight:700;margin:1.2rem 0 .4rem}div[data-testid="stRadio"]>div{justify-content:center;gap:.3rem;border-block:1px solid var(--line);padding:.38rem 0;margin-bottom:1.35rem}div[data-testid="stRadio"] label{padding:.62rem 1.2rem;margin:0!important}div[data-testid="stRadio"] label:has(input:checked){background:var(--forest)}div[data-testid="stRadio"] label p{font-size:.72rem;font-weight:600;color:#354438!important;white-space:nowrap}div[data-testid="stRadio"] label:has(input:checked) p{color:#fff!important}div[data-testid="stRadio"] div[role="radiogroup"]>label>div:first-child{display:none}
.topbar{background:var(--sage);padding:1.65rem 1.9rem;margin-bottom:1rem;border-left:4px solid var(--forest)}.topbar h1{font-size:2.15rem;margin:0}.topbar p{font-size:.75rem;color:#465347;margin:.35rem 0 0}.stock-card,.pair-card{background:#fff;border:1px solid var(--line);padding:1rem 1.15rem;margin:.55rem 0;display:grid;align-items:center}.stock-card{grid-template-columns:1fr auto;gap:1rem;border-left:4px solid var(--danger)}.pair-card{grid-template-columns:1fr auto 1fr;border-left:4px solid var(--leaf);gap:1rem}.product-name{font-family:'Cormorant Garamond',serif;font-size:1.25rem;font-weight:600;color:var(--ink)}.product-meta{font-size:.7rem;color:var(--muted);margin-top:.2rem}.stock-action{background:#f2e1dd;color:#70251e;padding:.55rem .75rem;font-size:.64rem;font-weight:700;text-align:center}.pair-arrow{color:var(--leaf);font-size:.72rem;text-transform:uppercase;letter-spacing:.08em}.pair-card .right{text-align:right}.empty-state{background:#edf3e7;border:1px solid #cad8bd;padding:1rem;color:#2c4d29}
section[data-testid="stSidebar"]{display:none!important}#MainMenu,footer,header{visibility:hidden}
.wordmark strong,.product-name,.purpose .number{font-family:'Archivo',Arial,sans-serif!important}.wordmark strong{font-size:1.25rem!important;letter-spacing:.08em!important;font-weight:700!important}.product-name{font-size:1rem!important}.purpose .number{font-size:2rem!important;color:#143d1b!important;font-weight:700!important}.purpose .intro b{display:inline!important;color:#143d1b!important}.purpose>div b{color:#1d251d!important}.purpose>div span{color:#596258!important}.purpose h2{color:#1d251d!important;font-size:1.45rem!important}.hero-copy h1{font-weight:700!important}
.retail-hero{height:285px;padding:2.5rem}.hero-copy{max-width:440px}.hero-copy h1{font-size:2.55rem;margin-bottom:.8rem}.hero-copy p{max-width:390px}.purpose{display:grid;grid-template-columns:1.25fr .75fr .75fr;gap:1px;background:var(--line);border:1px solid var(--line);margin-bottom:1.4rem}.purpose>div{background:#fff;padding:1.25rem}.purpose .intro{background:#f3f4ea}.purpose .label{font-size:.56rem;letter-spacing:.13em;text-transform:uppercase;color:var(--forest);font-weight:700}.purpose h2{font-size:1.7rem;line-height:1;margin:.4rem 0 .55rem}.purpose p{font-size:.7rem;line-height:1.6;color:#505b51;margin:0}.purpose .number{font-family:'Cormorant Garamond',serif;font-size:2.3rem;line-height:1;color:var(--forest);font-weight:600}.purpose b{display:block;font-size:.68rem;margin:.4rem 0 .2rem}.purpose span{font-size:.62rem;color:var(--muted)}.workflow{display:grid;grid-template-columns:1fr 1fr;gap:.8rem;margin-bottom:1.2rem}.workflow div{padding:.9rem 1rem;border-left:3px solid var(--leaf);background:#fafaf5}.workflow b{display:block;font-size:.72rem}.workflow span{font-size:.65rem;color:var(--muted)}.evidence{display:block;font-size:.58rem;color:#596258;margin-top:.25rem;text-transform:none;letter-spacing:0}
@media(max-width:800px){.block-container{padding:0 1rem 2rem}.notice{margin:0 -1rem}.retail-hero{height:270px;padding:1.3rem;background-position:60% center}.hero-copy{max-width:62%}.hero-copy h1{font-size:1.8rem}.purpose{grid-template-columns:1fr}.workflow{grid-template-columns:1fr}.header-meta{display:none}div[data-testid="stRadio"]>div{justify-content:flex-start;overflow-x:auto}}
.purpose .intro b{display:inline!important}.purpose .intro p{color:#404b41!important}.purpose .number,.purpose>div b,.purpose>div span{visibility:visible!important;opacity:1!important}.wordmark:before,.wordmark:after{display:none!important}.wordmark{text-align:left!important;line-height:1!important;border-left:3px solid var(--forest);padding-left:.7rem}.wordmark small{margin-top:.3rem!important}
/* Portfolio typography: expressive brand, editorial headings, highly legible UI. */
html,body,[class*="css"],p,label,input,button,select,textarea{font-family:'Stack Sans Text','Segoe UI',sans-serif!important}
h1,h2,h3,h4,.topbar h1,.purpose h2{font-family:'Red Hat Display','Segoe UI',sans-serif!important;letter-spacing:-.035em}
.wordmark strong{font-family:'Momo Trust Display','Red Hat Display',sans-serif!important;letter-spacing:.08em!important}
.hero-copy h1{font-family:'Red Hat Display','Segoe UI',sans-serif!important;font-weight:700;letter-spacing:-.055em}
.product-name,.purpose .number{font-family:'Red Hat Display','Segoe UI',sans-serif!important}
button,div[data-testid="stRadio"] label p,.eyebrow,.header-meta,.klbl{font-family:'Stack Sans Text','Segoe UI',sans-serif!important}
.retail-hero{height:300px!important;padding:2.4rem!important;align-items:center;margin-bottom:.7rem}.retail-hero .hero-copy{max-width:450px}.retail-hero .hero-copy h1{font-size:2.35rem!important;line-height:1.05!important;margin:.65rem 0 .9rem!important}.retail-hero .eyebrow{display:block;position:static;margin:0 0 .45rem;line-height:1.3}.purpose,.workflow{display:none!important}.nav-label{margin-top:.45rem}.workspace-note{display:flex;justify-content:space-between;gap:1.2rem;align-items:center;background:#f1f4e9;border-left:4px solid var(--forest);padding:.8rem 1rem;margin:.2rem 0 .85rem}.workspace-note b{font-size:.78rem}.workspace-note span{font-size:.72rem;color:var(--muted)}div[data-testid="stRadio"]{position:sticky;top:0;z-index:50;background:rgba(247,245,237,.96);padding:.35rem 0;backdrop-filter:blur(10px)}.stock-card,.pair-card{transition:border-color .18s ease,transform .18s ease}.stock-card:hover,.pair-card:hover{transform:translateY(-2px);border-color:#9aa78d}.data-hint{font-size:.72rem;color:var(--muted);margin:.2rem 0 .8rem}@media(max-width:800px){.retail-hero{height:330px!important;padding:1.4rem!important}.retail-hero .hero-copy{max-width:68%}.retail-hero .hero-copy h1{font-size:1.8rem!important}}
.topbar p{max-width:720px!important;font-size:.84rem!important;line-height:1.55!important;color:#37453a!important}.stock-card *,.pair-card *,.workspace-note *,.empty-state{opacity:1!important}.stAlert,.stAlert *{color:#172619!important}.stTextInput label p,.stNumberInput label p,.stSelectbox label p,.stMultiSelect label p,.stSlider label p{color:#203321!important;font-size:.82rem!important}.composition{display:grid;grid-template-columns:160px 1fr;gap:1rem;padding:1rem 1.2rem;background:#f1f4e9;border-left:4px solid var(--forest);margin:.8rem 0}.composition b{font-size:.72rem;text-transform:uppercase;letter-spacing:.1em;color:var(--forest)}.composition p{margin:0;max-width:760px;color:#415043;line-height:1.55;font-size:.82rem}@media(max-width:700px){.composition,.workspace-note{grid-template-columns:1fr;display:grid}}
.workspace-note b{color:#173f20!important;opacity:1!important;font-weight:700!important}.workspace-note span{color:#40514c!important;opacity:1!important}
.cross-app-link{position:fixed;top:1rem;right:1.7rem;z-index:9999;display:inline-flex;align-items:center;justify-content:center;padding:.62rem 1rem;background:#11131a;color:#fff!important;border:1px solid rgba(255,255,255,.18);border-radius:5px;font:650 .78rem "Stack Sans Text","Segoe UI",sans-serif;text-decoration:none!important;box-shadow:0 3px 12px rgba(0,0,0,.18)}.cross-app-link:hover{filter:brightness(1.12)}</style>""", unsafe_allow_html=True)

@st.cache_data
def load():
    return pd.read_csv(BASE_DIR / "inventory_levels.csv"), pd.read_csv(BASE_DIR / "association_rules.csv")

@st.cache_data(show_spinner=False)
def image_b64(name):
    return base64.b64encode((Path(__file__).parent / "assets" / name).read_bytes()).decode("ascii")

stock, rules = load()
hero = image_b64("valuemart-hero.webp")
if "reorder_history" not in st.session_state: st.session_state.reorder_history = []
if "placement_history" not in st.session_state: st.session_state.placement_history = []
at_risk_count = int((stock["stockout_risk"] == 1).sum())
reorder_units = int(stock.loc[stock["stockout_risk"] == 1, "reorder_point"].sum())
st.markdown(f"""
<div class="notice">Retail clarity, from stockroom to shelf</div><div class="site-header"><div class="wordmark"><strong>VALUEMART</strong><small>RETAIL INTELLIGENCE</small></div><div class="header-meta">Inventory <span>Merchandising</span></div></div>
<div class="retail-hero" style="background-image:linear-gradient(90deg,rgba(247,245,237,.98) 0%,rgba(247,245,237,.92) 35%,rgba(247,245,237,.05) 64%),url('data:image/webp;base64,{hero}')"><div class="hero-copy"><div class="eyebrow">Inventory & merchandising assistant</div><h1>Know What to Reorder.<br><span>Know What to Place Together.</span></h1><p>A focused workspace for store and inventory managers. It converts stock levels and customer basket data into actions for today.</p></div></div>
<div class="purpose"><div class="intro"><div class="label">What this software does</div><h2>Two decisions, one workspace</h2><p>Use <b>Reorder alerts</b> to prevent empty shelves. Use <b>Shelf placement</b> to position products that customers frequently buy together.</p></div><div><div class="number">{at_risk_count}</div><b>Products need reordering</b><span>Based on current stock cover</span></div><div><div class="number">{reorder_units:,}</div><b>Suggested units</b><span>Total reorder-point quantity</span></div></div>
<div class="workflow"><div><b>1. Replenishment</b><span>Review products at risk and the quantity recommended for ordering.</span></div><div><b>2. Merchandising</b><span>Review evidence-based product pairs and adjust nearby shelf placement.</span></div></div><div class="nav-label">Choose the task you want to complete</div>
""", unsafe_allow_html=True)

st.markdown('<div class="workspace-note"><b>Store action workspace</b><span>Act on replenishment and shelf-placement recommendations here. Use the separate dashboard to investigate sales and inventory trends.</span></div>', unsafe_allow_html=True)
nav = st.radio("Retail operations", ["Reorder alerts", "Shelf placement"], horizontal=True, label_visibility="collapsed")
if nav == "Reorder alerts":
    st.markdown('<div class="topbar"><h1>Automated Reorder Alerts</h1><p>Products approaching their reorder threshold, ranked for immediate stock action.</p></div>', unsafe_allow_html=True)
    at_risk = stock[stock["stockout_risk"] == 1]
    filter_a, filter_b = st.columns([1.4, 1])
    with filter_a:
        product_search = st.text_input("Find a product", placeholder="Search by product name", key="reorder_search")
    with filter_b:
        category_filter = st.multiselect("Category", sorted(at_risk["category"].dropna().unique()), key="reorder_categories")
    if product_search:
        at_risk = at_risk[at_risk["product"].str.contains(product_search, case=False, na=False)]
    if category_filter:
        at_risk = at_risk[at_risk["category"].isin(category_filter)]
    st.markdown(f'<div class="data-hint">Showing {len(at_risk)} products requiring action. Reorder quantities come directly from the existing inventory rules.</div>', unsafe_allow_html=True)
    if at_risk.empty:
        st.markdown('<div class="empty-state">No reorder alerts match the current filters. Clear the search or category filter to see all alerts.</div>', unsafe_allow_html=True)
    for _, item in at_risk.iterrows():
        st.markdown(f'<div class="stock-card"><div><div class="product-name">{item["product"]}</div><div class="product-meta">{item["category"]} · {item["current_stock"]} units on hand · {item["days_of_stock"]} days remaining</div></div><div class="stock-action">REORDER {item["reorder_point"]} UNITS</div></div>', unsafe_allow_html=True)
    if not at_risk.empty:
        st.markdown('<div class="composition"><b>Prepare order</b><p>Select the products to order, then review and adjust the final quantities. The original recommendation remains visible for comparison.</p></div>', unsafe_allow_html=True)
        order_editor = at_risk[["product_id", "product", "category", "current_stock", "reorder_point"]].copy()
        order_editor.insert(0, "Select", False)
        order_editor["Order quantity"] = order_editor["reorder_point"].astype(int)
        edited_order = st.data_editor(order_editor, hide_index=True, use_container_width=True, disabled=["product_id", "product", "category", "current_stock", "reorder_point"], column_config={"Select": st.column_config.CheckboxColumn("Select"), "reorder_point": st.column_config.NumberColumn("Recommended"), "Order quantity": st.column_config.NumberColumn("Final quantity", min_value=1, step=1)}, key="reorder_editor")
        order_list = edited_order[edited_order["Select"]].copy()
        order_note = st.text_input("Order note", placeholder="Optional supplier or delivery instruction")
        if order_list.empty:
            st.caption("Select at least one product to prepare an order.")
        if st.button("Mark selected products as ordered", disabled=order_list.empty, use_container_width=True):
            st.session_state.reorder_history.append({"ordered_at": datetime.now().strftime("%d %b %Y, %H:%M"), "products": len(order_list), "units": int(order_list["Order quantity"].sum()), "note": order_note or "No note"})
            st.success(f"Order prepared for {len(order_list)} products and {int(order_list['Order quantity'].sum()):,} units.")
        if not order_list.empty:
            st.download_button("Download selected reorder list", order_list.drop(columns=["Select"]).to_csv(index=False), "valuemart_reorder_list.csv", "text/csv", use_container_width=True)
        if st.session_state.reorder_history:
            with st.expander(f"Recent reorder actions ({len(st.session_state.reorder_history)})"):
                st.dataframe(pd.DataFrame(st.session_state.reorder_history), hide_index=True, use_container_width=True)
else:
    st.markdown('<div class="topbar"><h1>Shelf Placement Recommendations</h1><p>Product relationships detected in customer baskets, translated into practical merchandising suggestions.</p></div>', unsafe_allow_html=True)
    filter_a, filter_b = st.columns([1.4, 1])
    with filter_a:
        pair_search = st.text_input("Find a product pair", placeholder="Search either product", key="pair_search")
    with filter_b:
        min_confidence = st.slider("Minimum confidence", 0, 100, 25, 5)
    filtered_rules = rules.copy()
    if pair_search:
        mask = filtered_rules["antecedents"].str.contains(pair_search, case=False, na=False) | filtered_rules["consequents"].str.contains(pair_search, case=False, na=False)
        filtered_rules = filtered_rules[mask]
    filtered_rules = filtered_rules[filtered_rules["confidence"] * 100 >= min_confidence].head(20)
    st.markdown(f'<div class="data-hint">Showing {len(filtered_rules)} evidence-based placement recommendations. Higher confidence means the companion item appears more consistently with the primary item.</div>', unsafe_allow_html=True)
    if filtered_rules.empty:
        st.markdown('<div class="empty-state">No product pairs match the current filters. Lower the confidence threshold or clear the search.</div>', unsafe_allow_html=True)
    else:
        pair_options = [f"{row['antecedents']} → {row['consequents']}" for _, row in filtered_rules.iterrows()]
        selected_pairs = st.multiselect("Select recommendations to action", pair_options)
        placement_status = st.selectbox("Set selected recommendations to", ["Accepted", "Implemented", "Dismissed"])
        if st.button("Update placement status", disabled=not selected_pairs, use_container_width=True):
            for pair in selected_pairs:
                st.session_state.placement_history.append({"updated_at": datetime.now().strftime("%d %b %Y, %H:%M"), "recommendation": pair, "status": placement_status})
            st.success(f"Updated {len(selected_pairs)} placement recommendations to {placement_status.lower()}.")
        if st.session_state.placement_history:
            with st.expander(f"Placement action history ({len(st.session_state.placement_history)})"):
                st.dataframe(pd.DataFrame(st.session_state.placement_history), hide_index=True, use_container_width=True)
    for _, row in filtered_rules.iterrows():
        confidence = float(row.get("confidence", 0)) * 100
        lift = float(row.get("lift", 0))
        st.markdown(f'<div class="pair-card"><div><div class="product-name">{row["antecedents"]}</div><div class="product-meta">Primary basket item</div></div><div class="pair-arrow">Place nearby<span class="evidence">{confidence:.0f}% confidence · {lift:.2f}× relationship</span></div><div class="right"><div class="product-name">{row["consequents"]}</div><div class="product-meta">Recommended companion item</div></div></div>', unsafe_allow_html=True)
st.markdown("<div style='text-align:center;color:#626b61;font-size:.64rem;padding:2rem 0 1rem'>ValueMart · Retail Intelligence · 2026</div>", unsafe_allow_html=True)
