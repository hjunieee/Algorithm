def findHouse(x,y, count):
    if lines[x][y] == 1: #현재 위치가 집이면,
        lines[x][y] = house_num #다녀갔다고 표시
        count+=1
        
    #상하좌우로 집이 있는지 확인
    # 상
    if x - 1 >= 0 and lines[x-1][y] == 1:
        count = findHouse(x-1, y, count)

    # 하
    if x + 1 < n and lines[x+1][y] == 1:
        count = findHouse(x+1, y, count)

    # 좌
    if y - 1 >= 0 and lines[x][y-1] == 1:
        count = findHouse(x, y-1, count)

    # 우
    if y + 1 < n and lines[x][y+1] == 1:
        count = findHouse(x, y+1, count)
    
    return count




n = int(input())

lines = [list(map(int, input().strip())) for _ in range(n)]
#print(lines)

house_list = []

house_num = 2 #맵에 1과 중복을 피하기 위해 2번집부터로 시작

for i in range(n):
    for j in range(n):
        if(lines[i][j] == 1): #현재 위치에 집이 있으면
            res = findHouse(i,j, 0) #재귀적으로 탐색한다
            house_list.append(res)
            #print(res) #탐색된 결과(같은 집의 수) 출력
            house_num+=1 #집 번호 증가

house_list.sort()
print(house_num-2)
for i in range(len(house_list)):
    print(house_list[i])

