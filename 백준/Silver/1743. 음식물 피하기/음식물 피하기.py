import sys
sys.setrecursionlimit(100000)

n, m, k = map(int, input().split())

arr = [[0] * m for _ in range(n)]

for i in range (k):
    r,c = map(int, input().split())
    #print(r,c)
    arr[r-1][c-1] = 1
#print(arr)

max_cnt = 0

def find_food(x, y, cnt):
    #print("find_food", x,y,cnt)
    
    #위쪽
    if x-1>=0 and arr[x-1][y] == 1: #위쪽 방향으로 다녀간 적이 없는 음식물이 있으면
        #print("위쪽")
        arr[x-1][y] = 2 #다녀갔다고 표시
        cnt = find_food(x-1, y, cnt+1)
    #오른쪽
    if y+1<m and arr[x][y+1] == 1: #오른쪽 방향으로 다녀간 적이 없는 음식물이 있으면
        #print("오른쪽")
        arr[x][y+1] = 2 #다녀갔다고 표시
        cnt = find_food(x,y+1, cnt+1)
    #아래쪽
    if x+1<n and arr[x+1][y] == 1: #아래쪽 방향으로 다녀간 적이 없는 음식물이 있으면
        #print("아래쪽")
        arr[x+1][y] = 2 #다녀갔다고 표시
        cnt = find_food(x+1,y, cnt+1)
    #왼쪽
    if y-1>=0 and arr[x][y-1] == 1: #왼쪽 방향으로 다녀간 적이 없는 음식물이 있으면
        #print("왼쪽")
        arr[x][y-1] = 2 #다녀갔다고 표시
        cnt = find_food(x,y-1, cnt+1)

    return(cnt)

for i in range(n):
    for j in range(m):
        if arr[i][j]==1: #음식물이 있으면
            arr[i][j] = 2 #다녀갔다고 표시
            count = find_food(i,j,1)
            #print(i,j,count)
            if max_cnt<count :
                max_cnt = count

print(max_cnt)
