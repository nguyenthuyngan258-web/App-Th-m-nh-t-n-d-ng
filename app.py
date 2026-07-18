import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# Cấu hình Page
st.set_page_config(page_title="CreditAnalyzer Premium", layout="wide")

# CSS "WOW" Effect: Bo góc, đổ bóng, animation và font chữ hiện đại
st.markdown("""
    <style>
    .big-font {font-size: 24px !important; font-weight: bold; color: #1e3d59;}
    .css-card {background-color: #ffffff; padding: 25px; border-radius: 20px; box-shadow: 0 4px 20px rgba(0,0,0,0.1); margin-bottom: 20px;}
    .stButton>button {width: 100%; border-radius: 10px; background-color: #ff6e40; color: white; font-weight: bold; height: 50px;}
    .stSelectbox, .stNumberInput {border-radius: 10px !important;}
    </style>
""", unsafe_allow_html=True)

# Header
st.markdown("<h1 style='text-align: center; color: #1e3d59;'>🚀 CREDIT ANALYZER PREMIUM</h1>", unsafe_allow_html=True)

# Chia layout thành 2 phần chính
main_col, side_col = st.columns([2, 1])

with main_col:
    with st.container():
        st.markdown("<div class='css-card'>", unsafe_allow_html=True)
        st.subheader("📋 Nhập thông tin chi tiết")
        c1, c2 = st.columns(2)
        with c1:
            so_tien_vay = st.number_input("Số tiền vay (VNĐ)", 0, 10000000000, 500000000)
            thu_nhap = st.number_input("Thu nhập hàng tháng (VNĐ)", 0, 1000000000, 20000000)
            gia_tri_tsdb = st.number_input("Giá trị TSĐB (VNĐ)", 0, 10000000000, 1000000000)
        with c2:
            thoi_han = st.slider("Thời gian vay (tháng)", 6, 360, 60)
            lai_suat = st.number_input("Lãi suất (%/năm)", 0.0, 30.0, 10.0)
            cic_score = st.selectbox("Điểm tín dụng CIC", ["Nhóm 1 - Tốt", "Nhóm 2 - Cần lưu ý", "Nhóm 3+ - Rủi ro"])
        st.markdown("</div>", unsafe_allow_html=True)

with side_col:
    st.markdown("<div class='css-card'>", unsafe_allow_html=True)
    st.subheader("💡 Chỉ số nhanh")
    du_no_cu = st.number_input("Dư nợ khoản vay cũ (VNĐ)", 0)
    if st.button("TÍNH TOÁN NGAY"):
        # Logic tính toán
        goc_lai = (so_tien_vay / thoi_han) + (so_tien_vay * (lai_suat/100/12))
        dti = ((du_no_cu + goc_lai) / (thu_nhap + 1)) * 100
        ltv = (so_tien_vay / (gia_tri_tsdb + 1)) * 100
        
        # Hiển thị chỉ số
        st.metric("DTI Ratio", f"{dti:.2f}%")
        st.metric("LTV Ratio", f"{ltv:.2f}%")
        st.write(f"Kết luận: **{'ĐẠT' if dti < 40 else 'CẢNH BÁO'}**")
    st.markdown("</div>", unsafe_allow_html=True)

# Phần biểu đồ "WOW"
st.subheader("📈 Phân tích rủi ro trực quan")
fig = go.Figure(go.Indicator(
    mode="gauge+number", value=45,
    gauge={'axis': {'range': [0, 100]}, 'bar': {'color': "#1e3d59"}, 'steps': [{'range': [0, 40], 'color': "#00c853"}, {'range': [40, 70], 'color': "#ffd600"}]}))
st.plotly_chart(fig, use_container_width=True)
