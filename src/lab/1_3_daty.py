data1 = (1, 4, 2020)
data2 = (3, 4, 2020)

ktora = 0

if data1[2] < data2[2]:
    ktora = 1
elif data1[2] > data2[2]:
    ktora = 2
elif data1[1] < data2[1]:
    ktora = 1
elif data1[1] > data2[1]:
    ktora = 2
elif data1[0] < data2[0]:
    ktora = 1
elif data1[0] > data2[0]:
    ktora = 2
else:
    ktora = 0

print(ktora)

newdata1 = (data1[2], data1[1], data1[0])
newdata2 = (data2[2], data2[1], data2[0])

print(newdata1 < newdata2)

data1_int = data1[0] + data1[1]*100 + data1[2] * 100 * 100
data2_int = data2[0] + data2[1]*100 + data2[2] * 100 * 100

print(data1_int, data2_int, data1_int < data2_int)