from collections import deque


n, m = map(int, input().split())

matrix = [list(map(int, input().strip())) for _ in range(n)]

queue = deque([(0,0)])

while queue:
    #큐에서 꺼내서 확인한다
    x,y = queue.popleft()
    #print(x1,y1,x,y)
    
    #현재 위치가 n,m에 도달했는지 확인
    if(x==n-1 and y==m-1):
        print(matrix[x][y]) #첫 시작 때 2로 시작하는 것을 마이너스로 보상해서 결과 출력 
        #for i in range(len(matrix)):
        #    print(matrix[i])
        break

    #현재 위치에서 갈 수 있는 길을 큐에 넣는다
    if(x+1<n and matrix[x+1][y] == 1): # 아래방향 가능 여부
        matrix[x+1][y] = matrix[x][y]+1
        queue.append((x+1,y))
    if(y+1<m and matrix[x][y+1]==1): # 오른쪽 방향 가능 여부
        matrix[x][y+1] = matrix[x][y]+1
        queue.append((x,y+1))
    if(x-1>=0 and matrix[x-1][y]==1): # 위쪽 방향 가능 여부
        matrix[x-1][y] = matrix[x][y]+1
        queue.append((x-1,y))
    if(y-1>=0 and matrix[x][y-1]==1): # 왼쪽 방향 가능 여부
        matrix[x][y-1] = matrix[x][y]+1
        queue.append((x,y-1))
