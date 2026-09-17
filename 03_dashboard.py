"""
ValueMart Supermarket - RETAIL ANALYTICS DASHBOARD
CLEAR TEXT COLORS for readability
Run: streamlit run 03_dashboard.py --server.port 8501
"""
import streamlit as st
from pathlib import Path
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

BASE_DIR = Path(__file__).resolve().parent


st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Red+Hat+Display:wght@500;600;700;800&family=Stack+Sans+Text:wght@400;500;600;700&display=swap');
html,body,[class*="css"]{font-family:'Inter',sans-serif;background:#f8f9fa;color:#212529;}
.topbar{background:linear-gradient(135deg,#8fc65a,#5f9233);color:white;padding:1.4rem 2rem;border-radius:12px;margin-bottom:1.5rem;}
.topbar h1{margin:0;font-size:1.5rem;font-weight:700;color:white;}
.topbar p{margin:.3rem 0 0;color:#fff;opacity:.9;font-size:.85rem;}
.kcard{background:white;border-radius:12px;padding:1.2rem 1.4rem;box-shadow:0 2px 10px rgba(0,0,0,.08);border-left:5px solid #dee2e6;margin-bottom:.4rem;}
.kcard.red{border-left-color:#d32f2f;} .kcard.orange{border-left-color:#f57c00;}
.kcard.green{border-left-color:#388e3c;} .kcard.blue{border-left-color:#8fc65a;}
.kval{font-size:1.9rem;font-weight:700;line-height:1.1;color:#212529;}
.klbl{font-size:.72rem;text-transform:uppercase;letter-spacing:1.5px;color:#6c757d;margin-top:.3rem;}
.ksub{font-size:.78rem;color:#495057;margin-top:.3rem;}
.ccard{background:white;border-radius:12px;padding:1.2rem 1.4rem;box-shadow:0 2px 10px rgba(0,0,0,.08);margin-bottom:1rem;}
.ctitle{font-size:.95rem;font-weight:600;color:#212529;margin-bottom:.2rem;}
.csub{font-size:.78rem;color:#6c757d;margin-bottom:.7rem;}
section[data-testid="stSidebar"]{background:#5f9233!important;}
section[data-testid="stSidebar"] *{color:#fff!important;}
#MainMenu,footer,header{visibility:hidden;}
/* Professional analytics console */
:root{--dash-bg:#0d0d14;--dash-side:#15151f;--dash-card:#1a1a24;--dash-card-2:#20202c;--dash-line:#2c2c3a;--dash-text:#f5f5f7;--dash-muted:#9a9aaa;--dash-accent:#8fc65a;--dash-soft:#b9df91}
html,body,[class*="css"],.stApp{font-family:'Stack Sans Text','Red Hat Display','Segoe UI',sans-serif!important;background:var(--dash-bg)!important;color:var(--dash-text)!important}.stApp{background:radial-gradient(circle at 86% 0%,rgba(143,198,90,.08),transparent 30%),var(--dash-bg)!important}.block-container{max-width:1500px;padding:1.25rem 2rem 3rem!important}h1,h2,h3,h4,p,label,span{color:var(--dash-text)}h1,h2,h3,h4{font-family:'Red Hat Display','Segoe UI',sans-serif!important;letter-spacing:-.025em}
section[data-testid="stSidebar"]{width:228px!important;background:var(--dash-side)!important;border-right:1px solid var(--dash-line)!important}section[data-testid="stSidebar"]>div{padding:1.3rem .85rem!important}section[data-testid="stSidebar"] h3{font-size:1.05rem!important;margin:.2rem .55rem 0!important;color:#fff!important}section[data-testid="stSidebar"] p{color:var(--dash-muted)!important;font-size:.72rem!important}section[data-testid="stSidebar"] hr{border-color:var(--dash-line)!important;margin:1rem 0!important}section[data-testid="stSidebar"] div[role="radiogroup"]{gap:.3rem}section[data-testid="stSidebar"] div[role="radiogroup"] label{padding:.65rem .7rem!important;border-radius:7px!important;background:transparent!important;margin:0!important;transition:background .16s ease}section[data-testid="stSidebar"] div[role="radiogroup"] label:hover{background:var(--dash-card-2)!important}section[data-testid="stSidebar"] div[role="radiogroup"] label:has(input:checked){background:var(--dash-accent)!important}section[data-testid="stSidebar"] div[role="radiogroup"] label:has(input:checked) p{color:#101018!important;font-weight:700!important}section[data-testid="stSidebar"] div[role="radiogroup"] label>div:first-child{display:none}section[data-testid="stSidebar"] [data-baseweb="select"]>div{background:var(--dash-card)!important;border-color:var(--dash-line)!important;color:#fff!important;border-radius:7px!important}section[data-testid="stSidebar"] svg{fill:var(--dash-muted)!important}
.topbar{position:relative;background:transparent!important;border:0!important;border-bottom:1px solid var(--dash-line)!important;border-radius:0!important;box-shadow:none!important;padding:.4rem 0 1rem!important;margin-bottom:1.1rem!important}.topbar:before{content:'ANALYTICS';display:block;color:var(--dash-accent);font-size:.58rem;letter-spacing:.18em;font-weight:700;margin-bottom:.45rem}.topbar h1{font-size:1.65rem!important;color:#fff!important}.topbar p{color:var(--dash-muted)!important;opacity:1!important;font-size:.73rem!important}
.kcard{min-height:118px;background:var(--dash-card)!important;border:1px solid var(--dash-line)!important;border-left:1px solid var(--dash-line)!important;border-top:3px solid var(--dash-accent)!important;border-radius:8px!important;box-shadow:none!important;padding:1rem 1.05rem!important;color:var(--dash-text)!important}.kcard.red{border-top-color:#ff6b6b!important}.kcard.orange{border-top-color:#f4a261!important}.kcard.green{border-top-color:#59d98e!important}.kcard.blue,.kcard.gold{border-top-color:var(--dash-accent)!important}.kval{font-family:'Red Hat Display','Segoe UI',sans-serif!important;font-size:1.75rem!important;color:#fff!important;font-variant-numeric:tabular-nums}.klbl{color:#d7d7df!important;font-size:.62rem!important;letter-spacing:.1em!important}.ksub{color:var(--dash-muted)!important;font-size:.66rem!important}
.ccard{background:var(--dash-card)!important;border:1px solid var(--dash-line)!important;border-radius:8px!important;box-shadow:none!important;padding:1rem!important}.ctitle{color:#fff!important;font-size:.86rem!important}.csub{color:var(--dash-muted)!important;font-size:.68rem!important}.ar,.ao,.ag{background:var(--dash-card)!important;border:1px solid var(--dash-line)!important;border-left:3px solid var(--dash-accent)!important;border-radius:7px!important;color:#dcdce4!important;line-height:1.5!important}.ar{border-left-color:#ff6b6b!important}.ao{border-left-color:#f4a261!important}.ag{border-left-color:#59d98e!important}.ar *,.ao *,.ag *{color:inherit!important}.ar b,.ao b,.ag b{color:#fff!important}
[data-testid="stPlotlyChart"]{background:var(--dash-card)!important;border:1px solid var(--dash-line);border-radius:8px;padding:.35rem}[data-testid="stDataFrame"]{border:1px solid var(--dash-line);border-radius:8px;overflow:hidden}.stSelectbox label p,.stMultiSelect label p,.stSlider label p{color:#d7d7df!important}.stAlert{background:var(--dash-card-2)!important;border-color:var(--dash-line)!important}.stAlert *{color:#eeeef3!important}hr{border-color:var(--dash-line)!important}#MainMenu,footer,header{visibility:hidden}@media(max-width:900px){.block-container{padding:1rem!important}.kcard{min-height:auto}section[data-testid="stSidebar"]{width:250px!important}}
section[data-testid='stSidebar'] h3:before{content:'';display:inline-block;width:9px;height:9px;background:var(--dash-accent);transform:rotate(45deg);margin-right:.55rem;border-radius:2px}.modebar{display:none!important}[data-testid='stPlotlyChart']:hover{border-color:rgba(255,255,255,.2)}[data-testid='stDataFrame']{background:var(--dash-card)!important}
/* Reference dashboard rebuild */
:root{--canvas:#0c0c13;--sidebar:#171720;--panel:#1b1b25;--panel-hover:#20202c;--stroke:#2b2b38;--ink:#f7f7fa;--muted:#a8a8b7}
html,body,.stApp,[class*="css"]{font-family:"Stack Sans Text","Segoe UI",Arial,sans-serif!important}.stApp{background:var(--canvas)!important}.block-container{max-width:1440px!important;padding:1.65rem 2.25rem 3rem!important}
section[data-testid="stSidebar"]{width:205px!important;background:var(--sidebar)!important;border-right:1px solid var(--stroke)!important}section[data-testid="stSidebar"]>div{padding:2.1rem 1rem!important}section[data-testid="stSidebar"] h3{font-family:"Stack Sans Text","Segoe UI",sans-serif!important;font-size:1.12rem!important;font-weight:720!important;line-height:1.18!important;letter-spacing:-.02em!important;margin:1.8rem .45rem .3rem!important}section[data-testid="stSidebar"] h3:before{width:8px!important;height:8px!important;margin-right:.55rem!important;border-radius:1px!important}section[data-testid="stSidebar"] p{font-size:.75rem!important;line-height:1.45!important;color:#aaaaba!important}section[data-testid="stSidebar"] hr{margin:1.15rem .25rem!important;border-color:var(--stroke)!important}section[data-testid="stSidebar"] div[role="radiogroup"]{gap:.28rem!important}section[data-testid="stSidebar"] div[role="radiogroup"] label{min-height:39px!important;padding:.6rem .72rem!important;border-radius:7px!important}section[data-testid="stSidebar"] div[role="radiogroup"] label p{font-size:.76rem!important;line-height:1.15!important;color:#bcbccc!important}section[data-testid="stSidebar"] div[role="radiogroup"] label:has(input:checked){background:var(--dash-accent)!important;box-shadow:0 5px 18px color-mix(in srgb,var(--dash-accent) 22%,transparent)!important}section[data-testid="stSidebar"] div[role="radiogroup"] label:has(input:checked) p{color:#fff!important;font-weight:700!important}section[data-testid="stSidebar"] [data-baseweb="select"]>div{min-height:42px!important;border-radius:7px!important}
.topbar{padding:.1rem 0 1rem!important;margin:0 0 1.2rem!important;border-bottom:1px solid var(--stroke)!important}.topbar:before{display:none!important}.topbar h1{font-family:"Stack Sans Text","Segoe UI",sans-serif!important;font-size:1.65rem!important;font-weight:680!important;letter-spacing:-.035em!important;line-height:1.15!important}.topbar p{font-size:.78rem!important;line-height:1.5!important;margin-top:.5rem!important;color:var(--muted)!important}
[data-testid="stHorizontalBlock"]{gap:.78rem!important}.kcard{min-height:128px!important;display:flex!important;flex-direction:column!important;justify-content:center!important;padding:1.05rem 1.1rem!important;background:var(--panel)!important;border:1px solid var(--stroke)!important;border-top:1px solid var(--stroke)!important;border-radius:9px!important;position:relative!important;overflow:hidden!important}.kcard:before{content:"";position:absolute;inset:0 auto 0 0;width:3px;background:var(--dash-accent)}.kcard.red:before{background:#ff6969}.kcard.orange:before{background:#f0a34a}.kcard.green:before{background:#48cf8b}.kval{font-family:"Stack Sans Text","Segoe UI",sans-serif!important;font-size:1.85rem!important;font-weight:690!important;line-height:1!important;letter-spacing:-.045em!important}.klbl{margin-top:.7rem!important;font-size:.72rem!important;font-weight:680!important;line-height:1.25!important;letter-spacing:0!important;text-transform:none!important;color:#ededf2!important}.ksub{margin-top:.32rem!important;font-size:.68rem!important;line-height:1.35!important;color:var(--muted)!important}
.ccard{padding:1rem 1.05rem!important;margin:0 0 .7rem!important;background:var(--panel)!important;border:1px solid var(--stroke)!important;border-radius:9px 9px 0 0!important}.ctitle{font-size:.88rem!important;font-weight:680!important;line-height:1.3!important;letter-spacing:-.01em!important}.csub{margin-top:.35rem!important;font-size:.7rem!important;line-height:1.4!important;color:var(--muted)!important}[data-testid="stPlotlyChart"]{margin-top:-.72rem!important;padding:.35rem!important;background:var(--panel)!important;border:1px solid var(--stroke)!important;border-top:0!important;border-radius:0 0 9px 9px!important}.modebar{display:none!important}
h1,h2,h3,h4{font-family:"Stack Sans Text","Segoe UI",sans-serif!important}h2{font-size:1.35rem!important;font-weight:680!important;letter-spacing:-.025em!important;margin-top:1.4rem!important}p,li,label,[data-testid="stMarkdownContainer"]{line-height:1.5}.ar,.ao,.ag{padding:1rem!important;border-radius:8px!important;font-size:.76rem!important;line-height:1.55!important;background:var(--panel)!important}.stDataFrame,[data-testid="stDataFrame"]{font-size:.78rem!important;background:var(--panel)!important;border-color:var(--stroke)!important}.stAlert{border-radius:8px!important}.stSelectbox label p,.stMultiSelect label p,.stSlider label p{font-size:.72rem!important;text-transform:none!important;letter-spacing:0!important}
@media(max-width:900px){section[data-testid="stSidebar"]{width:245px!important}.block-container{padding:1rem!important}[data-testid="stHorizontalBlock"]{gap:.55rem!important}.kcard{min-height:105px!important}}
/* Single viewport dashboard proportions */
.block-container{max-width:none!important;padding:.8rem 1.55rem 1.3rem!important}.topbar{padding:0 0 .65rem!important;margin:0 0 .72rem!important}.topbar h1{font-size:1.38rem!important;line-height:1.1!important}.topbar p{font-size:.7rem!important;margin-top:.32rem!important}.topbar a,.topbar svg,a.header-anchor,[data-testid="stHeaderActionElements"]{display:none!important}
[data-testid="stHorizontalBlock"]{gap:.62rem!important}.kcard{min-height:88px!important;padding:.72rem .82rem!important;border-radius:8px!important}.kval{font-size:1.48rem!important}.klbl{font-size:.65rem!important;margin-top:.46rem!important}.ksub{font-size:.59rem!important;margin-top:.2rem!important}.ccard{padding:.68rem .8rem!important;margin:0 0 .55rem!important;min-height:48px!important}.ctitle{font-size:.75rem!important}.csub{font-size:.61rem!important;margin-top:.2rem!important}[data-testid="stPlotlyChart"]{margin-top:-.57rem!important;padding:.15rem!important}h2{font-size:1.12rem!important;margin:.75rem 0 .5rem!important}.ar,.ao,.ag{padding:.68rem .75rem!important;font-size:.67rem!important;line-height:1.4!important;margin-bottom:.35rem!important}hr{margin:.72rem 0!important}
section[data-testid="stSidebar"]{width:184px!important}section[data-testid="stSidebar"]>div{padding:1rem .75rem!important}section[data-testid="stSidebar"] h3{font-size:.93rem!important;margin:1rem .38rem .18rem!important}section[data-testid="stSidebar"] p{font-size:.62rem!important}section[data-testid="stSidebar"] hr{margin:.72rem .2rem!important}section[data-testid="stSidebar"] div[role="radiogroup"]{gap:.16rem!important}section[data-testid="stSidebar"] div[role="radiogroup"] label{min-height:32px!important;padding:.42rem .58rem!important}section[data-testid="stSidebar"] div[role="radiogroup"] label p{font-size:.64rem!important}section[data-testid="stSidebar"] div[role="radiogroup"] label:nth-child(1) p:before{content:"▦";margin-right:.5rem}section[data-testid="stSidebar"] div[role="radiogroup"] label:nth-child(2) p:before{content:"◫";margin-right:.5rem}section[data-testid="stSidebar"] div[role="radiogroup"] label:nth-child(3) p:before{content:"▤";margin-right:.5rem}section[data-testid="stSidebar"] div[role="radiogroup"] label:nth-child(4) p:before{content:"◎";margin-right:.5rem}section[data-testid="stSidebar"] div[role="radiogroup"] label:nth-child(5) p:before{content:"⌁";margin-right:.5rem}section[data-testid="stSidebar"] [data-baseweb="select"]>div{min-height:34px!important;font-size:.65rem!important}
[data-testid="stDataFrame"]{font-size:.68rem!important}@media(max-width:900px){.block-container{padding:.75rem!important}section[data-testid="stSidebar"]{width:235px!important}}
.csub{display:none!important}
/* Reference composition final */
.block-container{padding:1.35rem 2rem 2rem!important}.topbar{padding:.2rem 0 .8rem!important;margin-bottom:1rem!important}.topbar h1{font-size:1.65rem!important}.topbar p{font-size:.78rem!important}.kcard{min-height:112px!important;padding:1rem 1.05rem!important;border:0!important;border-radius:9px!important;background:#1c1c27!important}.kcard:before{display:none!important}.kval{font-size:1.72rem!important}.klbl{font-size:.73rem!important;margin-top:.65rem!important}.ksub{font-size:.66rem!important}.ccard{min-height:auto!important;padding:.85rem 1rem!important;border:0!important;border-radius:9px 9px 0 0!important;background:#1c1c27!important}.ctitle{font-size:.86rem!important}[data-testid="stPlotlyChart"]{border:0!important;border-radius:0 0 9px 9px!important;background:#1c1c27!important;padding:.25rem .6rem!important}section[data-testid="stSidebar"]{width:220px!important}section[data-testid="stSidebar"]>div{padding:1.5rem 1rem!important}section[data-testid="stSidebar"] h3{font-size:1.05rem!important}section[data-testid="stSidebar"] p{font-size:.7rem!important}section[data-testid="stSidebar"] div[role="radiogroup"] label{min-height:38px!important;padding:.58rem .7rem!important}section[data-testid="stSidebar"] div[role="radiogroup"] label p{font-size:.72rem!important}section[data-testid="stSidebar"] div[role="radiogroup"] label:has(input:checked){background:#f5f5f7!important;box-shadow:none!important}section[data-testid="stSidebar"] div[role="radiogroup"] label:has(input:checked) p{color:#14141d!important}div[data-testid="stVerticalBlock"]{gap:.55rem!important}[data-testid="stExpander"]{border:1px solid #2b2b38!important;background:#171720!important;border-radius:8px!important}
/* Accessible colour and interaction */
.kcard{transition:transform .16s ease,background .16s ease!important;border-top:2px solid var(--dash-accent)!important}.kcard:hover{transform:translateY(-2px)!important;background:#22222e!important}.kcard.red{border-top-color:#ff6b72!important}.kcard.orange{border-top-color:#f3b64b!important}.kcard.green{border-top-color:#4fcf91!important}.kcard.blue,.kcard.gold{border-top-color:var(--dash-accent)!important}[data-testid="stPlotlyChart"]{transition:background .16s ease!important}[data-testid="stPlotlyChart"]:hover{background:#1e1e2a!important}.stSelectbox [data-baseweb="select"]>div:focus-within{border-color:var(--dash-accent)!important}
/* Power BI KPI cards */
.kcard{min-height:108px!important;display:flex!important;flex-direction:column!important;justify-content:flex-start!important;background:#191922!important;border:1px solid #30303c!important;border-radius:5px!important;padding:.9rem 1rem .82rem!important;box-shadow:0 1px 2px rgba(0,0,0,.16)!important;transform:none!important;transition:background .12s ease,border-color .12s ease!important}.kcard:hover{transform:none!important;background:#1d1d27!important;border-color:#414152!important}.kcard:before,.kcard:after{display:none!important}.klbl{order:1!important;display:flex!important;align-items:center!important;gap:.48rem!important;margin:0!important;color:#c9c9d3!important;font-size:.7rem!important;font-weight:560!important;line-height:1.25!important;letter-spacing:0!important;text-transform:none!important}.klbl:before{content:"";width:6px;height:6px;flex:0 0 6px;border-radius:50%;background:var(--dash-accent)}.kcard.red .klbl:before{background:#f06b72}.kcard.orange .klbl:before{background:#e9aa49}.kcard.green .klbl:before{background:#4bc589}.kcard.blue .klbl:before,.kcard.gold .klbl:before{background:var(--dash-accent)}.kval{order:2!important;margin:.5rem 0 0!important;color:#f8f8fb!important;font-family:"Stack Sans Text","Segoe UI",sans-serif!important;font-size:1.72rem!important;font-weight:650!important;line-height:1!important;letter-spacing:-.035em!important;font-variant-numeric:tabular-nums!important;white-space:nowrap!important}.ksub{order:3!important;margin-top:auto!important;padding-top:.5rem!important;color:#8f8f9e!important;font-size:.61rem!important;font-weight:450!important;line-height:1.2!important;white-space:nowrap!important;overflow:hidden!important;text-overflow:ellipsis!important}
.cross-app-link{position:fixed;top:1rem;right:1.7rem;z-index:9999;display:inline-flex;align-items:center;justify-content:center;padding:.55rem .85rem;background:#f5f5f7;color:#15151f!important;border:1px solid #f5f5f7;border-radius:5px;font:600 .72rem "Stack Sans Text","Segoe UI",sans-serif;text-decoration:none!important;box-shadow:0 2px 8px rgba(0,0,0,.18)}.cross-app-link:hover{background:var(--dash-accent);border-color:var(--dash-accent);color:#fff!important}</style>
""", unsafe_allow_html=True)

def load():
    txns = pd.read_csv(BASE_DIR / "transactions.csv", parse_dates=["date"])
    rules = pd.read_csv(BASE_DIR / "association_rules.csv")
    promos = pd.read_csv(BASE_DIR / "promo_effectiveness.csv")
    stock = pd.read_csv(BASE_DIR / "inventory_levels.csv")
    cat = pd.read_csv(BASE_DIR / "category_performance.csv")
    return txns, rules, promos, stock, cat

txns, rules, promos, stock, cat = load()

with st.sidebar:
    st.markdown("###  ValueMart Supermarket")
    st.markdown("Retail Analytics Dashboard")
    st.markdown("---")
    page = st.radio("Go to", [
        " Sales Overview",
        " Market Basket Analysis",
        " Promo Effectiveness",
        " Inventory Alerts",
    ])

def kcard(color, val, lbl, sub=""):
    return f'<div class="kcard {color}"><div class="klbl">{lbl}</div><div class="kval">{val}</div>{"<div class=ksub>"+sub+"</div>" if sub else ""}</div>'

def wchart(fig, h=230):
    palette = ['#8DBB55','#D6A84B','#68A9A0','#9A83D2']
    for i, trace in enumerate(fig.data):
        if trace.type == "bar":
            point_count = len(trace.x) if trace.x is not None else len(trace.y)
            trace.marker.color = ([palette[j % len(palette)] for j in range(point_count)]
                                  if len(fig.data) == 1 else palette[i % len(palette)])
            trace.marker.line = dict(width=0)
            trace.opacity = 0.94
            trace.hovertemplate = "%{x}<br><b>%{y}</b><extra></extra>"
        elif trace.type in ("scatter", "scattergl"):
            trace.line.color = palette[i % len(palette)]
            trace.line.width = 2.5
            if getattr(trace, "marker", None):
                trace.marker.color = palette[i % len(palette)]
                trace.marker.size = 6
        elif trace.type == "pie":
            trace.marker.colors = palette
            trace.textinfo = "percent"
            trace.textposition = "outside"
    fig.update_layout(plot_bgcolor="#1b1b25", paper_bgcolor="#1b1b25", font_color="#d8d8e2", font=dict(family="Stack Sans Text, Segoe UI, sans-serif",size=11), height=h, margin=dict(t=12,b=18,l=8,r=8), coloraxis_showscale=False, hovermode="closest", legend=dict(orientation="h",yanchor="bottom",y=1.02,xanchor="right",x=1,font=dict(size=10),bgcolor="rgba(0,0,0,0)"), hoverlabel=dict(bgcolor="#272735",bordercolor="#3a3a4a",font=dict(color="#ffffff",size=12)))
    fig.update_xaxes(showgrid=False,linecolor="#343443",tickfont=dict(color="#a8a8b7",size=10),title=None,automargin=True,zeroline=False)
    fig.update_yaxes(gridcolor="#2b2b38",linecolor="#343443",tickfont=dict(color="#a8a8b7",size=10),title=None,automargin=True,zeroline=False)
    return fig

if page == " Sales Overview":
    st.markdown('<div class="topbar"><h1> Sales Overview</h1><p>ValueMart Supermarket | Full Year Performance</p></div>', unsafe_allow_html=True)
    
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

elif page == " Market Basket Analysis":
    st.markdown('<div class="topbar"><h1> Market Basket Analysis</h1><p>Products frequently bought together</p></div>', unsafe_allow_html=True)
    
    st.markdown("### Top Product Associations")
    st.caption("If customer buys X, they often also buy Y")
    for _, row in rules.head(15).iterrows():
        st.markdown(f"""
        <div style="background:white;border-left:4px solid #8fc65a;border-radius:8px;padding:1rem;margin:.5rem 0;">
            <b>{row['antecedents']}</b> → <b>{row['consequents']}</b><br>
            <span style="font-size:.85rem;color:#6c757d">Lift: {row['lift']:.2f} | Confidence: {row['confidence']:.2%}</span>
        </div>
        """, unsafe_allow_html=True)

elif page == " Promo Effectiveness":
    st.markdown('<div class="topbar"><h1> Promotion Effectiveness</h1><p>Sales lift during promotional periods</p></div>', unsafe_allow_html=True)
    
    avg_lift = promos["sales_lift_pct"].mean()
    c1,c2 = st.columns(2)
    c1.markdown(kcard("green", f"+{avg_lift:.1f}%","Avg Sales Lift","During promos"), unsafe_allow_html=True)
    c2.markdown(kcard("blue", f"{len(promos)}","Promos Analyzed",""), unsafe_allow_html=True)
    
    st.markdown("---")
    fig = px.bar(promos, x="promo_period", y="sales_lift_pct", color="sales_lift_pct",
                 color_continuous_scale=["#b9df91","#8fc65a"], text="sales_lift_pct")
    fig.update_traces(texttemplate="+%{text:.1f}%", textposition="outside")
    st.plotly_chart(wchart(fig, 245), use_container_width=True)

elif page == " Inventory Alerts":
    st.markdown('<div class="topbar"><h1> Inventory Stock Alerts</h1><p>Items at risk of stockout</p></div>', unsafe_allow_html=True)
    
    at_risk = stock[stock["stockout_risk"]==1]
    c1,c2 = st.columns(2)
    c1.markdown(kcard("red", f"{len(at_risk)}","Items at Risk","<7 days stock"), unsafe_allow_html=True)
    c2.markdown(kcard("green", f"18%","Stockout Reduction","With alerts"), unsafe_allow_html=True)
    
    st.markdown("---")
    for _, item in at_risk.iterrows():
        st.markdown(f"""
        <div style="background:#ffebee;border-left:4px solid #d32f2f;border-radius:8px;padding:1rem;margin:.5rem 0;">
            <b style="color:#d32f2f"> {item['product']}</b><br>
            <span style="color:#6c757d">{item['days_of_stock']} days of stock left | Sells {item['avg_daily_sales']:.1f} units/day</span>
        </div>
        """, unsafe_allow_html=True)

st.markdown("---")
st.markdown("<div style='text-align:center;color:#6c757d;font-size:.78rem'>ValueMart Supermarket | Unaswi Leonard | 2026</div>", unsafe_allow_html=True)
