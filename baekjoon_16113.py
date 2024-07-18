N = int(input())
Signal = input()
col = N // 5
signal = [[0 for _ in range(5)] for _ in range(col)]

tmp = 0
ans = ''
for i in range(5):
    for j in range(col):
        if (Signal[tmp] == '#'):
            signal[j][i] = 1
        else:
            signal[j][i] = 0
        tmp += 1
emptyrule = [0, 0, 0, 0, 0]
z = 0
while (z < col):
    if (signal[z] == emptyrule):
        z += 1
    elif (signal[z] == [1, 1, 1, 1, 1]):  # 0,1,6,8
        if (z + 1 >= col):
            ans += '1'
            z += 2
        elif (signal[z + 1] == emptyrule):  # 1
            ans += '1'
            z += 2
        elif (signal[z + 1] == [1, 0, 0, 0, 1]):  # 0
            ans += '0'
            z += 3

        elif (signal[z + 2] == [1, 0, 1, 1, 1]):  # 6
            ans += '6'
            z += 3

        else:  # 8
            ans += '8'
            z += 3
    elif (signal[z] == [1, 1, 1, 0, 1]):  # 5,9
        if (signal[z + 2] == [1, 0, 1, 1, 1]):
            ans += '5'
            z += 3
        else:
            ans += '9'
            z += 3
    elif (signal[z] == [1, 0, 1, 1, 1]):  # 2
        ans += '2'
        z += 3
    elif (signal[z] == [1, 0, 1, 0, 1]):  # 3
        ans += '3'
        z += 3
    elif (signal[z] == [1, 1, 1, 0, 0]):  # 4
        ans += '4'
        z += 3
    elif (signal[z] == [1, 0, 0, 0, 0]):  # 7
        ans += '7'
        z += 3

print(''.join(ans))