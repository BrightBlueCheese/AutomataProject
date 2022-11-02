import numpy as np

cell_one = [_ for _ in range(1,4)]
cell_1t9 = []
for i in range(3):
    ma_list = []
    for j in cell_one:
        ma_list.append(j + 3*i )
    cell_1t9.append(ma_list)

ma_mat = np.array(cell_1t9)
print(ma_mat)

print(ma_mat[1,1])

for row, col in np.ndindex(ma_mat.shape):
    if row-1 < 1 or col < -1 :
        pass


ma_list = [_ for _ in range(10)]
print(ma_list[9:0])

print(len)

# cell_zeros = np.zeros((6,6))



# cells = [[0, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, 0]]

# cells = np.array(cells)

# print(cells)

# for row, col in np.ndindex(cells.shape):
#     # print(row, col)
#     if 