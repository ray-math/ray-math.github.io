import numpy as np
from scipy.optimize import linprog

# 목표 함수의 계수
c = np.array([-3000, -2000, -4000])

# 제약 조건의 계수
A = np.array([[3, 2, 4], [4, 1, 3], [2, 3, 2]])

# 제약 조건의 오른쪽 값
b = np.array([100, 120, 80])

# 변수의 범위
x0_bounds = (0, None)
x1_bounds = (0, None)
x2_bounds = (0, None)

# linprog 함수 호출
res = linprog(c, A_ub=A, b_ub=b, bounds=[x0_bounds, x1_bounds, x2_bounds], method='highs')

print('Optimal value:', -res.fun, '\nX:', res.x)
