import streamlit as st
import math

def tinh_lai_kep(P, r, n, t):
  """
  Tính số tiền thu được sau n kì tính lãi trong t năm với lãi suất kép theo định kì

  Args:
    P: Số tiền vốn ban đầu
    r: Lãi suất năm (số thập phân)
    n: Số kì tính lãi trong một năm
    t: Số năm gửi tiết kiệm

  Returns:
    Số tiền thu được sau n kì tính lãi trong t năm
  """
  A = P * (1 + r / n) ** (n * t)
  return A

st.title("Tính lãi kép")

# Ô input cho số tiền vốn ban đầu
P = st.number_input("Số tiền vốn ban đầu (triệu đồng)", value=120,min_value=0)

# Ô input cho lãi suất năm
r = st.number_input("Lãi suất năm (%)", min_value=0, value=6,max_value=100) / 100

# Ô input cho số kì tính lãi trong một năm
n = st.number_input("Số kì tính lãi trong một năm", value=4,min_value=1)

# Ô input cho số năm gửi tiết kiệm
t = st.number_input("Số năm gửi tiết kiệm", value=5,min_value=1)

# Button để tính toán
if st.button("Tính toán"):
  # Tính toán số tiền thu được
  A_quy = tinh_lai_kep(P, r, 4, t)
  A_thang = tinh_lai_kep(P, r, 12, t)
  A_lien_tuc = P * math.exp(r * t)

  # Hiển thị kết quả
  st.write(f"Số tiền thu được sau 5 năm gửi tiết kiệm lãi kép hàng quý: {A_quy:.2f} triệu đồng")
  st.write(f"Số tiền thu được sau 5 năm gửi tiết kiệm lãi kép hàng tháng: {A_thang:.2f} triệu đồng")
  st.write(f"Số tiền thu được sau 5 năm gửi tiết kiệm lãi kép liên tục: {A_lien_tuc:.2f} triệu đồng")
