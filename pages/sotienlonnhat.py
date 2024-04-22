import streamlit as st
import numpy as np
from scipy.optimize import linprog

st.title("Bài toán tối ưu hóa sản xuất bàn ghế")

# Input parameters
assembly_time_table = st.number_input("Số giờ lắp ráp của bàn", value=1.5)
finishing_time_table = st.number_input("Số giờ hoàn thiện của bàn", value=1.0)
assembly_time_chair = st.number_input("Số giờ lắp ráp của ghế", value=1.0)
finishing_time_chair = st.number_input("Số giờ hoàn thiện của ghế", value=2.0)
num_workers_assembly = st.number_input("Số công nhân của bộ phận lắp ráp", value=3)
num_workers_finishing = st.number_input("Số công nhân của bộ phận hoàn thiện", value=4)
profit_table = st.number_input("Số tiền lãi của bàn (nghìn đồng)", value=600)
profit_chair = st.number_input("Số tiền lãi của ghế (nghìn đồng)", value=450)

# Define coefficients of objective function
c = np.array([-profit_table, -profit_chair])  # Negative because linprog minimizes by default

# Define coefficients of inequality constraints
A_ub = np.array([
    [assembly_time_table, assembly_time_chair],
    [finishing_time_table, finishing_time_chair],
    [0, -1],
    [-3.5, 1],
    [-1, 0]
]) * num_workers_assembly  # Scaling by the number of workers in assembly

b_ub = np.array([24 * num_workers_assembly, 24 * num_workers_finishing, 0, 0, 0])  # Number of hours constraint, chair consumption constraint, non-negativity constraint

# Button to execute the program
if st.button("Tính toán"):
    # Solve the linear programming problem
    result = linprog(c, A_ub=A_ub, b_ub=b_ub, bounds=[(0, None), (0, None)], method='highs')

    # Display the results
    if result.success:
        optimal_profit = -result.fun * 1000  # Scaling back to đồng
        st.write("Doanh thu tối đa:", optimal_profit, "(đồng)")
        st.write("Số lượng bàn(x) tối ưu:", int(result.x[0]))
        st.write("Số lượng ghế(y) tối ưu:", int(result.x[1]))
    else:
        st.write("Không tìm được giải pháp tối ưu")