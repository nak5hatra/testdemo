import streamlit as st
import pandas as pd
import plotly.express as px
# Code for Light and Dark Theme START

# Theme Select at start of the app
if "theme" not in st.session_state:
    st.session_state.theme = "light"

# Function to change Theme
def toggle_theme():
    if st.session_state.theme == "light":
        # Dark mode
        st._config.set_option("theme.base", "dark")
        st._config.set_option("theme.primaryColor", "#1ed760")
        st._config.set_option("theme.backgroundColor", "#2a2a2a")
        st._config.set_option("theme.secondaryBackgroundColor", "#121212")
        st._config.set_option("theme.textColor", "#ffffff")
        st._config.set_option("theme.linkColor", "#1ed760")
        st._config.set_option("theme.borderColor", "#7c7c7c")
        st._config.set_option("theme.codeBackgroundColor", "#121212")
        st.session_state.theme = "dark"
    else:
        # Light mode (your custom colors)
        st._config.set_option("theme.base", "light")
        st._config.set_option("theme.primaryColor", "#cb785c")
        st._config.set_option("theme.backgroundColor", "#fdfdf8")
        st._config.set_option("theme.secondaryBackgroundColor", "#ecebe3")
        st._config.set_option("theme.textColor", "#3d3a2a")
        st._config.set_option("theme.linkColor", "#3d3a2a")
        st._config.set_option("theme.borderColor", "#d3d2ca")
        st._config.set_option("theme.codeBackgroundColor", "#ecebe4")
        st.session_state.theme = "light"

# Theme Toggle Button
btn_label = "🌜 Switch to Dark Mode" if st.session_state.theme == "light" else "🌞 Switch to Light Mode"
_, col2 = st.columns([5, 1])
with col2:
    st.button(btn_label, on_click=toggle_theme, type="primary")
    
# Code for Light and Dark Theme END


df = pd.read_csv("./sales_data.csv")

st.set_page_config(layout="wide")
df_region_rcp = df.drop(columns=["order_date", "product", "channel", "quantity"]).groupby(by="region").sum().reset_index()


# Dataframe styling code START

if st.session_state.theme == "light":
    th_bg = "#e4e4e0"       # Light theme header
    th_color = "#3d3a2a"    # Dark text
    td_color = "#3d3a2a"
    label_color = "#3d3a2a"
else:
    th_bg = "#2a2a2a"       # Dark theme header
    th_color = "#ffffff"    # White text
    td_color = "#ffffff"
    label_color = "#ffffff"

st.markdown(f"""
<style>
/* Table header */
table th {{
    background-color: {th_bg} !important;
    color: {th_color} !important;
    font-size: 40px !important;
    text-align: center !important;
}}

/* Table cells */
table td {{
    font-size: 40px !important;
    color: {td_color} !important;
    text-align: center !important;
}}

div[data-testid="stMarkdownContainer"] p  {{
    font-size: 16px;
}}

div[data-baseweb="select"] {{
    font-size: 20px;
}}
</style>
""", unsafe_allow_html=True)

# Dataframe styling code END

st.title("ITTTM DEMO Dashboard")

option = st.selectbox(label="Select an option.",options=df_region_rcp["region"])
if option == "East":
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Revenue", df_region_rcp.iloc[[0]]["revenue"], border=True)
    with col2:
        st.metric("Cost", df_region_rcp.iloc[[0]]["cost"], border=True)
    with col3:
        st.metric("Profit", df_region_rcp.iloc[[0]]["profit"], border=True)
    fig = px.bar(df_region_rcp.iloc[[0]], x="region", y=["revenue", "cost", "profit"], barmode='group')
    st.plotly_chart(fig, use_container_width=True)
    
elif option == "North":
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Revenue", df_region_rcp.iloc[[1]]["revenue"], border=True)
    with col2:
        st.metric("Cost", df_region_rcp.iloc[[1]]["cost"], border=True)
    with col3:
        st.metric("Profit", df_region_rcp.iloc[[1]]["profit"], border=True)
    fig = px.bar(df_region_rcp.iloc[[0]], x="region", y=["revenue", "cost", "profit"], barmode='group')
    st.plotly_chart(fig, use_container_width=True)
    
elif option == "South":
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Revenue", df_region_rcp.iloc[[2]]["revenue"], border=True)
    with col2:
        st.metric("Cost", df_region_rcp.iloc[[2]]["cost"], border=True)
    with col3:
        st.metric("Profit", df_region_rcp.iloc[[2]]["profit"], border=True)
    fig = px.bar(df_region_rcp.iloc[[0]], x="region", y=["revenue", "cost", "profit"], barmode='group')
    st.plotly_chart(fig, use_container_width=True)
    
elif option == "West":
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Revenue", df_region_rcp.iloc[[3]]["revenue"], border=True)
    with col2:
        st.metric("Cost", df_region_rcp.iloc[[3]]["cost"], border=True)
    with col3:
        st.metric("Profit", df_region_rcp.iloc[[3]]["profit"], border=True)
    fig = px.bar(df_region_rcp.iloc[[0]], x="region", y=["revenue", "cost", "profit"], barmode='group')
    st.plotly_chart(fig, use_container_width=True)
    

# Complete Data Frame
st.header("Complete Data of Sales Region Wise:")
st.table(df_region_rcp)

