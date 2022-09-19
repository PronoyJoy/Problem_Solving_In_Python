
inputs = list(map(int,input().split()))
N_ROW = inputs[0]
M_COL = inputs[1]



for i in range(N_ROW):
    if i%2 != 0:
        print(('.|.'*i).center(M_COL,'-'))
print("WELCOME".center(M_COL,'-'))

for j in range(N_ROW-1,0,-1):
    if j%2 != 0:
        print(('.|.'*j).center(M_COL,'-'))